# Architecture Overview

Simple architecture documentation for the MCP Playbook Server.

## System Overview

The MCP Playbook Server is a lightweight MCP server built with FastMCP that provides curated playbook templates for product management, documentation, and code review workflows.

```
┌─────────────────────────────────────────┐
│        MCP Playbook Server             │
├─────────────────────────────────────────┤
│  ┌──────────────────────────────────┐  │
│  │      FastMCP Framework           │  │
│  │  (HTTP Server + MCP Protocol)    │  │
│  └──────────────────────────────────┘  │
├─────────────────────────────────────────┤
│  ┌──────────────────────────────────┐  │
│  │         MCP Tools                │  │
│  │  • list_playbooks()              │  │
│  │  • get_playbook(id)              │  │
│  │  • plan_feature(...)             │  │
│  └──────────────────────────────────┘  │
├─────────────────────────────────────────┤
│  ┌──────────────────────────────────┐  │
│  │    Playbook Registry             │  │
│  │  (In-memory dictionary)          │  │
│  └──────────────────────────────────┘  │
├─────────────────────────────────────────┤
│  ┌──────────────────────────────────┐  │
│  │    Configuration                 │  │
│  │  (Pydantic Settings)             │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## Core Components

### 1. FastMCP Framework

**Purpose**: Provides MCP protocol implementation and HTTP server

**Implementation**:
```python
from fastmcp import FastMCP

mcp = FastMCP("Playbook MCP Server")

@mcp.tool()
def list_playbooks() -> Dict[str, Any]:
    """Tool implementation with automatic registration"""
    return {"playbooks": [...], "total_playbooks": 6}
```

**Features**:
- Automatic tool registration via decorators
- JSON schema validation
- HTTP transport on port 8000

### 2. MCP Tools

**Available Tools**:

1. **list_playbooks()** - Returns all available playbooks with metadata
2. **get_playbook(playbook_id)** - Retrieves specific playbook template
3. **plan_feature(feature_description, project_type, complexity)** - Generates implementation plans

### 3. Playbook Registry

**Purpose**: In-memory storage of playbook templates

**Structure**:
```python
PLAYBOOKS = {
    "playbook_id": {
        "name": str,
        "description": str,
        "category": str,
        "template": {
            "title": str,
            "sections": [...]
        }
    }
}
```

**Available Playbooks**:

1. **Product Management**
   - `product_owner_epic` - Epic writing with Atlassian integration
   - `product_owner_story` - User story templates
   - `epic_story_review` - Review checklist for epics/stories

2. **Documentation**
   - `documentation` - Basic documentation template
   - `comprehensive_wiki` - Multi-layered wiki structure

3. **Development**
   - `code_review` - Code review checklist

### 4. Configuration

**Purpose**: Environment-based settings management

**Implementation**:
```python
class Settings(BaseSettings):
    server_name: str = "Playbook MCP Server"
    port: int = 8000
    environment: str = "development"
```

**Configuration Source**: `.env` file or environment variables

## Data Flow

```
MCP Client Request
       ↓
FastMCP HTTP Server
       ↓
Tool Execution (list_playbooks/get_playbook/plan_feature)
       ↓
Playbook Registry Lookup
       ↓
JSON Response
       ↓
MCP Client
```

## Integration Points

**Atlassian Integration**:
- Playbooks include instructions for using Atlassian MCP tools
- Integration guidance for Jira issue creation/editing
- No direct Atlassian API calls in this server

**Code Issues Integration**:
- Code review playbook includes displayFindings tool instructions
- No direct implementation of code analysis

## File Structure

```
mcp-playbook-server/
├── src/
│   ├── server.py          # Main server + tools + playbooks
│   ├── config.py          # Configuration settings
│   └── __init__.py
├── docs/                  # Documentation
├── docker/                # Docker configuration
├── pyproject.toml         # Dependencies
└── README.md
```

## Technology Stack

- **Framework**: FastMCP
- **Language**: Python 3.x
- **Configuration**: Pydantic Settings
- **Transport**: HTTP
- **Protocol**: Model Context Protocol (MCP)ntralized configuration and environment management

**Configuration Hierarchy**:
```
Environment Variables (Highest Priority)
    ↓
.env Files
    ↓
Configuration Files
    ↓
Default Values (Lowest Priority)
```

**Settings Schema**:
```python
class Settings(BaseSettings):
    # Server Configuration
    server_name: str = "MCP Playbook Server"
    port: int = 8000
    environment: str = "development"
    debug: bool = False
    
    # Logging Configuration
    log_level: str = "INFO"
    log_format: str = "json"
    
    # Security Configuration
    cors_origins: List[str] = ["*"]
    rate_limit_enabled: bool = False
    rate_limit_requests: int = 100
    rate_limit_window: int = 60
    
    # AI Configuration
    ai_enabled: bool = True
    ai_provider: str = "openai"
    ai_model: str = "gpt-4"
    
    # Monitoring Configuration
    metrics_enabled: bool = True
    health_check_interval: int = 30
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
```

## Data Flow Architecture

### Request Processing Flow

```
1. Client Request → 2. MCP Protocol → 3. Tool Routing → 4. Validation
        ↓                    ↓               ↓              ↓
8. Response ← 7. Formatting ← 6. Processing ← 5. Execution
```

**Detailed Flow Description**:

1. **Client Request**: HTTP POST with tool name and JSON parameters
2. **MCP Protocol**: FastMCP handles protocol-specific processing and validation
3. **Tool Routing**: Request routed to appropriate tool handler based on tool name
4. **Validation**: Parameter validation using Pydantic schemas and business rules
5. **Execution**: Tool logic execution with comprehensive error handling
6. **Processing**: Business logic execution, template processing, AI generation
7. **Formatting**: Response formatting according to MCP standards and client expectations
8. **Response**: Structured JSON response returned to client with metadata

### Playbook Processing Flow

```
Playbook Request → Registry Lookup → Template Retrieval → Content Generation
       ↓                 ↓               ↓                    ↓
   Response ← Formatting ← Validation ← Processing ← AI Enhancement
```

**AI-Enhanced Processing Flow** (for comprehensive_wiki):
```
Repository Analysis → Pattern Recognition → Content Generation → Template Population
        ↓                     ↓                    ↓                   ↓
   Quality Review ← Human Oversight ← AI Validation ← Content Integration
```

### Error Handling Flow

```
Error Occurrence → Error Classification → Error Logging → Error Response
       ↓                    ↓                ↓              ↓
   Recovery ← Notification ← Monitoring ← Client Response
```

## Security Architecture

### Security Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    Security Layers                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   Transport     │  │   Application   │  │    Data     │ │
│  │   Security      │  │   Security      │  │  Security   │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   Network       │  │   Container     │  │   Runtime   │ │
│  │   Security      │  │   Security      │  │  Security   │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Security Implementation**:

1. **Transport Security**
   - HTTPS/TLS 1.3 in production
   - Certificate management and rotation
   - Secure headers (HSTS, CSP, etc.)

2. **Input Validation**
   - Pydantic schema validation for all inputs
   - SQL injection prevention
   - XSS protection
   - Parameter sanitization

3. **Authentication & Authorization** (Future)
   - JWT token validation
   - Role-based access control (RBAC)
   - API key management
   - OAuth 2.0 integration

4. **Container Security**
   - Non-root user execution
   - Read-only filesystem
   - Minimal base images
   - Security scanning

## Scalability Architecture

### Horizontal Scaling Design

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │   Load Balancer │    │   Load Balancer │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  MCP Server 1   │    │  MCP Server 2   │    │  MCP Server N   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
┌─────────────────────────────────────────────────────────────────┐
│                    Shared Configuration                        │
└─────────────────────────────────────────────────────────────────┘
```

**Scaling Characteristics**:
- **Stateless Design**: No session state maintained between requests
- **Independent Processing**: Each request processed independently
- **Shared Configuration**: Common configuration across all instances
- **Load Distribution**: Even distribution of tool requests across instances
- **Auto-scaling**: Kubernetes HPA based on CPU/memory metrics

### Performance Optimization

**Caching Strategy**:
```python
class CacheManager:
    def __init__(self):
        self.template_cache = TTLCache(maxsize=100, ttl=3600)
        self.playbook_cache = TTLCache(maxsize=50, ttl=1800)
        
    @cached(cache=template_cache)
    def get_template(self, playbook_id: str) -> Dict[str, Any]:
        """Cache playbook templates for faster access"""
        return load_playbook_template(playbook_id)
```

**Connection Management**:
```python
# Async HTTP client with connection pooling
connector = aiohttp.TCPConnector(
    limit=100,              # Total connection pool size
    limit_per_host=30,      # Per-host connection limit
    ttl_dns_cache=300,      # DNS cache TTL
    use_dns_cache=True,     # Enable DNS caching
)
```

## Integration Architecture

### External Integrations

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP Playbook Server                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Atlassian     │  │   AI Services   │  │   Repository    │ │
│  │   Integration   │  │   Integration   │  │   Analysis      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Monitoring    │  │    Logging      │  │   Metrics       │ │
│  │   Services      │  │   Services      │  │   Collection    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

**Integration Patterns**:

1. **Plugin Architecture**
```python
class IntegrationPlugin:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute integration logic"""
        raise NotImplementedError
        
class AtlassianPlugin(IntegrationPlugin):
    async def create_epic(self, epic_data: Dict[str, Any]) -> str:
        """Create Jira epic using Atlassian API"""
        return await self.jira_client.create_issue(epic_data)
```

2. **Circuit Breaker Pattern**
```python
class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
```

3. **Retry Logic**
```python
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(ConnectionError)
)
async def call_external_service(self, request: Dict[str, Any]) -> Dict[str, Any]:
    """Call external service with retry logic"""
    return await self.http_client.post(self.endpoint, json=request)
```

## Deployment Architecture

### Container Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Docker Container                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                  Python Runtime                            │ │
│  ├─────────────────────────────────────────────────────────────┤ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │ │
│  │  │   FastMCP       │  │   Pydantic      │  │   Python    │ │ │
│  │  │   Framework     │  │   Validation    │  │   Dotenv    │ │ │
│  │  └─────────────────┘  └─────────────────┘  └─────────────┘ │ │
│  ├─────────────────────────────────────────────────────────────┤ │
│  │                  Application Code                          │ │
│  └─────────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                    Base OS (Alpine Linux)                      │
└─────────────────────────────────────────────────────────────────┘
```

### Kubernetes Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Kubernetes Cluster                        │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │    Ingress      │  │   Service       │  │   ConfigMap     │ │
│  │   Controller    │  │   Discovery     │  │   Management    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Deployment    │  │   ReplicaSet    │  │     Pods        │ │
│  │   Controller    │  │   Management    │  │   (Containers)  │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Monitoring and Observability

### Observability Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                    Observability Layer                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │    Metrics      │  │     Logging     │  │     Tracing     │ │
│  │  (Prometheus)   │  │  (Structured)   │  │   (Optional)    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Dashboards    │  │     Alerts      │  │   Health        │ │
│  │   (Grafana)     │  │ (AlertManager)  │  │    Checks       │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

**Key Metrics**:
- Request rate and latency percentiles
- Tool execution times and success rates
- Error rates by tool and error type
- Memory and CPU usage patterns
- Playbook usage statistics and trends
- AI generation success rates and quality scores

**Logging Strategy**:
```python
import structlog

logger = structlog.get_logger()

# Structured logging with context
logger.info(
    "Tool executed successfully",
    tool_name="plan_feature",
    execution_time=0.245,
    user_id="user123",
    request_id="req456"
)
```

## Future Architecture Considerations

### Planned Enhancements

1. **Microservices Architecture**
   - Split into specialized services (playbook service, AI service, etc.)
   - Service mesh for inter-service communication
   - Independent scaling and deployment

2. **Event-Driven Architecture**
   - Event streaming with Kafka/Redis
   - Asynchronous processing pipelines
   - Event sourcing for audit trails

3. **Advanced Caching**
   - Redis cluster for distributed caching
   - CDN integration for static content
   - Intelligent cache invalidation

4. **Database Integration**
   - PostgreSQL for persistent storage
   - Analytics database for usage metrics
   - Time-series database for monitoring data

### Technology Evolution Roadmap

- **Phase 1**: Current stateless architecture with in-memory caching
- **Phase 2**: Redis integration and enhanced monitoring
- **Phase 3**: Microservices decomposition and event streaming
- **Phase 4**: Advanced AI integration and multi-region deployment
- **Phase 5**: Full event-driven architecture with real-time capabilities

This architecture provides a solid foundation for current needs while enabling future growth and enhancement.