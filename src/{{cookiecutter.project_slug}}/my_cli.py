"""
Command-line interface for {{ cookiecutter.project_name }} using Typer.
"""
import typer
from {{ cookiecutter.project_slug }}.main import greet

app = typer.Typer()

@app.command()
def hello(name: str):
    """Greet someone by name."""
    typer.echo(greet(name))


if __name__ == "__main__":
    app()