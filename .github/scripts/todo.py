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


class TaskPool:
    def __init__(self):
        self.tasks = []  # Initializes an empty list to store tasks

    def populate(self):
        # Create tasks with different initial statuses
        task1 = Task("Add Login UI", status="Done")
        task2 = Task("Fix UI Bug", status="Done")
        task3 = Task("Write Tests", status="Done")
        task4 = Task("Update Login UI", status="ToDo")
        task5 = Task("Update Documentation", status="ToDo")
        task6 = Task("Deploy to Production", status="ToDo")

        # Mark the first three tasks as completed
        task1.mark_completed()
        task2.mark_completed()
        task3.mark_completed()

        # Assign all tasks to the pool
        self.tasks = [task1, task2, task3, task4, task5, task6]

    def add_task(self, task):
        # Adds a Task object to the list
        self.tasks.append(task)

    def get_open_tasks(self):
        # Returns only the tasks that are still "ToDo"
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        # Returns only the tasks that are marked "Done"
        return [task for task in self.tasks if task.status == "Done"]

def main():
    pool = TaskPool()
    pool.populate()

    task_titles = [task.title for task in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for title in task_titles:
        print(title)

    completed_titles = [task.title for task in pool.get_done_tasks()]
    print("\nDone Tasks:")
    for title in completed_titles:
        print(title)

