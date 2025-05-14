"""
Core functionality for {{ cookiecutter.project_name }}.
"""

def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Example entry point
    print(greet("World"))
