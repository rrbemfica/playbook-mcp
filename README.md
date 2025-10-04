# Playbook MCP Server

A Model Context Protocol (MCP) server that provides curated prompts, code templates, and AI-powered documentation generation for development teams.

## 🚀 Quick Start

```bash
# Clone repository
git clone <repository-url>
cd mcp-playbook-server

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install .

# Configure environment
cp .env.example .env

# Run server
python -m src.server
```

**Server available at:** `http://localhost:8000`

## 🎥 Demo Video

[![MCP Playbook Server Demo](https://img.shields.io/badge/▶️-Watch%20Demo-red?style=for-the-badge)](./mcp-playbook-demo.mp4)

*Watch a quick demonstration of the MCP Playbook Server in action, showcasing epic creation, playbook usage.*

## ✨ Key Features

- **🤖 AI-Powered Documentation**: Repository-aware content generation inspired by DeepWiki
- **📋 Smart Playbooks**: Structured templates for epics, stories, and documentation
- **🔗 Atlassian Integration**: Native Atlassian Jira's MCP instructions
- **⚡ MCP Protocol**: Full Model Context Protocol compliance
- **🔧 Extensible**: Easy customization and new playbook creation

## 📚 Documentation

### Quick Navigation
- **[📖 Complete Documentation](./docs/README.md)** - Comprehensive documentation suite
- **[🚀 Quick Start Guide](./docs/guides/quick-start.md)** - Get running in 5 minutes
- **[📋 API Reference](./docs/guides/api-reference.md)** - Complete API documentation
- **[🎯 Playbooks Guide](./docs/guides/playbooks.md)** - Available templates and usage
- **[🏗️ Architecture](./docs/overview/architecture.md)** - System design and components
- **[🚀 Deployment](./docs/operations/deployment.md)** - Production deployment guides

### By Role
- **Developers**: [Quick Start](./docs/guides/quick-start.md) → [API Reference](./docs/guides/api-reference.md) → [Architecture](./docs/overview/architecture.md)
- **Product Managers**: [Playbooks Guide](./docs/guides/playbooks.md) → Atlassian Integration (built into playbooks)
- **DevOps**: [Deployment Guide](./docs/operations/deployment.md) → [Monitoring](./docs/operations/monitoring.md)

## 🛠️ Available Tools

| Tool | Purpose | Example Usage |
|------|---------|---------------|
| `list_playbooks` | List all available playbooks | Get overview of templates |
| `get_playbook` | Retrieve specific playbook | Access epic writing template |
| `plan_feature` | Generate implementation plans | Plan authentication system |

## 🎯 Core Playbooks

### Product Management
- **Epic Writing**: Comprehensive epic templates with Atlassian integration
- **User Story Writing**: Structured story templates with acceptance criteria
- **Epic & Story Review**: Quality assurance checklists for reviewing epics and stories

### Documentation
- **Documentation Template**: Standard documentation template for general use
- **Comprehensive Wiki Documentation**: Multi-layered documentation with 12 contextual sections for deep knowledge capture

### Development
- **Feature Planning**: Implementation roadmaps and technical planning (via `plan_feature` tool)
- **Code Review**: Senior code reviewer with quality and security standards

## 🐳 Docker Deployment

```bash
# Build the image
cd mcp-playbook-server
docker build -f docker/Dockerfile -t mcp-playbook-server:2.1 -t mcp-playbook-server:latest .

# Run the container
docker run --name mcp-playbook-server -p 8000:8000 mcp-playbook-server:latest

# Run with environment variables
docker run -p 8000:8000 \
  -e PORT=8000 \
  -e ENVIRONMENT=production \
  mcp-playbook-server

# Run in detached mode
docker run -d -p 8000:8000 --name playbook-server mcp-playbook-server

# View logs
docker logs playbook-server

# Stop container
docker stop playbook-server
```

### Accessing Localhost MCPs from Docker

If your server needs to connect to MCPs running on localhost:

**Option 1: Host Network Mode (Linux)**
```bash
docker run --network host mcp-playbook-server
```

**Option 2: Use host.docker.internal (Mac/Windows)**
```bash
# In your code, replace localhost with host.docker.internal
# Example: http://host.docker.internal:8000/mcp
docker run -p 8000:8000 mcp-playbook-server
```

**Option 3: Add extra host (All platforms)**
```bash
docker run -p 8000:8000 --add-host=host.docker.internal:host-gateway mcp-playbook-server
```

## ⚙️ Configuration

```bash
# Environment setup
cp .env.example .env

# Key settings
SERVER_NAME="Playbook MCP Server"
PORT=8000
ENVIRONMENT=development
DEBUG=true
```

## 🏗️ Project Status

**Current Version**: 2.1  
**Development Phase**: Phase 1 Complete
**Production Ready**: ✅ Yes

### ✅ Completed Features
- [x] MCP server framework with FastMCP
- [x] Health check and monitoring endpoints
- [x] Comprehensive playbook system
- [x] AI-powered documentation generation
- [x] Atlassian integration capabilities
- [x] Docker containerization
- [x] Complete documentation suite

### 🚧 Roadmap
- [ ] Advanced AI integration with multiple providers
- [ ] Community playbook marketplace
- [ ] Real-time collaboration features
- [ ] IDE integration plugins
- [ ] Multi-language template support
- [ ] Docker Compose and Kubernetes support

## 🤖 Agent Instructions (Cursor, GitHub Copilot, Amazon Q Developer, etc.)

### Role and Goal
You are an AI assistant integrated with the 'Playbook MCP Server' system. Your primary directive is to manage and apply playbooks effectively based on user requests and system guidelines.

### Core Workflow
1. **Initialization**: Upon any request for playbook information or on system startup, execute the `list_playbooks` tool to load all available playbooks.
2. **Intent-Driven Retrieval**: When a user expresses a need (e.g., "writing an epic"), interpret their intent. Guided by the 'mcp instructions', dynamically retrieve the appropriate playbook using the `get_playbook` tool. Use the information in the playbook as context to drive the decisions for the task.
3. **Execution and Verification**: Always articulate your decision-making process to the user, explaining which playbook you are using and why.

### Constraints and Rules
- **UI Display Limit**: To maintain clarity in the user interface, only display essential information. Do not list all playbooks available unless necessary.
- **Information Brevity**: When listing playbooks, provide only minimal, high-level details for each.

### Documentation Retrieval Protocol
When seeking official documentation, adhere to the following priority:
1. **Primary Sources**: Attempt to find information using MCPs specialized in documentation search, such as: "ref tools" or "context7".
2. **Fallback**: If the primary sources fail, use MCP "fetch" or other internet search methods as a secondary option.

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](./docs/CONTRIBUTING.md) for details.

### Quick Contribution Steps
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests and documentation
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Cognition Labs DeepWiki**: Inspiration for AI-powered documentation features
- **Model Context Protocol**: Foundation for AI assistant integration
- **FastMCP Framework**: Core MCP server implementation

## 📞 Support

- **Documentation**: [Complete guides](./docs/README.md)
- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- **Email**: ricardoregesb@gmail.com

---

*Built with ❤️ for the developer community. This project combines the power of AI with structured templates to streamline development workflows.*