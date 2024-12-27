import os

BACKUP_FILE = "backup.txt"

def save_to_file(filename, data, mode="a"):
    """Save data to file."""
    with open(filename, mode) as file:
        file.write(data + "\n")

def load_from_file(filename):
    """Load data from a file."""

class ToDoList:
    def __init__(self):
        self.tasks = load_from_file(BACKUP_FILE)

    def add_task(self, task):
        self.tasks.append(task)
        save_to_file(BACKUP_FILE, task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' has been removed.")
            self._backup_tasks()
        else:
            print(f"No such task '{task}' exists.")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task updated from '{old_task}' to '{new_task}'.")
            self._backup_tasks()
        else:
            print(f"'{old_task}' is not present in the list.")

    def show_tasks(self):
        if self.tasks:
            print("Your Todo List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your Todo List is empty.")

    def _backup_tasks(self):
        """Rewrites all tasks to the backup file."""
        with open(BACKUP_FILE, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")


# Main execution
todo_list = ToDoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Do homework")
todo_list.add_task("Call Mom")

todo_list.show_tasks()

todo_list.remove_task("Finish the report")
todo_list.update_task("Buy groceries", "Go for a walk")
todo_list.show_tasks()


