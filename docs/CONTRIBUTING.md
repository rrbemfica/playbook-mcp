# Contributing to MCP Playbook Server

Thank you for your interest in contributing to the MCP Playbook Server! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Development Workflow](#development-workflow)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Guidelines](#documentation-guidelines)
- [Community and Support](#community-and-support)

## Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow. Please read and follow these guidelines to ensure a welcoming environment for everyone.

### Our Standards

- **Be respectful**: Treat all community members with respect and kindness
- **Be inclusive**: Welcome newcomers and help them get started
- **Be collaborative**: Work together constructively and share knowledge
- **Be professional**: Maintain professional communication in all interactions

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Personal attacks or trolling
- Spam or irrelevant content
- Sharing private information without permission

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Docker (optional, for containerized development)
- Basic understanding of MCP (Model Context Protocol)

### First Contribution

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Set up development environment** (see Development Setup)
4. **Find an issue** to work on (look for "good first issue" labels)
5. **Create a branch** for your changes
6. **Make your changes** following our guidelines
7. **Submit a pull request**

## Development Setup

### Local Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/mcp-playbook-server.git
cd mcp-playbook-server

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/mcp-playbook-server.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Copy environment configuration
cp .env.example .env

# Run tests to verify setup
python -m pytest tests/ -v
```

### Development Dependencies

```bash
# Install development tools
pip install -r requirements-dev.txt

# This includes:
# - pytest: Testing framework
# - black: Code formatting
# - isort: Import sorting
# - flake8: Linting
# - mypy: Type checking
# - pre-commit: Git hooks
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

### Docker Development

```bash
# Build development image
docker build -f docker/Dockerfile.dev -t mcp-playbook-server:dev .

# Run with development setup
docker-compose -f docker-compose.dev.yml up
```

## Contributing Guidelines

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes**: Fix issues and improve stability
2. **Feature Development**: Add new features and capabilities
3. **Documentation**: Improve guides, API docs, and examples
4. **Testing**: Add test cases and improve coverage
5. **Performance**: Optimize performance and scalability
6. **Playbooks**: Create new playbook templates
7. **Integrations**: Add new service integrations

### Coding Standards

#### Python Code Style

```python
# Use Black for formatting
black src/ tests/

# Use isort for import sorting
isort src/ tests/

# Follow PEP 8 guidelines
flake8 src/ tests/

# Use type hints
def process_playbook(playbook_id: str) -> Dict[str, Any]:
    """Process playbook with proper type hints."""
    return {"result": "success"}
```

#### Code Quality Guidelines

1. **Write Clear Code**
   - Use descriptive variable and function names
   - Keep functions small and focused
   - Add docstrings for all public functions and classes

2. **Follow Patterns**
   - Use existing patterns and conventions
   - Maintain consistency with existing codebase
   - Follow MCP protocol standards

3. **Error Handling**
   - Use appropriate exception types
   - Provide meaningful error messages
   - Log errors appropriately

4. **Performance**
   - Consider performance implications
   - Use async/await for I/O operations
   - Implement caching where appropriate

#### Example Code Structure

```python
"""Module for playbook processing functionality."""

import logging
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class PlaybookRequest(BaseModel):
    """Request model for playbook operations."""
    
    playbook_id: str = Field(..., description="Unique playbook identifier")
    parameters: Optional[Dict[str, Any]] = Field(default=None, description="Optional parameters")


class PlaybookProcessor:
    """Handles playbook processing operations."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize processor with configuration."""
        self.config = config
        logger.info("PlaybookProcessor initialized")
    
    async def process_playbook(self, request: PlaybookRequest) -> Dict[str, Any]:
        """
        Process a playbook request.
        
        Args:
            request: Validated playbook request
            
        Returns:
            Processed playbook result
            
        Raises:
            PlaybookNotFoundError: If playbook doesn't exist
            ProcessingError: If processing fails
        """
        try:
            # Implementation here
            logger.info(f"Processing playbook: {request.playbook_id}")
            return {"status": "success"}
        except Exception as e:
            logger.error(f"Failed to process playbook: {e}")
            raise
```

### Git Workflow

#### Branch Naming

```bash
# Feature branches
git checkout -b feature/add-new-playbook
git checkout -b feature/atlassian-integration

# Bug fix branches
git checkout -b fix/template-processing-error
git checkout -b fix/memory-leak-issue

# Documentation branches
git checkout -b docs/api-reference-update
git checkout -b docs/deployment-guide
```

#### Commit Messages

Follow conventional commit format:

```bash
# Format: type(scope): description

# Examples:
git commit -m "feat(playbooks): add API documentation generator"
git commit -m "fix(server): resolve memory leak in template processing"
git commit -m "docs(api): update endpoint documentation"
git commit -m "test(playbooks): add unit tests for epic template"
git commit -m "refactor(config): improve configuration validation"
```

**Commit Types:**
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `test`: Test additions or modifications
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `chore`: Maintenance tasks

## Pull Request Process

### Before Submitting

1. **Update your branch**
```bash
git fetch upstream
git rebase upstream/main
```

2. **Run quality checks**
```bash
# Format code
black src/ tests/
isort src/ tests/

# Run linting
flake8 src/ tests/

# Type checking
mypy src/

# Run tests
pytest tests/ -v --cov=src
```

3. **Update documentation** if needed

### Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes (or properly documented)

## Related Issues
Closes #123
```

### Review Process

1. **Automated Checks**: All CI checks must pass
2. **Code Review**: At least one maintainer review required
3. **Testing**: Comprehensive test coverage required
4. **Documentation**: Documentation updates for new features

## Issue Reporting

### Bug Reports

Use the bug report template:

```markdown
**Bug Description**
Clear description of the bug.

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen.

**Actual Behavior**
What actually happens.

**Environment**
- OS: [e.g., Ubuntu 20.04]
- Python version: [e.g., 3.11]
- Server version: [e.g., 2.0.0]

**Additional Context**
Any other relevant information.
```

### Feature Requests

Use the feature request template:

```markdown
**Feature Description**
Clear description of the proposed feature.

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should this feature work?

**Alternatives Considered**
Other approaches considered.

**Additional Context**
Any other relevant information.
```

## Development Workflow

### Setting Up Development Environment

```bash
# 1. Fork and clone repository
git clone https://github.com/YOUR_USERNAME/mcp-playbook-server.git
cd mcp-playbook-server

# 2. Set up Python environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt

# 3. Set up pre-commit hooks
pre-commit install

# 4. Create feature branch
git checkout -b feature/your-feature-name

# 5. Make changes and test
# ... make your changes ...
pytest tests/ -v

# 6. Commit and push
git add .
git commit -m "feat: add your feature"
git push origin feature/your-feature-name

# 7. Create pull request
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_playbooks.py -v

# Run tests matching pattern
pytest tests/ -k "test_epic" -v
```

### Local Development Server

```bash
# Run development server
python -m src.server

# Run with debug mode
DEBUG=true python -m src.server

# Run with hot reload (if available)
python -m src.server --reload
```

## Testing Guidelines

### Test Structure

```python
"""Test module for playbook functionality."""

import pytest
from unittest.mock import Mock, patch
from src.playbooks import PlaybookProcessor


class TestPlaybookProcessor:
    """Test cases for PlaybookProcessor class."""
    
    @pytest.fixture
    def processor(self):
        """Create processor instance for testing."""
        config = {"test": True}
        return PlaybookProcessor(config)
    
    def test_process_playbook_success(self, processor):
        """Test successful playbook processing."""
        request = PlaybookRequest(playbook_id="test_playbook")
        result = processor.process_playbook(request)
        
        assert result["status"] == "success"
        assert "playbook_id" in result
    
    def test_process_playbook_not_found(self, processor):
        """Test playbook not found error."""
        request = PlaybookRequest(playbook_id="nonexistent")
        
        with pytest.raises(PlaybookNotFoundError):
            processor.process_playbook(request)
    
    @patch('src.playbooks.external_service')
    def test_process_playbook_with_mock(self, mock_service, processor):
        """Test playbook processing with mocked external service."""
        mock_service.return_value = {"data": "test"}
        
        request = PlaybookRequest(playbook_id="test_playbook")
        result = processor.process_playbook(request)
        
        assert result["status"] == "success"
        mock_service.assert_called_once()
```

### Test Categories

1. **Unit Tests**: Test individual functions and classes
2. **Integration Tests**: Test component interactions
3. **API Tests**: Test HTTP endpoints
4. **Performance Tests**: Test performance characteristics

### Test Coverage

- Maintain minimum 80% test coverage
- Focus on critical paths and edge cases
- Include both positive and negative test cases

## Documentation Guidelines

### Documentation Types

1. **API Documentation**: Endpoint specifications and examples
2. **User Guides**: Step-by-step instructions for users
3. **Developer Guides**: Technical documentation for contributors
4. **Architecture Documentation**: System design and components

### Writing Guidelines

1. **Clear and Concise**: Use simple, direct language
2. **Examples**: Include practical examples and code snippets
3. **Structure**: Use consistent formatting and organization
4. **Updates**: Keep documentation current with code changes

### Documentation Format

```markdown
# Title

Brief description of the topic.

## Overview

Detailed explanation of the concept or feature.

## Usage

### Basic Example

```python
# Code example with explanation
result = function_call(parameters)
```

### Advanced Usage

More complex examples and use cases.

## Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `param1` | str | "default" | Parameter description |

## Troubleshooting

Common issues and solutions.
```

## Community and Support

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and community discussions
- **Email**: Direct contact for sensitive issues

### Getting Help

1. **Check Documentation**: Review existing guides and references
2. **Search Issues**: Look for similar problems or questions
3. **Ask Questions**: Use GitHub Discussions for help
4. **Report Bugs**: Use GitHub Issues for bug reports

### Helping Others

- Answer questions in discussions
- Review pull requests
- Improve documentation
- Share knowledge and experiences

## Recognition

### Contributors

All contributors are recognized in:
- README.md contributor section
- Release notes and changelogs
- Annual contributor acknowledgments

### Contribution Types

We value all types of contributions:
- Code contributions
- Documentation improvements
- Bug reports and testing
- Community support and mentoring
- Feature suggestions and feedback

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to the MCP Playbook Server! Your contributions help make this project better for everyone.