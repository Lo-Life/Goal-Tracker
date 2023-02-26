# Goal Tracker
# Sprint.py
# By Lo


class Sprint:
    'The Sprint object'

    def __init__(self, id, name, start, length, backlog, blocked, toDo, inProgress, done):
        self.id = id
        self.name = name
        self.start = start
        self.length = length
        self.backlog = backlog
        self.blocked = blocked
        self.toDo = toDo
        self.inProgress = inProgress
        self.done = done

    def __str__(self):
        return f'Sprint: {self.name} \n started: {self.start} \n length: {self.length}'
