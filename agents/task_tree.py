# agents/task_tree.py

class TaskTree:
    def __init__(self):
        self.tree = {}

    def add_task(self, subtopic, task_details):
        # Add a new task to the Task Tree
        self.tree[subtopic] = task_details
        print(f"Added task for {subtopic}: {task_details}")

    def get_tasks(self):
        # Retrieve all tasks in the Task Tree
        return self.tree
