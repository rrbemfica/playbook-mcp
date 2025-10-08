# Changelog

All notable changes to the MCP Playbook Server project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.1] - 2025-10-07

### Documentation Overhaul
- **Architecture**: Simplified architecture.md to reflect actual FastMCP implementation, removed fictional AI features and Kubernetes support
- **Playbooks**: Added critical_instructions to documentation and comprehensive_wiki playbooks enforcing code-first documentation approach
- **API Reference**: Removed non-existent REST endpoints (/health, /info), clarified MCP protocol usage, fixed plan_feature response structure
- **Quick Start**: Added streamable HTTP connection example (http://localhost:8000/mcp), removed fictional hot reload and testing features
- **Playbooks Guide**: Removed Python client code examples, added missing code_review and epic_story_review playbooks
- **Deployment**: Simplified Docker Compose section to match actual docker-compose.yml

### Added
- docker-compose.yml in docker/ folder for containerized deployment
- Streamable MCP connection configuration example
- Critical instructions in playbooks to prevent documenting non-existent features

### Changed
- All dates in changelog updated to match actual git history (Sept-Oct 2025)
- Server description from "Enhanced MCP Playbook Server with AI documentation" to "MCP Playbook Server for curated prompts and templates"
- Documentation now accurately represents 6 template-based playbooks (not AI-powered)

### Removed
- Fictional features: AI-powered content generation, DeepWiki references, repository analysis
- Non-existent infrastructure: Kubernetes manifests, Prometheus, Grafana, monitoring
- Fictional API features: rate limiting, CORS configuration, authentication
- Future epics and unreleased features from changelog
- Python client usage examples (server is MCP-only)

### Fixed
- plan_feature response structure to match actual implementation
- MCP client configuration examples
- Docker Compose deployment instructions
- All documentation inconsistencies with codebase

## [2.1.0] - 2025-10-06

### Documentation Updates
- Updated all documentation to reflect current playbook names and IDs
- Fixed references from `enhanced_deep_wiki` to `comprehensive_wiki`
- Added complete documentation for `epic_story_review` playbook
- Updated API reference with correct playbook examples and response formats
- Improved playbooks guide with accurate template structures and usage examples
- Added folder structure documentation for comprehensive wiki playbook
- Updated code review integration documentation with displayFindings tool usage
- Corrected playbook counts (6 total playbooks) throughout documentation
- Standardized playbook categories and descriptions

### Changed
- Standardized playbook naming conventions across all documentation files
- Updated usage examples to match current server implementation
- Improved clarity in playbook descriptions and usage instructions
- Enhanced quick start guide with correct playbook IDs
- Updated roadmap to reflect current development priorities

### Fixed
- Inconsistent playbook references between code and documentation
- Missing documentation for epic_story_review playbook
- Incorrect API response examples in documentation
- Outdated playbook IDs in code examples

## [2.0.0] - 2025-10-04

### Added
- **Comprehensive Wiki Documentation**: Multi-layered documentation with 12 contextual sections
- **Atlassian Integration**: Instructions for Jira and Confluence integration
- **Epic & Story Review Checklist**: Review template for product management
- **Documentation Templates**: Structured templates for project documentation
- **Configuration Management**: Environment-based configuration with Pydantic
- **Docker Support**: Dockerfile and docker-compose.yml for containerization

### Changed
- **Playbook Structure**: Enhanced template structure with comprehensive sections
- **Configuration System**: Pydantic-based configuration management
- **Documentation Structure**: Organized documentation for better navigation



## [1.1.0] - 2025-09-29

### Changed
- Documentation improvements and fixes

## [1.0.0] - 2025-09-27

### Added
- Initial MCP Server Framework with FastMCP
- Core Playbooks: Epic Writing, User Story Writing, Documentation
- MCP Tools: list_playbooks, get_playbook, plan_feature
- Basic configuration with Pydantic
- Docker support

## Development Milestones

### Epic N8N-7: MCP Playbook Server Foundation
**Status**: ✅ Complete  
**Duration**: September 2025 - October 2025

**Objectives**:
- Establish MCP server framework
- Implement core playbook functionality
- Create comprehensive documentation
- Enable production deployment

**Deliverables**:
- [x] Basic MCP server framework
- [x] Health check endpoints
- [x] Configuration management
- [x] Docker containerization
- [x] Comprehensive playbook system (6 playbooks)
- [x] Product management playbooks with Atlassian integration
- [x] Documentation templates including comprehensive wiki
- [x] Code review and feature planning tools
- [x] Comprehensive documentation suite
- [x] Production deployment guides

### Future Epics



## Version History Summary

| Version | Release Date | Key Features | Status |
|---------|--------------|--------------|--------|
| 2.1.1 | 2025-10-07 | Documentation sanitization, removed fictional features | ✅ Current |
| 2.1.0 | 2025-10-06 | Documentation fixes, improved clarity | ✅ Stable |
| 2.0.0 | 2025-10-04 | Playbook templates, Atlassian integration | ✅ Stable |
| 1.1.0 | 2025-09-29 | Documentation updates | ✅ Stable |
| 1.0.0 | 2025-09-27 | Initial MCP server, core playbooks | ✅ Stable |



## Acknowledgments

- **Model Context Protocol**: Foundation protocol for AI assistant integration
- **FastMCP Framework**: Core framework for MCP server implementation

---

*For the most current information, check the latest version in the repository.*