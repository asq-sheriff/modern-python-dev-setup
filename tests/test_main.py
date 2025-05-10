# tests/test_main.py
from src.my_package.main import greet

def test_greet():
    assert greet("Developer") == "Hello, Developer"