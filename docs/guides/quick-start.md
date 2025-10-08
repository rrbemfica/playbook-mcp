# Quick Start Guide

Get the MCP Playbook Server running in 5 minutes.

## Prerequisites

- Python 3.11+
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
pip install .
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

Server starts at `http://localhost:8000`

## Verify Installation

The server runs on HTTP transport using the MCP protocol. It's designed to be used with MCP-compatible clients (Claude Desktop, IDEs with MCP support, etc.), not direct HTTP/cURL access.

### Check Server is Running
```bash
# Server should display startup message
# MCP Playbook Server running on http://0.0.0.0:8000
```

## Using with MCP Clients

### Configure MCP Client

#### Option 1: Streamable (HTTP) Connection

First, start the server:
```bash
python -m src.server
```

Then add to your MCP client configuration (e.g., Claude Desktop config):

```json
{
  "mcpServers": {
    "playbook-server": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

#### Option 2: Command-based Connection

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "playbook-server": {
      "command": "python",
      "args": ["-m", "src.server"],
      "cwd": "/path/to/mcp-playbook-server"
    }
  }
}
```

### Available Tools

Once connected via MCP client:
- `list_playbooks()` - List all 6 available playbooks
- `get_playbook(playbook_id)` - Get specific playbook template
- `plan_feature(feature_description, project_type, complexity)` - Generate implementation plan



## Docker Quick Start

### Run with Docker
```bash
# Build image
docker build -f docker/Dockerfile -t mcp-playbook-server .

# Run container
docker run -p 8000:8000 mcp-playbook-server
```

### Docker Compose
```bash
# Navigate to docker folder
cd docker

# Start with docker-compose
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f mcp-server
```

## Configuration Options

### Environment Variables
```bash
# .env file
SERVER_NAME="MCP Playbook Server"
PORT=8000
ENVIRONMENT=development
DEBUG=true
```

### Available Settings
| Variable | Default | Description |
|----------|---------|-------------|
| `SERVER_NAME` | "Playbook MCP Server" | Server identification |
| `PORT` | 8000 | HTTP server port |
| `ENVIRONMENT` | "development" | Runtime environment |

## Troubleshooting

### Port Already in Use
```bash
# Check what's using port 8000
lsof -i :8000

# Kill process or change port in .env
PORT=8081
```

### Import Errors
```bash
# Reinstall dependencies
pip install . --force-reinstall
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

### Run in Development
```bash
# Set environment to development
ENVIRONMENT=development python -m src.server
```

**Note**: Hot reload and testing features are not currently implemented. The server provides a simple MCP interface for playbook templates.