# agents/task_tree.py

class TaskTree:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.subtopic] = task

    def remove_task(self, task):
        if task.subtopic in self.tasks:
            del self.tasks[task.subtopic]

    def get_tasks(self):
        return self.tasks

    def visualize_tasks(self):
        for subtopic, task in self.tasks.items():
            print(f"Task: {subtopic}, Status: {task.status}")
