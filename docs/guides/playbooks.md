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

#### Documentation Template
**ID**: `documentation`  
**Category**: Documentation

Standard comprehensive documentation template for general use.

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

#### Comprehensive Wiki Documentation
**ID**: `comprehensive_wiki`  
**Category**: Documentation

Multi-layered documentation template with 12 contextual sections for deep knowledge capture.

**Template Structure:**

1. **Executive Summary**: What, why, and key outcomes
2. **Context & Background**: Problem statement, current state, stakeholders
3. **Architecture Overview**: System design, components, data flow
4. **Implementation Guide**: Prerequisites, setup, configuration, verification
5. **Usage Patterns**: Common use cases with examples
6. **API Reference**: Endpoints, parameters, responses
7. **Advanced Topics**: Performance, security, scaling strategies
8. **Troubleshooting & Diagnostics**: Common issues, debugging tools, emergency procedures
9. **Integration & Dependencies**: External systems, upstream/downstream dependencies
10. **Operations & Maintenance**: Deployment, monitoring, backup & recovery
11. **Knowledge Base**: Decision log, lessons learned, related documentation
12. **Appendices**: Glossary, change history, contact information

**Folder Structure:**
```
docs/
├── README.md (Executive Summary)
├── overview/
│   ├── context.md
│   └── architecture.md
├── guides/
│   ├── implementation.md
│   ├── usage-patterns.md
│   └── api-reference.md
├── advanced/
│   ├── performance.md
│   └── troubleshooting.md
├── operations/
│   ├── integrations.md
│   └── maintenance.md
└── meta/
    ├── knowledge-base.md
    └── appendices.md
```

**Usage Workflow:**
1. Create the recommended folder structure in your project
2. Start with README.md (Executive Summary) as your main entry point
3. Create separate markdown files for each section in appropriate folders
4. Use relative links to connect documents
5. Fill in the placeholders with your specific content
6. Customize sections as needed for your use case

**Best Practices:**
- Use README.md as the main entry point
- Organize sections into logical folders by audience and purpose
- Link between documents using relative paths
- Keep file names lowercase with hyphens (kebab-case.md)
- Maintain consistency across all documentation files

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
# Get comprehensive wiki playbook
playbook = client.call_tool("get_playbook", {
    "playbook_id": "comprehensive_wiki"
})

# Access folder structure recommendations
folder_structure = playbook["folder_structure"]
print(f"Recommended layout: {folder_structure['recommended_layout']}")

# Get usage instructions
instructions = playbook["usage_instructions"]
for instruction in instructions:
    print(f"- {instruction}")
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

### Epic & Story Review

#### Epic & Story Review Checklist
**ID**: `epic_story_review`  
**Category**: Product Management

Comprehensive review template for epic and story summaries and descriptions.

**Template Structure:**
- **Summary Quality Check**: Epic and story summary validation
- **Description Completeness**: Business objectives, acceptance criteria, technical details
- **Clarity & Communication**: Language, tone, stakeholder alignment
- **Acceptance Criteria Review**: Epic-level and story-level criteria validation
- **Technical Considerations**: Implementation readiness, dependencies, integration
- **Review Recommendations**: Improvement areas with priority levels

**Atlassian Integration Features:**
- Use getJiraIssue tool to retrieve current epic/story details
- Use editJiraIssue tool to update based on review recommendations
- Add review comments using addCommentToJiraIssue tool
- Always validate project access before accessing issues

**Usage Example:**
```python
# Get review playbook
playbook = client.call_tool("get_playbook", {
    "playbook_id": "epic_story_review"
})

# Retrieve Jira issue for review
issue = get_jira_issue(cloud_id, issue_key)

# Apply review checklist
review_results = apply_review_checklist(playbook["template"], issue)

# Add review comments to Jira
add_comment_to_jira_issue(
    cloud_id=cloud_id,
    issue_key=issue_key,
    comment_body=format_review_results(review_results)
)
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

### Code Review Integration

1. **Code Issues Panel**
   - Use displayFindings tool to populate the Code Issues panel
   - Each finding must include: filePath, startLine, endLine, title, severity, description, language
   - Map priority to severity: Critical → 'Critical', Warnings → 'Medium', Suggestions → 'Low'

2. **Review Process**
   - Run git diff to see recent changes
   - Focus on modified files
   - Provide feedback organized by priority
   - Include specific examples of how to fix issues

3. **Quality Checklist**
   - Code is simple and readable
   - Functions and variables are well-named
   - No duplicated code
   - Proper error handling
   - No exposed secrets or API keys
   - Input validation implemented
   - Good test coverage
   - Performance considerations addressed

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