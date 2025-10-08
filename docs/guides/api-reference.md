# API Reference

Complete API documentation for the MCP Playbook Server.

## Base Information

- **Base URL**: `http://localhost:8000`
- **Protocol**: HTTP/HTTPS
- **Format**: JSON
- **Authentication**: None required

## MCP Protocol

This server implements the Model Context Protocol (MCP). It does not expose traditional REST endpoints like `/health` or `/info`. Instead, it uses MCP tools accessed through MCP clients.

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
  "total_playbooks": 6,
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
      ]
    },
    {
      "phase": "Technical Design",
      "tasks": [
        "Architecture planning",
        "Database schema (if needed)",
        "API design (if applicable)"
      ]
    },
    {
      "phase": "Development",
      "tasks": [
        "Set up development environment",
        "Implement core functionality",
        "Add error handling"
      ]
    },
    {
      "phase": "Testing",
      "tasks": [
        "Unit tests",
        "Integration tests",
        "User acceptance testing"
      ]
    },
    {
      "phase": "Deployment",
      "tasks": [
        "Staging deployment",
        "Production deployment",
        "Monitoring setup"
      ]
    }
  ],
  "next_actions": [
    "Create Jira ticket with this plan",
    "Estimate effort and timeline",
    "Assign team members",
    "Begin requirements gathering"
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

## Server Configuration

The server runs on HTTP transport with configurable settings:
- **Host**: 0.0.0.0
- **Port**: 8000 (configurable via environment)
- **Transport**: HTTP
- **Protocol**: MCP (Model Context Protocol)

## Examples

### Python Client
```python
import requests

# List playbooks
response = requests.post(
    "http://localhost:8000/tools/list_playbooks",
    json={}
)
playbooks = response.json()

# Generate feature plan
response = requests.post(
    "http://localhost:8000/tools/plan_feature",
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
const response = await fetch('http://localhost:8000/tools/list_playbooks', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({})
});
const playbooks = await response.json();

// Get playbook
const playbookResponse = await fetch('http://localhost:8000/tools/get_playbook', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ playbook_id: 'comprehensive_wiki' })
});
const playbook = await playbookResponse.json();
```

### MCP Client Usage

This server is designed to be used with MCP-compatible clients (like Claude Desktop, IDEs with MCP support, etc.). Direct HTTP/cURL access is not the intended usage pattern.

For testing purposes, you can use MCP client libraries or tools that support the MCP protocol.