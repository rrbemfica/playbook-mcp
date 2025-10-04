# Quick Start Guide

Get the MCP Playbook Server running in 5 minutes.

## Prerequisites

- Python 3.8+
- pip package manager
- Git

## Installation

### 1. Clone Repository
```bash
git clone <repository-url>
cd mcp-playbook-server
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure
```bash
# Copy environment template
cp .env.example .env

# Edit configuration (optional)
# Default settings work for development
```

### 4. Run Server
```bash
python -m src.server
```

Server starts at `http://localhost:8080`

## Verify Installation

### Health Check
```bash
curl http://localhost:8080/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### List Available Tools
```bash
curl -X POST http://localhost:8080/tools/list_playbooks \
  -H "Content-Type: application/json" \
  -d '{}'
```

## First Steps

### 1. Explore Playbooks
```bash
# List all playbooks
curl -X POST http://localhost:8080/tools/list_playbooks -H "Content-Type: application/json" -d '{}'

# Get specific playbook
curl -X POST http://localhost:8080/tools/get_playbook \
  -H "Content-Type: application/json" \
  -d '{"playbook_id": "comprehensive_wiki"}'
```

### 2. Generate Feature Plan
```bash
curl -X POST http://localhost:8080/tools/plan_feature \
  -H "Content-Type: application/json" \
  -d '{
    "feature_description": "User authentication system",
    "project_type": "web",
    "complexity": "medium"
  }'
```

### 3. Create Code Review Checklist
```bash
curl -X POST http://localhost:8080/tools/code_review_checklist \
  -H "Content-Type: application/json" \
  -d '{
    "language": "python",
    "review_type": "security"
  }'
```

## Docker Quick Start

### Run with Docker
```bash
# Build image
docker build -f docker/Dockerfile -t mcp-playbook-server .

# Run container
docker run -p 8080:8080 mcp-playbook-server
```

### Docker Compose
```bash
# Create docker-compose.yml (see deployment guide)
docker-compose up -d
```

## Configuration Options

### Environment Variables
```bash
# .env file
SERVER_NAME="MCP Playbook Server"
PORT=8080
ENVIRONMENT=development
DEBUG=true
```

### Available Settings
| Variable | Default | Description |
|----------|---------|-------------|
| `SERVER_NAME` | "MCP Playbook Server" | Server identification |
| `PORT` | 8080 | HTTP server port |
| `ENVIRONMENT` | "development" | Runtime environment |
| `DEBUG` | false | Debug mode toggle |

## Troubleshooting

### Port Already in Use
```bash
# Check what's using port 8080
lsof -i :8080

# Kill process or change port in .env
PORT=8081
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Permission Issues
```bash
# Ensure proper permissions
chmod +x src/server.py
```

## Next Steps

- [API Reference](./api-reference.md) - Complete API documentation
- [Playbooks Guide](./playbooks.md) - Available templates and usage
- [Deployment Guide](../operations/deployment.md) - Production deployment
- [Architecture Overview](../overview/architecture.md) - System design

## Development Mode

### Enable Debug Logging
```bash
# In .env file
DEBUG=true
```

### Hot Reload (Development)
```bash
# Install development dependencies
pip install watchdog

# Run with auto-reload
python -m src.server --reload
```

### Testing
```bash
# Run tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src
```