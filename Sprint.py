# Goal Tracker
# Sprint.py
# By Lo


class Sprint:
    'The Sprint object'

    def __init__(self, id, name, start, length, tasks, toDo, inProgress, done):
        self.id = id
        self.name = name
        self.start = start
        self.length = length
        self.tasks = tasks
        self.toDo = toDo
        self.inProgress = inProgress
        self.done = done
        self.newData = False

    def __str__(self):
        return f'Sprint: {self.name}\nStarted: {self.start}\nLength: {self.length}\nTasks:\n{self.listTasks()}'

    def listTasks(self):
        for task in self.tasks:
            print(task + '\n')
