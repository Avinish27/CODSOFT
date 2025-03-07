import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{index}. {task['task']} [{status}]")

    def mark_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            self.save_tasks()

todo = ToDoList()
todo.add_task("Complete Python project")
todo.add_task("Study for exams")
todo.view_tasks()
todo.mark_done(1)
todo.view_tasks()
todo.delete_task(2)
todo.view_tasks()
