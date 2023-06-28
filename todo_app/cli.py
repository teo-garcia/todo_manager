import click
from .models import Task
from .utils import save_tasks, load_tasks

@click.group()
def cli():
    pass


@click.command()
@click.argument("description")
def add(description):
    """Add a new task"""
    tasks = load_tasks()
    task = Task(description)
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f"\n Task '{description}' added.\n")

@click.command()
def list(): 
    """List all tasks"""
    tasks = load_tasks()
    click.echo("\n Tasks:\n")
    if tasks:
        for task in tasks:
            click.echo(task)
    else:
        click.echo("\n No tasks found.\n")

@click.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """Complete a task"""
    tasks = load_tasks()
    if task_id > 0 and task_id <= len(tasks):
        task = tasks[task_id - 1]
        task.completed = True
        save_tasks(tasks)
        click.echo(f"\nTask '{task.description}' completed.\n")
    else:
        click.echo("\nInvalid task ID.\n")



@click.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task"""
    tasks = load_tasks()
    if task_id > 0 and task_id <= len(tasks):
        task = tasks.pop(task_id - 1)
        save_tasks(tasks)
        click.echo(f"\n Task '{task.description}' deleted")
    else:
        click.echo("\nInvalid task ID.\n")


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
  cli()