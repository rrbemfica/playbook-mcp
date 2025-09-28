# Playbooks Guide

Comprehensive guide to using and customizing playbooks in the MCP Playbook Server.

## Overview

Playbooks are structured templates that provide consistent approaches to common development tasks. The server includes both traditional templates and AI-powered playbooks inspired by DeepWiki's repository analysis capabilities.

## Available Playbooks

### Product Management

#### Product Owner Epic Writing
**ID**: `product_owner_epic`  
**Category**: Product Management

Comprehensive template for writing product epics with Atlassian integration.

**Template Structure:**
- Epic Summary with business context
- Business Objectives and success metrics
- User Personas and target audience
- Acceptance Criteria at epic level
- Dependencies and integration points
- Risks, Assumptions, and mitigation strategies

**Atlassian Integration Features:**
- Automatic Jira epic creation
- Project validation and permissions check
- Required field validation
- User confirmation workflow
- Epic linking to existing projects

**Usage Example:**
```json
{
  "playbook_id": "product_owner_epic",
  "context": {
    "project_key": "AUTH",
    "epic_title": "User Authentication System",
    "business_value": "Secure user access and data protection",
    "target_users": "All application users",
    "success_metrics": "100% secure login, <2s response time"
  }
}
```

#### Product Owner User Story Writing
**ID**: `product_owner_story`  
**Category**: Product Management

Template for writing effective user stories with proper acceptance criteria.

**Template Structure:**
- User Story format (As a... I want... So that...)
- Acceptance Criteria (Given/When/Then format)
- Definition of Done checklist
- Business Value quantification
- Technical Notes and constraints

**Best Practices:**
- Use specific user personas
- Include measurable acceptance criteria
- Define clear business value
- Consider edge cases and error scenarios

**Usage Example:**
```json
{
  "playbook_id": "product_owner_story",
  "context": {
    "user_type": "registered user",
    "functionality": "reset password",
    "benefit": "regain access to account without support",
    "acceptance_criteria": [
      "Given user forgot password, when they click reset, then email is sent",
      "Given valid reset token, when new password entered, then account is updated"
    ]
  }
}
```

### Documentation

#### Deep Wiki Documentation
**ID**: `deep_wiki_documentation`  
**Category**: Documentation

Traditional comprehensive wiki-style documentation template.

**Template Structure:**
1. **Overview**: Purpose, audience, prerequisites
2. **Table of Contents**: Organized navigation
3. **Quick Start**: 5-minute setup guide
4. **Detailed Guide**: Core concepts and step-by-step instructions
5. **Advanced Topics**: Performance, integration, best practices
6. **Troubleshooting**: Common issues and debugging
7. **References**: Related docs, external resources, changelog

**Usage Workflow:**
1. Copy template sections to your documentation
2. Fill in placeholders with project-specific content
3. Customize sections for your use case
4. Remove irrelevant sections
5. Maintain and update regularly

**Best Practices:**
- Start with Quick Start for immediate value
- Use code examples liberally
- Include troubleshooting for common issues
- Maintain a comprehensive changelog
- Link to related documentation

#### Enhanced Deep Wiki Documentation (AI-Powered)
**ID**: `enhanced_deep_wiki`  
**Category**: Documentation

AI-powered comprehensive documentation with repository analysis and automated content generation.

**AI-Powered Sections:**

1. **Auto-Generated Overview**
   - Purpose analysis from codebase structure
   - Target audience identification from README and docs
   - Prerequisites extraction from requirements and setup files

2. **Intelligent Quick Start**
   - Setup steps derived from configuration files
   - Essential commands extracted from scripts and Makefiles
   - Basic examples generated from code patterns

3. **Context-Aware Detailed Guide**
   - Core concepts identified from architecture patterns
   - System design documentation from code structure
   - Configuration tables auto-generated from environment files

4. **Advanced Integration Patterns**
   - Performance optimization tips from code analysis
   - Integration patterns identified from dependencies
   - Best practices derived from code quality metrics

5. **Intelligent Troubleshooting**
   - Common issues extracted from error handling code
   - Debugging steps generated from logging patterns
   - FAQ compiled from issue tracking and support patterns

6. **Smart References**
   - Related documentation links from project structure
   - External dependencies analysis and documentation
   - Automated changelog generation from commit history

**DeepWiki Inspiration:**
- **Source**: Cognition Labs DeepWiki MCP Server
- **Key Concepts**: AI-powered context gathering, repository-aware documentation
- **Enhancements**: Structured template framework, hybrid manual/AI approach

**Usage Workflow:**
1. **Repository Analysis**: Analyze target repository structure and patterns
2. **Content Generation**: Generate AI-powered content for each section
3. **Template Population**: Populate template with generated content
4. **Quality Assurance**: Review and refine generated documentation
5. **Publication**: Deploy documentation with update mechanisms

**AI Features:**
- Repository structure analysis
- Code pattern recognition
- Dependency mapping and documentation
- Automated content generation
- Dynamic updates based on code changes

## Playbook Usage Patterns

### Basic Usage

```python
from mcp_client import MCPClient

# Initialize client
client = MCPClient("http://localhost:8080")

# List available playbooks
playbooks = client.call_tool("list_playbooks", {})
print(f"Available playbooks: {len(playbooks['playbooks'])}")

# Get specific playbook
playbook = client.call_tool("get_playbook", {
    "playbook_id": "enhanced_deep_wiki"
})

# Use playbook template
template = playbook["template"]
sections = template["sections"]
```

### Advanced Integration

```python
# Analyze documentation approach
analysis = client.call_tool("analyze_documentation_approach", {
    "current_approach": "manual",
    "target_project_type": "web",
    "repository_url": "https://github.com/user/repo"
})

# Get recommendation
recommended_playbook = analysis["recommended_playbook"]
effort_reduction = analysis["effort_reduction"]

# Use recommended playbook
playbook = client.call_tool("get_playbook", {
    "playbook_id": recommended_playbook
})
```

### Atlassian Integration

```python
# Epic creation with playbook
def create_epic_with_playbook(project_key, epic_data):
    # Get epic playbook
    playbook = client.call_tool("get_playbook", {
        "playbook_id": "product_owner_epic"
    })
    
    # Validate project access
    projects = get_visible_jira_projects(project_key)
    if not projects:
        raise ValueError(f"No access to project {project_key}")
    
    # Format epic description using template
    description = format_epic_description(playbook["template"], epic_data)
    
    # Create epic in Jira
    epic = create_jira_issue(
        project_key=project_key,
        issue_type="Epic",
        summary=epic_data["title"],
        description=description
    )
    
    return epic
```

## Customization Guide

### Creating Custom Playbooks

1. **Define Structure**
```python
custom_playbook = {
    "name": "API Documentation Generator",
    "description": "Generate API documentation from OpenAPI specs",
    "category": "Documentation",
    "template": {
        "title": "[API Name] Documentation",
        "sections": [
            {
                "name": "API Overview",
                "content": "## Overview\n[Generated from OpenAPI specification]"
            },
            {
                "name": "Endpoints",
                "content": "## Endpoints\n[Auto-generated endpoint documentation]"
            },
            {
                "name": "Authentication",
                "content": "## Authentication\n[Security scheme documentation]"
            }
        ]
    },
    "metadata": {
        "version": "1.0",
        "author": "Development Team",
        "tags": ["api", "documentation", "openapi"]
    }
}
```

2. **Add Processing Logic**
```python
def process_api_playbook(openapi_spec):
    """Process OpenAPI specification to generate documentation."""
    sections = []
    
    # Generate overview from spec info
    overview = generate_api_overview(openapi_spec.get("info", {}))
    sections.append({"name": "Overview", "content": overview})
    
    # Generate endpoint documentation
    endpoints = generate_endpoint_docs(openapi_spec.get("paths", {}))
    sections.append({"name": "Endpoints", "content": endpoints})
    
    # Generate authentication docs
    auth = generate_auth_docs(openapi_spec.get("components", {}).get("securitySchemes", {}))
    sections.append({"name": "Authentication", "content": auth})
    
    return sections
```

3. **Register Playbook**
```python
# Add to PLAYBOOKS registry
PLAYBOOKS["api_documentation"] = custom_playbook

# Register processing function
PLAYBOOK_PROCESSORS["api_documentation"] = process_api_playbook
```

### AI Enhancement Integration

For AI-powered playbooks:

1. **Repository Analysis**
```python
def analyze_repository(repo_path):
    """Analyze repository structure and patterns."""
    analysis = {
        "structure": analyze_directory_structure(repo_path),
        "dependencies": extract_dependencies(repo_path),
        "patterns": identify_code_patterns(repo_path),
        "documentation": find_existing_docs(repo_path)
    }
    return analysis
```

2. **Content Generation**
```python
def generate_ai_content(template, analysis):
    """Generate content using AI based on repository analysis."""
    content = {}
    
    for section in template["sections"]:
        section_name = section["name"]
        
        # Generate content based on section type and analysis
        if section_name == "Overview":
            content[section_name] = generate_overview(analysis)
        elif section_name == "Quick Start":
            content[section_name] = generate_quick_start(analysis)
        # ... more section types
    
    return content
```

3. **Quality Assurance**
```python
def validate_generated_content(content, analysis):
    """Validate AI-generated content for accuracy and completeness."""
    validation_results = {}
    
    for section, text in content.items():
        validation_results[section] = {
            "accuracy": check_factual_accuracy(text, analysis),
            "completeness": check_completeness(text, section),
            "clarity": check_readability(text)
        }
    
    return validation_results
```

## Best Practices

### Playbook Design

1. **Consistency**
   - Use standard section structures across playbooks
   - Maintain consistent naming conventions
   - Follow established formatting patterns

2. **Clarity**
   - Provide clear instructions and examples
   - Use simple, direct language
   - Include visual aids where helpful

3. **Completeness**
   - Cover all necessary aspects of the task
   - Include edge cases and error scenarios
   - Provide troubleshooting guidance

4. **Maintainability**
   - Design for easy updates and modifications
   - Use modular, reusable components
   - Document customization points

### AI Integration

1. **Human Oversight**
   - Always include review steps for AI-generated content
   - Provide manual override options
   - Implement quality gates

2. **Quality Gates**
   - Validate AI-generated content for accuracy
   - Check for completeness and relevance
   - Ensure consistency with project standards

3. **Fallback Options**
   - Provide manual alternatives when AI fails
   - Include traditional templates as backup
   - Graceful degradation for partial failures

4. **Transparency**
   - Clearly mark AI-generated content
   - Document the AI generation process
   - Provide confidence scores where applicable

### Template Management

1. **Version Control**
   - Track template changes over time
   - Maintain backward compatibility
   - Document breaking changes

2. **Documentation**
   - Document template usage and customization
   - Provide examples and best practices
   - Maintain up-to-date guides

3. **Testing**
   - Validate template outputs regularly
   - Test with various input scenarios
   - Ensure cross-platform compatibility

4. **Feedback Loop**
   - Collect user feedback on template effectiveness
   - Monitor usage patterns and success rates
   - Iterate based on real-world usage

## Integration Examples

### CI/CD Pipeline Integration

```yaml
# GitHub Actions example
name: Generate Documentation
on:
  push:
    branches: [main]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Generate Documentation
      run: |
        curl -X POST http://mcp-server:8080/tools/get_playbook \
          -H "Content-Type: application/json" \
          -d '{"playbook_id": "enhanced_deep_wiki"}' \
          | jq '.template' > docs/template.json
        
        # Process template with repository data
        python scripts/generate_docs.py
```

### IDE Integration

```python
# VS Code extension example
class MCPPlaybookProvider:
    def __init__(self, server_url):
        self.server_url = server_url
    
    def get_playbooks(self):
        """Get available playbooks for IDE integration."""
        response = requests.post(f"{self.server_url}/tools/list_playbooks", json={})
        return response.json()["playbooks"]
    
    def generate_feature_plan(self, description):
        """Generate feature plan from IDE."""
        response = requests.post(
            f"{self.server_url}/tools/plan_feature",
            json={"feature_description": description}
        )
        return response.json()
```

## Troubleshooting

### Common Issues

1. **Playbook Not Found**
   - **Cause**: Invalid playbook ID or typo
   - **Solution**: Use `list_playbooks` to verify available IDs
   - **Prevention**: Implement ID validation in client code

2. **Template Processing Errors**
   - **Cause**: Missing required template variables
   - **Solution**: Check template structure and provide all required data
   - **Prevention**: Validate input data before processing

3. **AI Generation Failures**
   - **Cause**: Repository analysis incomplete or failed
   - **Solution**: Ensure repository is accessible and well-structured
   - **Prevention**: Implement fallback to manual templates

4. **Integration Issues**
   - **Cause**: External service connectivity problems
   - **Solution**: Check network connectivity and service status
   - **Prevention**: Implement retry logic and circuit breakers

### Debugging Steps

1. **Verify Playbook Availability**
```bash
curl -X POST http://localhost:8080/tools/list_playbooks \
  -H "Content-Type: application/json" -d '{}'
```

2. **Check Template Structure**
```bash
curl -X POST http://localhost:8080/tools/get_playbook \
  -H "Content-Type: application/json" \
  -d '{"playbook_id": "your_playbook_id"}'
```

3. **Validate Input Parameters**
```python
# Ensure all required parameters are provided
required_params = ["feature_description"]
for param in required_params:
    if param not in request_data:
        raise ValueError(f"Missing required parameter: {param}")
```

4. **Test Individual Components**
```python
# Test repository analysis separately
analysis = analyze_repository("/path/to/repo")
print(f"Analysis results: {analysis}")

# Test content generation
content = generate_ai_content(template, analysis)
print(f"Generated content: {content}")
```

## Future Enhancements

### Planned Features

1. **Dynamic Playbook Loading**
   - Load playbooks from external repositories
   - Support for community-contributed playbooks
   - Version management and updates

2. **Template Inheritance**
   - Base templates with specialized extensions
   - Composition of multiple playbook components
   - Hierarchical template organization

3. **Multi-language Support**
   - Internationalization of templates
   - Language-specific content generation
   - Cultural adaptation of best practices

4. **Advanced AI Integration**
   - Enhanced repository analysis capabilities
   - Multi-modal content generation (text, diagrams, code)
   - Continuous learning from usage patterns

5. **Collaborative Features**
   - Multi-user playbook development
   - Real-time collaboration on templates
   - Community feedback and ratings

### Community Contributions

- **Playbook Sharing**: Community repository for sharing playbooks
- **Template Marketplace**: Curated collection of high-quality templates
- **Integration Plugins**: Third-party service integrations
- **AI Model Integration**: Support for different AI providers and models