# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Overview
This guide provides a comprehensive setup for a modern Python development environment with state-of-the-art tools and best practices. We'll use Ruff (a fast all-in-one linter/formatter that replaces Black, isort, and Flake8) along with other essential tools.

## Step 1: Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate on macOS/Linux
source .venv/bin/activate

# Activate on Windows (Git Bash or WSL)
source .venv/Scripts/activate

# Activate on Windows (Command Prompt)
.venv\Scripts\activate.bat

# Activate on Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

## Step 2: Initialize Git Repository

```bash
git init
```

## Step 3: Create `.gitignore` File

Create a comprehensive `.gitignore` file:

```gitignore
# Virtual Environment
.venv/
venv/
env/
ENV/

# IDE and OS files
.idea/
.vscode/
*.iml
.DS_Store
desktop.ini
*.swp
*.swo
*~

# Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Build artifacts
build/
dist/
*.egg-info/
*.egg
.eggs/
pip-wheel-metadata/

# Coverage reports
.coverage
.coverage.*
coverage.xml
htmlcov/
.tox/
.nox/
.hypothesis/

# Type checkers
.mypy_cache/
.dmypy.json
dmypy.json
.pytype/
.pyre/

# Testing
.pytest_cache/
.ruff_cache/
.cache/

# Documentation
docs/_build/
site/

# Secrets and sensitive files
.env
.env.*
secrets.json
*.pem
*.key

# Database
*.db
*.sqlite3

# Logs
*.log
logs/

# Local development files
.local/
```

## Step 4: Install Development Tools

Install modern development tools with Ruff replacing Black, isort, and Flake8:

```bash
# Core development tools
pip install \
    ruff \
    mypy \
    typer \
    "click==8.1.8" \  # Pin click to 8.1.8 as a workaround for Typer (see note)
    pytest pytest-cov pytest-asyncio \
    pre-commit \
    pip-tools \
    commitizen

# Additional utilities (optional but recommended)
pip install \
    bandit \
    safety \
    prettier \
    autopep8 \
    docformatter \
    types-requests types-setuptools
```
Note on Typer/Click Versioning:
As of May 2025, Typer (e.g., version 0.15.3+) has a known incompatibility with Click versions 8.2.0 and higher. This can lead to TypeErrors during help message generation (e.g., Parameter.make_metavar() missing 1 required positional argument: 'ctx') or when Click tries to format error messages. This issue has been observed on Python 3.11+ including Python 3.13.

A common workaround, as discussed in the Typer community (e.g., GitHub issue #1215 for fastapi/typer), is to pin the click dependency to a version known to be compatible, such as click==8.1.8. Keep an eye on Typer's release notes for official fixes and updated Click compatibility (e.g., related to Typer PRs #1145, #1218).

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{{ cookiecutter.project_slug }}"
version = "0.1.0"
description = "{{ cookiecutter.description }}"
authors = [{ name = "{{ cookiecutter.author_name }}", email = "{{ cookiecutter.author_email }}" }]
readme = "README.md"
requires-python = ">= {{ cookiecutter.python_version }}"

[project.optional-dependencies]
dev = [
    "pre-commit>=4.4.0",
    "ruff>=0.11.9",
    "mypy>=1.15.0",
    "bandit>=1.8.3",
    "docformatter>=1.7.7",
    "commitizen>=4.7.0"
]
```

## Step 6: Set Up Pre-commit Hooks

Your .pre-commit-config.yaml is templated and will be copied verbatim. After scaffold, hooks install automatically, or run:

```bash
pre-commit install --install-hooks
```

## Step 7: Create Initial Project Structure

Scaffold creates:

src/{{ cookiecutter.project_slug }}/ with main.py, my_cli.py, rich_demo.py

tests/ with test_main.py

You can add docs under docs/, CI under .github/, etc., as needed.

Development Workflow

On save: use File Watchers (Ruff, Docformatter, Mypy) in PyCharm to auto-fix/style.

On commit: Git hooks (pre-commit) validate and fix issues.

In CI: run ruff check . && ruff format --check . && mypy . && pytest --cov=src


### src/{{cookiecutter.project_slug}}/main.py

```python
"""
Core functionality for {{ cookiecutter.project_name }}.
"""

def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Example entry point
    print(greet("World"))
```

## Summary

This modern setup provides:

1. **Ruff** instead of Black, isort, and Flake8 (faster, unified tool)
2. **mypy** for type checking
3. **pytest** with async support and coverage
4. **pre-commit** hooks for automated code quality
5. **bandit** for security checks
6. **commitizen** for conventional commit messages
7. **pip-tools** for better dependency management
8. Comprehensive configuration in `pyproject.toml`
9. Ready-to-use CI/CD pipeline with GitHub Actions

All tools are configured to work together seamlessly, providing a robust development environment for any Python project.
