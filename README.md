# Todo Manager

Todo Manager is a command-line application that allows you to manage your tasks. You can add new tasks, list all tasks, delete tasks, and mark tasks as completed.

## Installation

1. Clone the repository:

```bash
  git clone https://github.com/your-username/todo-manager.git

```

2. Navigate to the project directory:

```bash
  cd todo-manager
```

3. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

## Usage

To use the Todo Manager app, follow the steps below:

Ensure you are in the project directory and have activated the virtual environment (if used).

Run the following command to execute the CLI:

```bash
python -m todo_app.cli
```

### Available Commands

- `add`: Add a new task.
- `list`: List all tasks.
- `delete`: Delete a task.
- `complete`: Mark a task as completed.

## Architecture

The Todo Manager app follows a simple and modular architecture. Here's an overview of the key components:

- `cli.py`: This file contains the command-line interface (CLI) logic using the `click` library. It defines commands such as `add`, `list`, `delete`, and `complete` and connects them to the corresponding functions in the `utils.py` file.

- `models.py`: This file defines the `Task` class, representing a single task with properties like `description` and `completed`.

- `utils.py`: This file contains utility functions for loading and saving tasks. It provides the `load_tasks` and `save_tasks` functions, which handle reading tasks from and writing tasks to the `tasks.txt` file.

- `data/tasks.txt`: This file stores the tasks. Each task is stored as a line in the file, with the format: `<description>,<completed>`. The `load_tasks` function reads from this file, and the `save_tasks` function writes to it.

## Contributing

Contributions to the Todo Manager app are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
