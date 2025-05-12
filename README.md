# Modern Python Development Environment Setup Guide

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
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
    # If Typer is a direct dependency of your project itself, add it here too:
    # "typer>=0.15.3", # Or your target Typer version
    # "click==8.1.8", # And the pinned Click version
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",          # Linter/Formatter
    "mypy>=1.7.0",          # Static Type Checker
    "typer>=0.15.3",        # For CLIs (using your current version or a target one)
    "click==8.1.8",         # Pinned version for Typer compatibility
    "pytest>=7.4.0",        # Testing framework
    "pytest-cov>=4.1.0",    # Test coverage
    "pytest-asyncio>=0.21.0", # For testing async code with pytest
    "pre-commit>=3.6.0",    # Git hooks manager
    "pip-tools>=7.3.0",     # For dependency management (compiling requirements)
    "commitizen>=3.13.0",   # For conventional commits
    "bandit>=1.7.6",        # Security linter
    "safety>=2.4.0",        # Checks for vulnerable dependencies
    "prettier",             # Optional: if you still use it for non-Python files
    "autopep8",             # Optional: if used for specific cases not covered by Ruff
    "docformatter",         # Optional: if Ruff's docstring formatting isn't sufficient
    "types-requests",       # Example: Stubs for type checking requests library
    "types-setuptools",     # Example: Stubs for type checking setuptools
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10" # Or your target Python version
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true # Can be helpful initially

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"] # B101: assert_used, B601: paramiko_calls

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0" # This should match your [project] version
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
     # "src/project_name/__init__.py:__version__" # If you store version in __init__.py too
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: [https://github.com/pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
    rev: v4.5.0 # Or your chosen version
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: [https://github.com/astral-sh/ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
    rev: v0.2.0 # Or your chosen version
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix, --exit-non-zero-on-fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: [https://github.com/pre-commit/mirrors-mypy](https://github.com/pre-commit/mirrors-mypy)
    rev: v1.8.0 # Or your chosen version
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: [https://github.com/PyCQA/bandit](https://github.com/PyCQA/bandit)
    rev: 1.7.6 # Or your chosen version
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: [https://github.com/commitizen-tools/commitizen](https://github.com/commitizen-tools/commitizen)
    rev: 3.13.0 # Or your chosen version
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: [https://github.com/PyCQA/docformatter](https://github.com/PyCQA/docformatter)
    rev: v1.7.5 # Or your chosen version
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile --output-file requirements.txt pyproject.toml
pip-tools compile --extra dev --output-file requirements-dev.txt pyproject.toml
pip-tools sync requirements.txt requirements-dev.txt

# Or create requirements.txt manually for runtime, and install dev tools separately
# pip freeze > requirements.txt (for runtime)
# pip install ruff mypy typer "click==8.1.8" pytest pytest-cov pytest-asyncio pre-commit pip-tools commitizen bandit safety #... (for dev)
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```

### 2. VS Code Settings
Create `.vscode/settings.json` for VS Code users:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "none",
  "python.linting.mypyEnabled": true,
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
  },
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.rulers": [88],
    "editor.tabSize": 4
  }
}
```

### 3. PyCharm Settings
For PyCharm users, configure the IDE to work with the modern toolstack:

#### 3.1. Configure Virtual Environment
1. Go to `File > Settings > Project > Python Interpreter`
2. Click the gear icon and select `Add`
3. Choose `Existing environment` and browse to `.venv/bin/python` (macOS/Linux) or `.venv\Scripts\python.exe` (Windows)

#### 3.2. Configure Code Style
Create `.idea/codeStyleSettings.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectCodeStyleConfiguration">
    <code_scheme name="Project" version="173">
      <Python>
        <option name="ALIGN_COLLECTIONS_AND_COMPREHENSIONS" value="false" />
        <option name="DICT_ALIGNMENT" value="0" />
        <option name="HANG_CLOSING_BRACKETS" value="false" />
        <option name="NEW_LINE_AFTER_COLON" value="false" />
        <option name="NEW_LINE_AFTER_COLON_MULTI_LINE" value="false" />
        <option name="OPTIMIZE_IMPORTS_SORT_NAMES_IN_FROM_IMPORTS" value="true" />
        <option name="OPTIMIZE_IMPORTS_SORT_IMPORTS" value="true" />
        <option name="OPTIMIZE_IMPORTS_SORT_BY_TYPE_FIRST" value="true" />
      </Python>
      <codeStyleSettings language="Python">
        <option name="ALIGN_MULTILINE_PARAMETERS" value="false" />
        <option name="ALIGN_MULTILINE_PARAMETERS_IN_CALLS" value="false" />
        <option name="CALL_PARAMETERS_LPAREN_ON_NEXT_LINE" value="false" />
        <option name="CALL_PARAMETERS_RPAREN_ON_NEXT_LINE" value="false" />
        <option name="METHOD_PARAMETERS_LPAREN_ON_NEXT_LINE" value="false" />
        <option name="METHOD_PARAMETERS_RPAREN_ON_NEXT_LINE" value="false" />
        <indentOptions>
          <option name="INDENT_SIZE" value="4" />
          <option name="CONTINUATION_INDENT_SIZE" value="4" />
          <option name="TAB_SIZE" value="4" />
        </indentOptions>
      </codeStyleSettings>
    </code_scheme>
  </component>
</project>
```

#### 3.3. Configure External Tools
Go to `File > Settings > Tools > External Tools` and add these tools:

**Add Ruff (Lint):**
- Name: `Ruff Lint`
- Program: `.venv/bin/ruff` (macOS/Linux) or `.venv\Scripts\ruff.exe` (Windows)
- Arguments: `check --fix $FilePath# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Working directory: `$ProjectFileDir# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Advanced Options: Check "Open console for tool output"

**Add Ruff (Format):**
- Name: `Ruff Format`
- Program: `.venv/bin/ruff` (macOS/Linux) or `.venv\Scripts\ruff.exe` (Windows)
- Arguments: `format $FilePath# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Working directory: `$ProjectFileDir# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Advanced Options: Check "Synchronize files after execution"

**Add MyPy:**
- Name: `MyPy`
- Program: `.venv/bin/mypy` (macOS/Linux) or `.venv\Scripts\mypy.exe` (Windows)
- Arguments: `$FilePath# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Working directory: `$ProjectFileDir# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Advanced Options: Check "Open console for tool output"

#### 3.4. Configure File Watchers
Go to `File > Settings > Tools > File Watchers` and add:

**Add Ruff Watcher:**
- Name: `Ruff`
- File type: `Python`
- Scope: `Project Files`
- Program: `.venv/bin/ruff` (macOS/Linux) or `.venv\Scripts\ruff.exe` (Windows)
- Arguments: `check --fix $FilePath# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Output paths to refresh: `$FilePath# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Working directory: `$ProjectFileDir# Modern Python Development Environment Setup Guide

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

## Step 5: Configure Tools via `pyproject.toml`

Create a comprehensive `pyproject.toml` configuration:

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "ruff>=0.2.0",
    "mypy>=1.7.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
    "pre-commit>=3.6.0",
    "pip-tools>=7.3.0",
    "commitizen>=3.13.0",
    "bandit>=1.7.6",
    "safety>=2.4.0",
]

# --- Tool Configurations ---

[tool.ruff]
# Enable modern Python features
target-version = "py310"

# Set the maximum line length
line-length = 88

# Enable import sorting, docstring formatting, and more
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
    "UP", # pyupgrade
    "N",  # pep8-naming
    "D",  # pydocstyle (docstrings)
    "S",  # bandit (security)
    "ANN", # flake8-annotations
    "PTH", # flake8-use-pathlib
]

# Never ignore, but feel free to customize
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D103", # Missing docstring in public function
    "D104", # Missing docstring in public package
    "D105", # Missing docstring in magic method
    "D213", # Multi-line docstring summary should start at the second line
    "ANN101", # Missing type annotation for 'self' in method
    "S101", # Use of assert detected (useful for testing)
]

# Exclude folders and files
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

# Allow autofix for specific rules
fixable = ["I", "F", "UP", "PTH"]
unfixable = []

# Ruff import sorting configuration (replaces isort)
[tool.ruff.isort]
known-first-party = ["src"]
section-order = ["future", "standard-library", "third-party", "first-party", "local-folder"]
combine-as-imports = true
force-wrap-aliases = true

# Ruff docstring configuration
[tool.ruff.pydocstyle]
convention = "google"  # Use Google style docstrings

# Ruff per-file ignores
[tool.ruff.per-file-ignores]
"tests/**/*.py" = ["S101", "ANN", "D"]  # Allow assertions and no type hints in tests
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
pretty = true
show_column_numbers = true
show_error_codes = true
ignore_missing_imports = true

# Exclude paths from mypy
exclude = [
    '\.git/',
    '\.venv/',
    'build/',
    'dist/',
]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q -s --strict-markers --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
python_files = "test_*.py *_test.py"
python_classes = "Test*"
python_functions = "test_*"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
    "asyncio: marks tests as async tests",
]

# Pytest coverage configuration
[tool.coverage.run]
branch = true
source = ["src"]
omit = ["tests/*", "*/migrations/*", "*/tests/*"]

[tool.coverage.report]
show_missing = true
ignore_errors = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]

[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
]
```

## Step 6: Set Up Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
# .pre-commit-config.yaml
repos:
  # Basic pre-commit hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key
      - id: check-ast

  # Ruff linter and formatter (replaces Black, isort, Flake8)
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      # Lint with Ruff
      - id: ruff
        args: [ --fix ]
      # Format with Ruff
      - id: ruff-format

  # Type checking with mypy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--config-file=pyproject.toml]

  # Security checks with bandit
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # Commit message linting
  - repo: https://github.com/commitizen-tools/commitizen
    rev: 3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]

  # Optional: Docstring formatter
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.5
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=88, --wrap-descriptions=88]
```

## Step 7: Install Pre-commit Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

## Step 8: Create Initial Project Structure

Create a basic project structure:

```bash
# Create source directory structure
mkdir -p src/project_name
touch src/__init__.py
touch src/project_name/__init__.py
touch src/project_name/main.py

# Create tests directory
mkdir -p tests
touch tests/__init__.py
touch tests/test_example.py

# Create documentation directory
mkdir -p docs
touch docs/README.md

# Create other necessary files
touch README.md
touch LICENSE
touch CHANGELOG.md
```

Create a sample test file (`tests/test_example.py`):

```python
"""Example test file."""
import pytest

from src.project_name.main import example_function


def test_example():
    """Test example function."""
    assert example_function() == "Hello, World!"


@pytest.mark.asyncio
async def test_async_example():
    """Test async example function."""
    # Async test example
    result = await async_example_function()
    assert result is not None
```

## Step 9: Install Dependencies

Create a `requirements.txt` or use pip-tools for better dependency management:

```bash
# Using pip-tools for dependency management
pip-tools compile pyproject.toml
pip-tools sync requirements.txt

# Or create requirements.txt manually
pip freeze > requirements.txt
```

## Step 10: Initial Commit

Make your first commit with all the setup files:

```bash
# Add all files
git add .gitignore pyproject.toml .pre-commit-config.yaml
git add src/ tests/ docs/
git add README.md LICENSE CHANGELOG.md

# First commit using conventional commit format
git commit -m "feat: initial project setup with modern dev tools"

# Optionally, create a tag
git tag v0.1.0
```

## Additional Recommendations

### 1. EditorConfig
Create `.editorconfig` for consistent formatting across editors:

```ini
# .editorconfig
root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.py]
indent_size = 4
max_line_length = 88

[*.{yml,yaml}]
indent_size = 2

[*.{md,rst}]
trim_trailing_whitespace = false
```


- Advanced Options: Uncheck "Auto-save edited files to trigger the watcher"

#### 3.5. Configure Run Configurations
Create `.idea/runConfigurations/pytest.xml`:

```xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="pytest" type="tests" factoryName="py.test">
    <module name="" />
    <option name="INTERPRETER_OPTIONS" value="" />
    <option name="PARENT_ENVS" value="true" />
    <envs />
    <option name="SDK_HOME" value="" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
    <option name="IS_MODULE_SDK" value="true" />
    <option name="ADD_CONTENT_ROOTS" value="true" />
    <option name="ADD_SOURCE_ROOTS" value="true" />
    <EXTENSION ID="PythonCoverageRunConfigurationExtension" runner="coverage.py" />
    <option name="SCRIPT_NAME" value="" />
    <option name="CLASS_NAME" value="" />
    <option name="METHOD_NAME" value="" />
    <option name="FOLDER_NAME" value="" />
    <option name="TEST_TYPE" value="TEST_SCRIPT" />
    <option name="PATTERN" value="" />
    <option name="USE_PATTERN" value="false" />
    <option name="testToRun" value="" />
    <option name="keywords" value="" />
    <option name="params" value="-v --cov=src --cov-report=html" />
    <option name="USE_PARAM" value="true" />
    <option name="USE_KEYWORD" value="false" />
    <method v="2" />
  </configuration>
</component>
```

#### 3.6. Configure Project Structure
Go to `File > Settings > Project > Project Structure` and mark directories:
- Mark `src` as "Sources Root"
- Mark `tests` as "Test Sources Root"
- Mark `.venv` as "Excluded"

#### 3.7. Configure Git Integration
PyCharm should automatically detect your `.gitignore` file. For commit message templates:

1. Go to `File > Settings > Version Control > Git`
2. Check "Use non-modal commit interface"
3. Go to `File > Settings > Version Control > Commit`
4. Check "Enable commit checks before commit"
5. Add commit inspection: "Python Inspection"

#### 3.8. PyCharm Configuration Files
Create `.idea/inspectionProfiles/Project_Default.xml`:

```xml
<component name="InspectionProjectProfileManager">
  <profile version="1.0">
    <option name="myName" value="Project Default" />
    <inspection_tool class="PyBroadExceptionInspection" enabled="false" level="WEAK WARNING" enabled_by_default="false" />
    <inspection_tool class="PyChainedComparisonsInspection" enabled="true" level="WEAK WARNING" enabled_by_default="true">
      <option name="ignoreConstantInTheMiddle" value="true" />
    </inspection_tool>
    <inspection_tool class="PyPackageRequirementsInspection" enabled="true" level="WARNING" enabled_by_default="true">
      <option name="ignoredPackages">
        <value>
          <list size="0" />
        </value>
      </option>
    </inspection_tool>
    <inspection_tool class="PyPep8Inspection" enabled="false" level="WEAK WARNING" enabled_by_default="false" />
    <inspection_tool class="PyPep8NamingInspection" enabled="false" level="WEAK WARNING" enabled_by_default="false" />
  </profile>
</component>
```

#### 3.9. Keyboard Shortcuts
Add custom keyboard shortcuts for quick access to tools:
1. Go to `File > Settings > Keymap`
2. Search for "External Tools > Ruff Lint" and assign `Ctrl+Alt+L` (or `⌘+⌥+L` on macOS)
3. Search for "External Tools > Ruff Format" and assign `Ctrl+Alt+F` (or `⌘+⌥+F` on macOS)
4. Search for "External Tools > MyPy" and assign `Ctrl+Alt+M` (or `⌘+⌥+M` on macOS)

#### 3.10. Optional: PyCharm Plugin Recommendations
Install these plugins via `File > Settings > Plugins`:
- `.env files support` - for environment file syntax highlighting
- `Requirements` - for requirements.txt management
- `Markdown` - for README and documentation
- `GitToolBox` - enhanced Git integration
- `Rainbow Brackets` - for better code readability

### 4. GitHub Actions CI/CD
Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.10, 3.11, 3.12]

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]
    
    - name: Lint with Ruff
      run: |
        ruff check .
        ruff format --check .
    
    - name: Type check with mypy
      run: mypy .
    
    - name: Test with pytest
      run: pytest --cov=./ --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: false
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
