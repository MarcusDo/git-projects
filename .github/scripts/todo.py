# todo.py
class Task:
    # Constructor initializes the task with title and status
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status  # Status defaults to "ToDo"

    # Marks the task as completed and changes its status to "Done"
    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    # Returns a concise string representation of the task
    def __repr__(self):
        return f"{self.title} - {'Done' if self.completed else 'ToDo'}"

    # Returns a user-friendly description for print() or str()
    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"
