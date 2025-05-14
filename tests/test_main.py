"""
Test suite for the greeting functionality.
"""
import pytest
from {{ cookiecutter.project_slug }}.main import greet


def test_greet():
    """Ensure greet returns the expected string with an exclamation."""
    assert greet("Developer") == "Hello, Developer!"