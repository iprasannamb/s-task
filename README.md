# 📋 Task Manager

> A sleek and intuitive command-line task management application built in Python

**Features at a glance:** Add, display, edit, and update tasks with persistent storage

## ✨ Features

- **Add Tasks**: Create new tasks with a simple input interface
- **Display Tasks**: View all tasks with their current status (Done/Not Done)
- **Edit Tasks**: Modify existing task descriptions
- **Update Status**: Toggle task completion status between Done and Not Done
- **Persistent Storage**: Tasks are saved to a text file (`task.txt`) for persistence

## 🛠️ Requirements

- **Python 3.10+** (uses `match` statement)
- **No external dependencies** required

## 🚀 Installation

1. Download the `init.py` file
2. Ensure you have Python 3.10+ installed
3. Run the script directly

## Usage

Run the application:

```bash
python init.py
```

### Menu Options

| Option | Description |
|--------|-------------|
| **1** | **Add Task** - Enter new tasks one by one. Type 'exit' or leave blank to finish |
| **2** | **Display Tasks** - Shows all tasks with their current status and index numbers |
| **3** | **Edit Task** - Select a task by number and modify its description |
| **4** | **Update Status** - Toggle a task's completion status between Done and Not Done |

### Example Workflow

```
1. Start the application
2. Select option 1 to add tasks
3. Enter your tasks (e.g., "Buy groceries", "Complete project")
4. Select option 2 to view all tasks
5. Select option 4 to mark tasks as completed
6. Select option 3 to edit task descriptions if needed
```

## File Structure

```
Project Directory
├── init.py          # Main application file
└── task.txt         # Auto-generated task storage file
```

## Data Format

Tasks are stored in `task.txt` with the following format:
```
Buy groceries-False
Complete project-True
```

**Format breakdown:**
- Task description comes before the dash
- Status is either `True` (Done) or `False` (Not Done)

## Notes

- Tasks are automatically saved when added
- The application creates `task.txt` if it doesn't exist
- Empty input or typing 'exit' will stop the task addition process
- Task numbers start from 1 for user convenience
