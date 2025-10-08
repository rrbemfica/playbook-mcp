from fastmcp import FastMCP
from typing import Dict, Any
from pydantic import Field
from .config import settings

mcp = FastMCP(settings.server_name)

mcp.server_info = {
    "name": settings.server_name,
    "version": "2.1.2",
    "description": "MCP Playbook Server for curated prompts and templates"
}

# Playbook registry
PLAYBOOKS = {
    "product_owner_epic": {
        "name": "Product Owner Epic Writing",
        "description": "Guide for writing comprehensive product epics with Atlassian integration",
        "category": "Product Management",
        "template": {
            "title": "Epic: [Feature Name]",
            "sections": [
                {
                    "name": "Epic Summary",
                    "content": "Brief description of the epic and its business value"
                },
                {
                    "name": "Business Objectives",
                    "content": "- Primary business goal\n- Success metrics\n- Expected ROI"
                },
                {
                    "name": "User Personas",
                    "content": "- Primary users\n- Secondary users\n- User needs and pain points"
                },
                {
                    "name": "Acceptance Criteria",
                    "content": "- Epic-level acceptance criteria\n- Definition of done\n- Quality gates"
                },
                {
                    "name": "Dependencies",
                    "content": "- Technical dependencies\n- Business dependencies\n- External dependencies"
                },
                {
                    "name": "Risks & Assumptions",
                    "content": "- Key risks\n- Mitigation strategies\n- Assumptions made"
                }
            ],
            "atlassian_integration": {
                "instructions": [
                    "IMPORTANT: Use Atlassian official MCP tools to create or edit epics in Jira",
                    "Always start by asking key questions to gather essential information:\n- What is the primary business goal of this epic?\n- Who are the target users/personas?\n- What are the expected outcomes and success metrics?\n- What are the known dependencies and risks?\n- What is the expected timeline and priority?\nOnly proceed with epic suggestions once sufficient context is gathered",
                    "Before executing any Atlassian commands, ALWAYS confirm with the user first",
                    "If user information is vague or incomplete, ask for clarification before proceeding",
                    "Required information: Project key, Epic title, Description, Priority (if not provided, ask user)",
                    "Use createJiraIssue tool with issueTypeName='Epic' for new epics",
                    "Use editJiraIssue tool for updating existing epics",
                    "Always validate project access using getVisibleJiraProjects before creation"
                ],
                "validation_checklist": [
                    "Project key is valid and accessible",
                    "Epic title is clear and descriptive",
                    "Business value is well-defined",
                    "User has confirmed the epic creation/edit",
                    "All required fields are populated"
                ]
            }
        }
    },
    "product_owner_story": {
        "name": "Product Owner User Story Writing",
        "description": "Template for writing effective user stories with Atlassian integration",
        "category": "Product Management",
        "template": {
            "title": "Story: [Story Title]",
            "sections": [
                {
                    "name": "User Story",
                    "content": "As a [user type], I want [functionality] so that [benefit]"
                },
                {
                    "name": "Acceptance Criteria",
                    "content": "Given [context]\nWhen [action]\nThen [outcome]\n\nScenario 1:\n- [ ] Criterion 1\n- [ ] Criterion 2\n\nScenario 2:\n- [ ] Criterion 3"
                },
                {
                    "name": "Definition of Done",
                    "content": "- [ ] Code complete\n- [ ] Unit tests pass\n- [ ] Integration tests pass\n- [ ] Code reviewed\n- [ ] Documentation updated\n- [ ] Deployed to staging"
                },
                {
                    "name": "Business Value",
                    "content": "- Impact on user experience\n- Business metrics affected\n- Priority justification"
                },
                {
                    "name": "Technical Notes",
                    "content": "- Implementation approach\n- Technical constraints\n- API changes needed"
                }
            ],
            "atlassian_integration": {
                "instructions": [
                    "IMPORTANT: Use Atlassian official MCP tools to create or edit user stories in Jira",
                    "Always start by asking key questions to gather essential information to structure the story effectively:\n- Who is the target user/persona for this story?\n- What specific functionality does the user need?\n- What is the expected benefit or outcome for the user?\n- Are there any technical constraints or dependencies?\n- What is the priority and timeline for this story?\nOnly proceed with story suggestions once sufficient context is gathered",
                    "Before executing any Atlassian commands, ALWAYS confirm with the user first",
                    "If user information is vague or incomplete, ask for clarification before proceeding",
                    "Required information: Project key, Story title, User story description, Priority (if not provided, ask user)",
                    "Use createJiraIssue tool with issueTypeName='Story' for new stories",
                    "Use editJiraIssue tool for updating existing stories",
                    "Always validate project access using getVisibleJiraProjects before creation",
                    "Consider linking stories to parent epics using the 'parent' field if applicable"
                ],
                "validation_checklist": [
                    "Project key is valid and accessible",
                    "Story follows proper user story format (As a... I want... So that...)",
                    "Acceptance criteria are clear and testable",
                    "User has confirmed the story creation/edit",
                    "All required fields are populated",
                    "Parent epic is specified if this is part of an epic"
                ]
            }
        }
    },
    "documentation": {
        "name": "Documentation Template",
        "description": "Comprehensive documentation template",
        "category": "Documentation",
        "template": {
            "title": "[Topic Name] - Documentation",
            "critical_instructions": [
                "CRITICAL: Document ONLY what exists in the codebase",
                "Read and analyze actual code files before writing documentation",
                "Do NOT invent features, components, or capabilities that are not implemented",
                "Use exact file names, function names, and class names from the code",
                "If a section doesn't apply because the feature doesn't exist, skip it or mark as 'Not Implemented'",
                "Verify all code examples by checking they exist in the actual codebase",
                "When in doubt, read the code first, then document what you see"
            ],
            "sections": [
                {
                    "name": "Overview",
                    "content": "## Purpose\n[What this component/feature actually does - based on code analysis]\n\n## Audience\n[Who should read this - based on actual use cases]\n\n## Prerequisites\n[Actual requirements from requirements.txt, pyproject.toml, or package.json]"
                },
                {
                    "name": "Quick Start",
                    "content": "### Getting Started\n\n[List actual setup steps from README or installation scripts]\n\n### Basic Example\n```\n[Real code example from the codebase or tests]\n```"
                },
                {
                    "name": "Detailed Guide",
                    "content": "### Core Concepts\n[Document actual concepts implemented in the code]\n\n### Configuration\n[Document actual config files and their real options]\n| Option | Description | Default |\n|--------|-------------|---------|\n| [actual_param] | [from code] | [actual default] |"
                },
                {
                    "name": "Troubleshooting",
                    "content": "### Common Issues\n\n[Document only known issues from code, error handling, or issue tracker]\n\n**Issue: [Actual problem]**\n- Cause: [From code analysis]\n- Solution: [Actual solution]"
                }
            ]
        }
    },
    "comprehensive_wiki": {
        "name": "Comprehensive Wiki Documentation",
        "description": "Multi-layered documentation with contextual sections for deep knowledge capture",
        "category": "Documentation",
        "template": {
            "title": "[Project/Topic Name] - Comprehensive Wiki",
            "critical_instructions": [
                "CRITICAL: Document ONLY what exists in the codebase",
                "Read and analyze actual code files before writing documentation",
                "Do NOT invent features, components, or capabilities that are not implemented",
                "Use exact file names, function names, and class names from the code",
                "If a section doesn't apply because the feature doesn't exist, skip it or mark as 'Not Implemented'",
                "Verify all code examples by checking they exist in the actual codebase",
                "When in doubt, read the code first, then document what you see"
            ],
            "sections": [
                {
                    "name": "Executive Summary",
                    "content": "## What is this?\n[One-sentence description based on actual project purpose]\n\n## Why does it matter?\n[Actual business/technical value - from README or project docs]\n\n## Key outcomes\n[List only implemented features/capabilities]"
                },
                {
                    "name": "Context & Background",
                    "content": "## Problem Statement\n[Actual problem from project documentation or code comments]\n\n## Current State\n[Describe actual implementation based on code analysis]\n\n## Stakeholders\n[Only list if documented in project files]"
                },
                {
                    "name": "Architecture Overview",
                    "content": "## System Design\n[Describe actual architecture from code structure]\n\n## Components\n[List only components that exist in the codebase]\n| Component | Purpose | Dependencies |\n|-----------|---------|--------------|\n| [Actual file/module] | [What it does] | [Actual dependencies from imports] |\n\n## Data Flow\n[Trace actual data flow through the code]"
                },
                {
                    "name": "Implementation Guide",
                    "content": "## Prerequisites\n[Actual requirements from requirements.txt, pyproject.toml, or package.json]\n\n## Setup Instructions\n```bash\n[Actual installation commands from README or setup scripts]\n```\n\n## Configuration\n[Document actual config files and their real options]\n```\n[Real configuration example from .env.example or config files]\n```\n\n## Verification\n```bash\n[Actual test/verification commands that exist]\n```"
                },
                {
                    "name": "Usage Patterns",
                    "content": "## Common Use Cases\n\n[Document only use cases supported by actual code]\n\n### [Actual Use Case from code/tests]\n**When**: [Real conditions]\n**How**: [Actual steps]\n**Example**:\n```\n[Real code example from the codebase or tests]\n```"
                },
                {
                    "name": "API Reference",
                    "content": "## API/Functions\n\n[ONLY document APIs/functions that exist in the code]\n[Read the actual source files to get function signatures]\n\n### [Actual function/endpoint name]\n**Purpose**: [What it actually does - from code]\n**Parameters**: [Real parameters from function signature]\n**Returns**: [Actual return type/structure]\n**Example**:\n```\n[Real usage example from code or tests]\n```"
                },
                {
                    "name": "Advanced Topics",
                    "content": "## Performance Optimization\n[Only document if performance features exist in code]\n\n## Security Considerations\n[Document only implemented security features]\n- **Authentication**: [If implemented, describe actual mechanism]\n- **Authorization**: [If implemented, describe actual implementation]\n\n## Scaling Strategies\n[Only document if scaling features are implemented]"
                },
                {
                    "name": "Troubleshooting & Diagnostics",
                    "content": "## Common Issues\n\n[Document only known issues from code, error handling, or issue tracker]\n\n### Issue: [Actual problem]\n**Symptoms**: [Real symptoms]\n**Cause**: [From code analysis]\n**Solution**: [Actual solution]\n\n## Debugging Tools\n[Only list tools/features that actually exist]\n- **Logs**: [Actual log location if logging is implemented]\n- **Health Check**: [Actual endpoint/command if it exists]"
                },
                {
                    "name": "Integration & Dependencies",
                    "content": "## External Systems\n[Only list if external integrations exist in code]\n\n## Dependencies\n[List actual dependencies from package files]\n- [Actual package]: [Why it's used - from code analysis]\n\n## Consumers\n[Only document if there are known consumers]"
                },
                {
                    "name": "Operations & Maintenance",
                    "content": "## Deployment Process\n[Document actual deployment process from CI/CD files or deployment scripts]\n\n## Monitoring & Alerts\n[Only document if monitoring is implemented]\n\n## Backup & Recovery\n[Only document if backup mechanisms exist]"
                },
                {
                    "name": "Knowledge Base",
                    "content": "## Decision Log\n[Document decisions from commit history, PR discussions, or ADR files if they exist]\n\n## Related Documentation\n[Link only to documentation that actually exists in the project]"
                },
                {
                    "name": "Appendices",
                    "content": "## Glossary\n[Define only terms actually used in the codebase]\n\n## Change History\n[Use actual version history from git tags or CHANGELOG if it exists]\n\n## Contact Information\n[Only include if documented in README or project files]"
                }
            ],
            "folder_structure": {
                "recommended_layout": "docs/\n├── README.md (Executive Summary)\n├── overview/\n│   ├── context.md (Context & Background)\n│   └── architecture.md (Architecture Overview)\n├── guides/\n│   ├── implementation.md (Implementation Guide)\n│   ├── usage-patterns.md (Usage Patterns)\n│   └── api-reference.md (API Reference)\n├── advanced/\n│   ├── performance.md (Advanced Topics)\n│   └── troubleshooting.md (Troubleshooting & Diagnostics)\n├── operations/\n│   ├── integrations.md (Integration & Dependencies)\n│   └── maintenance.md (Operations & Maintenance)\n└── meta/\n    ├── knowledge-base.md (Knowledge Base)\n    └── appendices.md (Appendices)",
                "instructions": [
                    "Create a 'docs' folder in your project root",
                    "Use README.md as the main entry point (Executive Summary)",
                    "Organize sections into logical folders by audience and purpose",
                    "Link between documents using relative paths",
                    "Keep file names lowercase with hyphens for consistency"
                ],
                "file_naming": {
                    "pattern": "kebab-case.md",
                    "examples": [
                        "implementation-guide.md",
                        "api-reference.md",
                        "troubleshooting.md"
                    ]
                }
            }
        }
    },
    "code_review": {
        "name": "Code Review",
        "description": "Senior code reviewer ensuring high standards of code quality and security",
        "category": "Development",
        "template": {
            "instructions": [
                "You are a senior code reviewer ensuring high standards of code quality and security.",
                "When invoked:",
                "1. Run git diff to see recent changes",
                "2. Focus on modified files",
                "3. Begin review immediately"
            ],
            "checklist": [
                "Code is simple and readable",
                "Functions and variables are well-named",
                "No duplicated code",
                "Proper error handling",
                "No exposed secrets or API keys",
                "Input validation implemented",
                "Good test coverage",
                "Performance considerations addressed"
            ],
            "feedback_structure": {
                "critical": "Critical issues (must fix)",
                "warnings": "Warnings (should fix)",
                "suggestions": "Suggestions (consider improving)"
            },
            "guidelines": [
                "Provide feedback organized by priority",
                "Include specific examples of how to fix issues"
            ],
            "code_issues_integration": {
                "instructions": [
                    "IMPORTANT: Use displayFindings tool to populate the Code Issues panel with review findings",
                    "Each finding must include: filePath (absolute), startLine, endLine, title, severity, description, language",
                    "Map priority to severity: Critical issues -> 'Critical', Warnings -> 'Medium', Suggestions -> 'Low'",
                    "Include specific line numbers where issues occur",
                    "Optionally provide suggestedFixes array with code examples",
                    "Run displayFindings once with all findings after completing the review"
                ]
            }
        }
    },
    "epic_story_review": {
        "name": "Epic & Story Review Checklist",
        "description": "Comprehensive review template for epic and story summaries and descriptions",
        "category": "Product Management",
        "template": {
            "title": "Review: [Epic/Story Title]",
            "sections": [
                {
                    "name": "Summary Quality Check",
                    "content": "## Epic Summary Review\n- [ ] Clear and concise description of the epic\n- [ ] Business value is explicitly stated\n- [ ] Target users/personas are identified\n- [ ] Success criteria are defined\n\n## Story Summary Review\n- [ ] Follows proper user story format (As a... I want... So that...)\n- [ ] User type is specific and clear\n- [ ] Functionality is well-defined\n- [ ] Benefit/value is articulated"
                },
                {
                    "name": "Description Completeness",
                    "content": "## Epic Description\n- [ ] Business objectives are clear\n- [ ] User personas and needs are defined\n- [ ] Dependencies are identified\n- [ ] Risks and assumptions are documented\n- [ ] Acceptance criteria at epic level\n\n## Story Description\n- [ ] Acceptance criteria are testable\n- [ ] Definition of done is complete\n- [ ] Technical constraints are noted\n- [ ] Business value is quantified"
                },
                {
                    "name": "Clarity & Communication",
                    "content": "## Language & Tone\n- [ ] Uses clear, jargon-free language\n- [ ] Consistent terminology throughout\n- [ ] Appropriate level of detail for audience\n- [ ] Action-oriented and specific\n\n## Stakeholder Alignment\n- [ ] Requirements align with business goals\n- [ ] Technical feasibility is considered\n- [ ] User experience impact is clear\n- [ ] Cross-team dependencies are noted"
                },
                {
                    "name": "Acceptance Criteria Review",
                    "content": "## Epic-Level Criteria\n- [ ] High-level outcomes are measurable\n- [ ] Success metrics are defined\n- [ ] Quality gates are established\n- [ ] Completion criteria are clear\n\n## Story-Level Criteria\n- [ ] Follows Given-When-Then format\n- [ ] Scenarios cover happy path\n- [ ] Edge cases are considered\n- [ ] Criteria are testable and specific"
                },
                {
                    "name": "Technical Considerations",
                    "content": "## Implementation Readiness\n- [ ] Technical approach is outlined\n- [ ] API changes are documented\n- [ ] Performance requirements are noted\n- [ ] Security considerations are addressed\n\n## Dependencies & Integration\n- [ ] System dependencies are mapped\n- [ ] Third-party integrations are identified\n- [ ] Data requirements are specified\n- [ ] Infrastructure needs are considered"
                },
                {
                    "name": "Review Recommendations",
                    "content": "## Improvement Areas\n### High Priority\n- [Issue 1]: [Specific recommendation]\n- [Issue 2]: [Specific recommendation]\n\n### Medium Priority\n- [Issue 3]: [Specific recommendation]\n- [Issue 4]: [Specific recommendation]\n\n### Low Priority\n- [Issue 5]: [Specific recommendation]\n\n## Overall Assessment\n- **Readiness Score**: [1-10]\n- **Recommendation**: [Approve/Revise/Reject]\n- **Next Steps**: [Specific actions needed]"
                }
            ],
            "atlassian_integration": {
                "instructions": [
                    "IMPORTANT: Use Atlassian official MCP tools to access and review epics/stories in Jira",
                    "Before making any changes, ALWAYS confirm with the user first",
                    "Use getJiraIssue tool to retrieve current epic/story details",
                    "Use editJiraIssue tool to update based on review recommendations",
                    "Add review comments using addCommentToJiraIssue tool",
                    "Always validate project access using getVisibleJiraProjects before accessing issues"
                ],
                "validation_checklist": [
                    "Issue key/ID is valid and accessible",
                    "Review covers all template sections",
                    "Recommendations are specific and actionable",
                    "User has confirmed any proposed changes",
                    "Review comments are added to the issue"
                ]
            }
        }
    }
}

@mcp.tool()
def plan_feature(
    feature_description: str = Field(description="Description of the feature to implement"),
    project_type: str = Field(default="web", description="Type of project (web, api, mobile, etc.)"),
    complexity: str = Field(default="medium", description="Complexity level (simple, medium, complex)")
) -> Dict[str, Any]:
    """Generate a structured implementation plan with phases, tasks, and next actions for any feature. Returns a breakdown covering requirements, design, development, testing, and deployment."""
    return {
        "feature": feature_description,
        "project_type": project_type,
        "complexity": complexity,
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

@mcp.tool()
def list_playbooks() -> Dict[str, Any]:
    """Retrieve all available playbooks with metadata. Returns playbook IDs, names, descriptions, and categories. Use this to discover which playbooks are available before retrieving specific ones."""
    playbook_list = []
    for key, playbook in PLAYBOOKS.items():
        playbook_list.append({
            "id": key,
            "name": playbook["name"],
            "description": playbook["description"],
            "category": playbook["category"]
        })
    
    return {
        "total_playbooks": len(playbook_list),
        "playbooks": playbook_list,
        "categories": list(set(p["category"] for p in PLAYBOOKS.values()))
    }

@mcp.tool()
def get_playbook(
    playbook_id: str = Field(description="ID of the playbook to retrieve (e.g., 'product_owner_epic', 'comprehensive_wiki', 'code_review')")
) -> Dict[str, Any]:
    """Retrieve complete playbook details including templates, instructions, and integration guidelines. Use this after identifying the needed playbook from list_playbooks. Returns structured content with sections, checklists, and usage instructions."""
    if playbook_id not in PLAYBOOKS:
        return {
            "error": f"Playbook '{playbook_id}' not found",
            "available_playbooks": list(PLAYBOOKS.keys())
        }
    
    playbook = PLAYBOOKS[playbook_id]
    result = {
        "id": playbook_id,
        "name": playbook["name"],
        "description": playbook["description"],
        "category": playbook["category"],
        "template": playbook["template"]
    }
    
    if playbook_id == "comprehensive_wiki":
        result["usage_instructions"] = [
            "Create the recommended folder structure in your project",
            "Start with README.md (Executive Summary) as your main entry point",
            "Create separate markdown files for each section in appropriate folders",
            "Use relative links to connect documents (e.g., [Architecture](overview/architecture.md))",
            "Fill in the placeholders with your specific content",
            "Customize sections as needed for your use case"
        ]
        result["folder_structure"] = playbook["template"].get("folder_structure", {})
    elif playbook_id == "epic_story_review":
        result["usage_instructions"] = [
            "Use this template to systematically review epics and stories",
            "Work through each section as a checklist",
            "Document specific issues and recommendations",
            "Provide actionable feedback with priority levels",
            "Use Atlassian tools to access and update issues as needed",
            "Add review comments directly to Jira issues"
        ]
    else:
        result["usage_instructions"] = [
            "Copy the template sections",
            "Fill in the placeholders with your specific content",
            "Customize sections as needed for your use case",
            "Remove sections that don't apply"
        ]
    
    return result

@mcp.prompt()
def playbook_guide() -> str:
    """Comprehensive guide for using playbook tools to write epics, stories, documentation, and code reviews."""
    return """You are an AI assistant integrated with the Playbook MCP Server. Your primary directive is to manage and apply playbooks effectively based on user requests.

## Core Workflow

### 1. Initialization
On any playbook request, execute list_playbooks() to load available playbooks.

### 2. Intent-Driven Retrieval
- Interpret user intent (e.g., "writing an epic")
- Call get_playbook(playbook_id) to retrieve the appropriate playbook
- Use playbook information as context to drive task decisions

### 3. Execution with Transparency
- Articulate your decision-making process
- Explain which playbook you're using and why
- Ask clarifying questions before proceeding
- Always confirm with user before making changes

## Available Playbooks
- **product_owner_epic**: Write comprehensive epics with business value and acceptance criteria
- **product_owner_story**: Write user stories in 'As a... I want... So that...' format
- **epic_story_review**: Review epics/stories for quality and completeness
- **comprehensive_wiki**: Create multi-layered project documentation
- **documentation**: Document features with overview, usage, and troubleshooting
- **code_review**: Review code for quality, security, and best practices
- **plan_feature**: Generate implementation plans (use plan_feature tool directly)

## Constraints
- Display only essential information to maintain UI clarity
- Provide minimal, high-level details when listing playbooks
- Don't list all playbooks unless necessary

## Integration Guidelines
- **Jira**: Use Atlassian MCP tools (getJiraIssue, createJiraIssue, editJiraIssue, addCommentToJiraIssue)
- **Documentation**: For official docs, prioritize 'ref tools' or 'context7' MCPs, fallback to 'fetch' if needed
- **Code Issues**: Use displayFindings tool for code review results"""

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=settings.port)