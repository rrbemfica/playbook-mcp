# Deployment Guide

Comprehensive deployment guide for the MCP Playbook Server across different environments.

## Overview

This guide covers deployment options from local development to production environments, including Docker, Kubernetes, and cloud platforms.

## Local Development

### Prerequisites
- Python 3.8+
- pip package manager
- Git
- Optional: Docker for containerized development

### Setup Steps

```bash
# Clone repository
git clone <repository-url>
cd mcp-playbook-server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run server
python -m src.server
```

### Development Configuration

```bash
# .env for development
SERVER_NAME="MCP Playbook Server - Dev"
PORT=8080
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG
```

### Development Tools

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run with hot reload
python -m src.server --reload

# Run tests
python -m pytest tests/ -v

# Code formatting
black src/ tests/
isort src/ tests/

# Linting
flake8 src/ tests/
mypy src/
```

## Docker Deployment

### Single Container

```bash
# Build image
docker build -f docker/Dockerfile -t mcp-playbook-server .

# Run container
docker run -p 8080:8080 \
  -e ENVIRONMENT=production \
  -e DEBUG=false \
  --name mcp-server \
  mcp-playbook-server
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  mcp-server:
    build:
      context: .
      dockerfile: docker/Dockerfile
    ports:
      - "8080:8080"
    environment:
      - ENVIRONMENT=production
      - DEBUG=false
      - SERVER_NAME=MCP Playbook Server
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    volumes:
      - ./logs:/app/logs
    networks:
      - mcp-network

  # Optional: Add monitoring
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - mcp-network

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-storage:/var/lib/grafana
    networks:
      - mcp-network

networks:
  mcp-network:
    driver: bridge

volumes:
  grafana-storage:
```

```bash
# Deploy with compose
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f mcp-server

# Scale service
docker-compose up -d --scale mcp-server=3

# Update service
docker-compose pull
docker-compose up -d
```

### Multi-stage Dockerfile

```dockerfile
# docker/Dockerfile.multi-stage
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim as runtime

# Create non-root user
RUN groupadd -r mcp && useradd -r -g mcp mcp

# Copy dependencies from builder
COPY --from=builder /root/.local /home/mcp/.local

# Set up application
WORKDIR /app
COPY src/ ./src/
COPY .env.example .env

# Set ownership
RUN chown -R mcp:mcp /app

# Switch to non-root user
USER mcp

# Update PATH
ENV PATH=/home/mcp/.local/bin:$PATH

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

CMD ["python", "-m", "src.server"]
```

## Kubernetes Deployment

### Basic Deployment

```yaml
# k8s/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: mcp-playbook
  labels:
    name: mcp-playbook
---
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mcp-server-config
  namespace: mcp-playbook
data:
  SERVER_NAME: "MCP Playbook Server - Production"
  ENVIRONMENT: "production"
  DEBUG: "false"
  PORT: "8080"
  LOG_LEVEL: "INFO"
---
# k8s/secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: mcp-server-secrets
  namespace: mcp-playbook
type: Opaque
data:
  # Add any sensitive configuration here (base64 encoded)
  api_key: <base64-encoded-api-key>
---
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-playbook-server
  namespace: mcp-playbook
  labels:
    app: mcp-playbook-server
    version: v2.0
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  selector:
    matchLabels:
      app: mcp-playbook-server
  template:
    metadata:
      labels:
        app: mcp-playbook-server
        version: v2.0
    spec:
      containers:
      - name: mcp-server
        image: mcp-playbook-server:2.0
        ports:
        - containerPort: 8080
          name: http
        envFrom:
        - configMapRef:
            name: mcp-server-config
        - secretRef:
            name: mcp-server-secrets
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
        volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: logs
          mountPath: /app/logs
      volumes:
      - name: tmp
        emptyDir: {}
      - name: logs
        emptyDir: {}
      securityContext:
        fsGroup: 1000
---
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mcp-playbook-service
  namespace: mcp-playbook
  labels:
    app: mcp-playbook-server
spec:
  selector:
    app: mcp-playbook-server
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
    name: http
  type: ClusterIP
---
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mcp-playbook-ingress
  namespace: mcp-playbook
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  tls:
  - hosts:
    - mcp.yourdomain.com
    secretName: mcp-tls
  rules:
  - host: mcp.yourdomain.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mcp-playbook-service
            port:
              number: 80
```

### Horizontal Pod Autoscaler

```yaml
# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: mcp-playbook-hpa
  namespace: mcp-playbook
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: mcp-playbook-server
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
```

### Deployment Commands

```bash
# Apply all configurations
kubectl apply -f k8s/

# Check deployment status
kubectl get all -n mcp-playbook

# View logs
kubectl logs -l app=mcp-playbook-server -n mcp-playbook

# Scale deployment
kubectl scale deployment mcp-playbook-server --replicas=5 -n mcp-playbook

# Rolling update
kubectl set image deployment/mcp-playbook-server mcp-server=mcp-playbook-server:2.1 -n mcp-playbook

# Check rollout status
kubectl rollout status deployment/mcp-playbook-server -n mcp-playbook

# Rollback if needed
kubectl rollout undo deployment/mcp-playbook-server -n mcp-playbook
```

## Cloud Platform Deployments

### AWS ECS Fargate

```json
{
  "family": "mcp-playbook-server",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "executionRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskExecutionRole",
  "taskRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskRole",
  "containerDefinitions": [
    {
      "name": "mcp-server",
      "image": "ACCOUNT.dkr.ecr.REGION.amazonaws.com/mcp-playbook-server:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {"name": "ENVIRONMENT", "value": "production"},
        {"name": "DEBUG", "value": "false"},
        {"name": "PORT", "value": "8080"}
      ],
      "secrets": [
        {
          "name": "API_KEY",
          "valueFrom": "arn:aws:secretsmanager:REGION:ACCOUNT:secret:mcp-api-key"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/mcp-playbook-server",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 60
      }
    }
  ]
}
```

### AWS ECS Service

```json
{
  "serviceName": "mcp-playbook-service",
  "cluster": "production-cluster",
  "taskDefinition": "mcp-playbook-server:1",
  "desiredCount": 3,
  "launchType": "FARGATE",
  "networkConfiguration": {
    "awsvpcConfiguration": {
      "subnets": ["subnet-12345", "subnet-67890"],
      "securityGroups": ["sg-abcdef"],
      "assignPublicIp": "ENABLED"
    }
  },
  "loadBalancers": [
    {
      "targetGroupArn": "arn:aws:elasticloadbalancing:REGION:ACCOUNT:targetgroup/mcp-tg/1234567890123456",
      "containerName": "mcp-server",
      "containerPort": 8080
    }
  ],
  "serviceRegistries": [
    {
      "registryArn": "arn:aws:servicediscovery:REGION:ACCOUNT:service/srv-1234567890123456"
    }
  ]
}
```

### Google Cloud Run

```yaml
# cloudrun.yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: mcp-playbook-server
  annotations:
    run.googleapis.com/ingress: all
    run.googleapis.com/cpu-throttling: "false"
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/maxScale: "100"
        autoscaling.knative.dev/minScale: "1"
        run.googleapis.com/execution-environment: gen2
    spec:
      containerConcurrency: 100
      timeoutSeconds: 300
      containers:
      - image: gcr.io/PROJECT-ID/mcp-playbook-server:latest
        ports:
        - containerPort: 8080
        env:
        - name: ENVIRONMENT
          value: production
        - name: PORT
          value: "8080"
        - name: DEBUG
          value: "false"
        resources:
          limits:
            cpu: "2"
            memory: "2Gi"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        startupProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          failureThreshold: 10
```

```bash
# Deploy to Cloud Run
gcloud run deploy mcp-playbook-server \
  --image gcr.io/PROJECT-ID/mcp-playbook-server:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars ENVIRONMENT=production,DEBUG=false \
  --memory 2Gi \
  --cpu 2 \
  --concurrency 100 \
  --max-instances 100 \
  --min-instances 1
```

### Azure Container Instances

```yaml
# azure-container-instance.yaml
apiVersion: 2019-12-01
location: eastus
name: mcp-playbook-server
properties:
  containers:
  - name: mcp-server
    properties:
      image: youracr.azurecr.io/mcp-playbook-server:latest
      ports:
      - port: 8080
        protocol: TCP
      environmentVariables:
      - name: ENVIRONMENT
        value: production
      - name: DEBUG
        value: "false"
      - name: PORT
        value: "8080"
      resources:
        requests:
          cpu: 1
          memoryInGB: 2
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 30
        periodSeconds: 10
  osType: Linux
  restartPolicy: Always
  ipAddress:
    type: Public
    ports:
    - protocol: TCP
      port: 8080
  imageRegistryCredentials:
  - server: youracr.azurecr.io
    username: <username>
    password: <password>
tags:
  environment: production
  service: mcp-playbook-server
type: Microsoft.ContainerInstance/containerGroups
```

## CI/CD Pipeline

### GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Build and Deploy MCP Playbook Server

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        
    - name: Cache dependencies
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
        
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
        
    - name: Lint code
      run: |
        flake8 src/ tests/
        black --check src/ tests/
        isort --check-only src/ tests/
        
    - name: Type check
      run: mypy src/
      
    - name: Run tests
      run: |
        pytest tests/ -v --cov=src --cov-report=xml
        
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
    - uses: actions/checkout@v4
    
    - name: Log in to Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
        
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
          
    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        context: .
        file: docker/Dockerfile
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    environment: staging
    steps:
    - name: Deploy to staging
      run: |
        echo "Deploying to staging environment"
        # Add staging deployment commands

  deploy-production:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
    - name: Deploy to production
      run: |
        echo "Deploying to production environment"
        # Add production deployment commands
```

### GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  DOCKER_LATEST: $CI_REGISTRY_IMAGE:latest

before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

test:
  stage: test
  image: python:3.11
  services:
    - docker:dind
  script:
    - pip install -r requirements.txt -r requirements-dev.txt
    - flake8 src/ tests/
    - black --check src/ tests/
    - mypy src/
    - pytest tests/ -v --cov=src
  coverage: '/TOTAL.*\s+(\d+%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -f docker/Dockerfile -t $DOCKER_IMAGE -t $DOCKER_LATEST .
    - docker push $DOCKER_IMAGE
    - docker push $DOCKER_LATEST
  only:
    - main
    - develop

deploy-staging:
  stage: deploy
  image: kubectl:latest
  script:
    - kubectl config use-context staging
    - kubectl set image deployment/mcp-playbook-server mcp-server=$DOCKER_IMAGE -n mcp-staging
    - kubectl rollout status deployment/mcp-playbook-server -n mcp-staging
  environment:
    name: staging
    url: https://mcp-staging.yourdomain.com
  only:
    - develop

deploy-production:
  stage: deploy
  image: kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/mcp-playbook-server mcp-server=$DOCKER_IMAGE -n mcp-production
    - kubectl rollout status deployment/mcp-playbook-server -n mcp-production
  environment:
    name: production
    url: https://mcp.yourdomain.com
  when: manual
  only:
    - main
```

## Production Considerations

### Environment Configuration

```bash
# Production .env
SERVER_NAME="MCP Playbook Server - Production"
PORT=8080
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO

# Security
CORS_ORIGINS=https://yourdomain.com,https://app.yourdomain.com
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60

# Monitoring
METRICS_ENABLED=true
HEALTH_CHECK_INTERVAL=30
```

### Security Hardening

1. **Container Security**
```dockerfile
# Use non-root user
RUN groupadd -r mcp && useradd -r -g mcp mcp
USER mcp

# Read-only filesystem
VOLUME ["/tmp", "/var/log"]
```

2. **Network Security**
```yaml
# Kubernetes NetworkPolicy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: mcp-network-policy
spec:
  podSelector:
    matchLabels:
      app: mcp-playbook-server
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 8080
```

3. **Secrets Management**
```yaml
# Use external secrets operator
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: vault-backend
spec:
  provider:
    vault:
      server: "https://vault.yourdomain.com"
      path: "secret"
      version: "v2"
      auth:
        kubernetes:
          mountPath: "kubernetes"
          role: "mcp-server"
```

### Monitoring and Observability

```yaml
# Prometheus ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: mcp-playbook-server
spec:
  selector:
    matchLabels:
      app: mcp-playbook-server
  endpoints:
  - port: http
    path: /metrics
    interval: 30s
```

### Backup and Disaster Recovery

```bash
# Backup configuration
kubectl get configmap mcp-server-config -o yaml > backup/configmap.yaml
kubectl get secret mcp-server-secrets -o yaml > backup/secrets.yaml

# Database backup (if applicable)
pg_dump mcp_database > backup/database.sql

# Container image backup
docker save mcp-playbook-server:latest | gzip > backup/image.tar.gz
```

## Troubleshooting

### Common Deployment Issues

1. **Container Won't Start**
```bash
# Check logs
docker logs <container-id>
kubectl logs <pod-name>

# Check resource limits
kubectl describe pod <pod-name>
```

2. **Health Check Failures**
```bash
# Test health endpoint
curl -f http://localhost:8080/health

# Check container health
docker inspect <container-id> | grep Health
```

3. **Network Connectivity Issues**
```bash
# Test from within cluster
kubectl run test-pod --image=curlimages/curl -it --rm -- /bin/sh
curl http://mcp-playbook-service/health
```

4. **Resource Constraints**
```bash
# Check resource usage
kubectl top pods
kubectl describe node <node-name>
```

### Performance Optimization

1. **Resource Tuning**
```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "200m"
  limits:
    memory: "1Gi"
    cpu: "1000m"
```

2. **Caching Strategy**
```python
# Add Redis for caching
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
cache = redis.Redis.from_url(REDIS_URL)
```

3. **Connection Pooling**
```python
# Configure connection limits
MAX_CONNECTIONS = 100
POOL_SIZE = 20
```

This comprehensive deployment guide covers all major deployment scenarios and production considerations for the MCP Playbook Server.