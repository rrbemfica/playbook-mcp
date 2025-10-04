# API Reference

Complete API documentation for the MCP Playbook Server.

## Base Information

- **Base URL**: `http://localhost:8080`
- **Protocol**: HTTP/HTTPS
- **Format**: JSON
- **Authentication**: None required

## Health Endpoints

### GET /health
Basic health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /info
Server information and capabilities.

**Response:**
```json
{
  "name": "MCP Playbook Server",
  "version": "2.0",
  "description": "Enhanced MCP Playbook Server with AI documentation",
  "tools": ["list_playbooks", "get_playbook", "plan_feature"]
}
```

## MCP Tools

All tools follow the MCP protocol standard with POST requests to `/tools/{tool_name}`.

### list_playbooks

List all available playbooks.

**Endpoint:** `POST /tools/list_playbooks`

**Request:**
```json
{}
```

**Response:**
```json
{
  "total_playbooks": 4,
  "playbooks": [
    {
      "id": "product_owner_epic",
      "name": "Product Owner Epic Writing",
      "description": "Guide for writing comprehensive product epics",
      "category": "Product Management"
    },
    {
      "id": "comprehensive_wiki",
      "name": "Comprehensive Wiki Documentation",
      "description": "Multi-layered documentation with contextual sections",
      "category": "Documentation"
    },
    {
      "id": "epic_story_review",
      "name": "Epic & Story Review Checklist",
      "description": "Comprehensive review template for epic and story summaries",
      "category": "Product Management"
    }
  ],
  "categories": ["Product Management", "Documentation"]
}
```

### get_playbook

Retrieve a specific playbook template.

**Endpoint:** `POST /tools/get_playbook`

**Request:**
```json
{
  "playbook_id": "comprehensive_wiki"
}
```

**Parameters:**
- `playbook_id` (required): ID of the playbook to retrieve

**Response:**
```json
{
  "id": "comprehensive_wiki",
  "name": "Comprehensive Wiki Documentation",
  "description": "Multi-layered documentation with contextual sections",
  "category": "Documentation",
  "template": {
    "title": "[Project/Topic Name] - Comprehensive Wiki",
    "sections": [
      {
        "name": "Executive Summary",
        "content": "## What is this?\n[One-sentence description]"
      }
    ]
  },
  "folder_structure": {
    "recommended_layout": "docs/\n├── README.md (Executive Summary)\n├── overview/...",
    "instructions": ["Create a 'docs' folder in your project root"]
  },
  "usage_instructions": [
    "Create the recommended folder structure in your project",
    "Start with README.md (Executive Summary) as your main entry point"
  ]
}
```

### plan_feature

Generate a comprehensive feature implementation plan.

**Endpoint:** `POST /tools/plan_feature`

**Request:**
```json
{
  "feature_description": "User authentication system",
  "project_type": "web",
  "complexity": "medium"
}
```

**Parameters:**
- `feature_description` (required): Description of the feature to implement
- `project_type` (optional): Type of project (web, api, mobile, etc.) - default: "web"
- `complexity` (optional): Complexity level (simple, medium, complex) - default: "medium"

**Response:**
```json
{
  "feature": "User authentication system",
  "project_type": "web",
  "complexity": "medium",
  "implementation_steps": [
    {
      "phase": "Requirements Analysis",
      "tasks": [
        "Define functional requirements",
        "Identify non-functional requirements",
        "Map dependencies"
      ],
      "deliverables": ["Requirements document", "Dependency map"],
      "estimated_effort": "2-3 days"
    },
    {
      "phase": "Design",
      "tasks": [
        "Create system architecture",
        "Design database schema",
        "Define API contracts"
      ],
      "deliverables": ["Architecture diagram", "Database schema", "API specification"],
      "estimated_effort": "3-5 days"
    }
  ],
  "technical_considerations": [
    "Security: Implement proper password hashing",
    "Performance: Consider session management strategy",
    "Scalability: Design for horizontal scaling"
  ],
  "next_actions": [
    "Create Jira epic with this plan",
    "Estimate detailed effort and timeline",
    "Identify team members and skills needed"
  ]
}
```

## Error Handling

### Error Response Format
```json
{
  "error": "Error description",
  "code": "ERROR_CODE",
  "details": {
    "parameter": "invalid_value",
    "expected": "valid_format"
  }
}
```

### Common Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| `PLAYBOOK_NOT_FOUND` | Requested playbook ID doesn't exist | Check available playbooks with `list_playbooks` |
| `INVALID_PARAMETERS` | Required parameters missing or invalid | Verify request parameters match schema |
| `TOOL_EXECUTION_ERROR` | Error during tool execution | Check server logs for details |
| `VALIDATION_ERROR` | Parameter validation failed | Ensure parameters match expected types |

### HTTP Status Codes

| Status | Meaning | When Used |
|--------|---------|-----------|
| 200 | Success | Tool executed successfully |
| 400 | Bad Request | Invalid parameters or malformed request |
| 404 | Not Found | Tool or playbook not found |
| 500 | Internal Server Error | Server-side error during execution |

## Rate Limiting

Currently no rate limiting is implemented. For production use, consider implementing:
- Request rate limits per IP
- Tool-specific rate limits
- Burst protection

## CORS Policy

CORS is enabled for all origins in development mode. For production:
```python
# Configure CORS appropriately
CORS_ORIGINS = ["https://yourdomain.com"]
```

## Authentication

No authentication is currently required, following the DeepWiki approach for development tools. For production use, consider:
- API key authentication
- JWT token validation
- OAuth integration

## Examples

### Python Client
```python
import requests

# List playbooks
response = requests.post(
    "http://localhost:8080/tools/list_playbooks",
    json={}
)
playbooks = response.json()

# Generate feature plan
response = requests.post(
    "http://localhost:8080/tools/plan_feature",
    json={
        "feature_description": "User authentication",
        "project_type": "web",
        "complexity": "medium"
    }
)
plan = response.json()
```

### JavaScript Client
```javascript
// List playbooks
const response = await fetch('http://localhost:8080/tools/list_playbooks', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({})
});
const playbooks = await response.json();

// Get playbook
const playbookResponse = await fetch('http://localhost:8080/tools/get_playbook', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ playbook_id: 'enhanced_deep_wiki' })
});
const playbook = await playbookResponse.json();
```

### cURL Examples
```bash
# Health check
curl http://localhost:8080/health

# List playbooks
curl -X POST http://localhost:8080/tools/list_playbooks \
  -H "Content-Type: application/json" \
  -d '{}'

# Generate feature plan
curl -X POST http://localhost:8080/tools/plan_feature \
  -H "Content-Type: application/json" \
  -d '{"feature_description": "User authentication", "project_type": "web"}' 
```

## OpenAPI Specification

The server provides an OpenAPI specification at `/openapi.json` for automatic client generation and API documentation tools.

## WebSocket Support

Currently not implemented. Future versions may include WebSocket support for:
- Real-time tool execution updates
- Streaming responses for large content generation
- Live collaboration features