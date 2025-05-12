# rich_demo.py
from rich import print
from rich.panel import Panel
from rich.table import Table

my_dict = {"name": "AJ", "role": "Cloud AI Architect", "skills": ["Python", "AWS", "MLOps", "GenAI"]}
my_list = [1, "apple", {"key": "value"}, True, None, 3.14]

print("--- Rich Printing ---")
print(my_dict)
print(my_list)

print(Panel("Hello, [bold magenta]World[/]!", title="[bold green]Welcome[/]", subtitle="Thank you"))

table = Table(title="My Project Tasks")
table.add_column("ID", style="dim", width=12)
table.add_column("Task Name")
table.add_column("Status", justify="right")

table.add_row("1", "Setup Environment", "[green]Done[/green]")
table.add_row("2", "Develop Model", "[yellow]In Progress[/yellow]")
table.add_row("3", "Deploy to SageMaker", "[red]Pending[/red]")

print(table)