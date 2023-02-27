# Goal Tracker
# Goal.py
# By Lo

import datetime as dt


class Goal:
    "The Goal object"

    def __init__(self, id, name, notes, tasks, created, timeFrame, deadline, priority, status):
        self.id = id
        self.name = name
        self.notes = notes
        self.tasks = tasks
        self.created = created
        self.timeFrame = timeFrame
        self.deadLine = deadline
        self.priority = priority
        self.status = status

    def __str__(self):
        return f'Goal: {self.name}\nDeadline: {self.deadLine}\npriority: {self.priority}\nstatus: {self.status}\ntasks:\n{self.listTasks()}'

    def complete(self):
        self.status = 'Completed at ' + str(dt.datetime.now())

    def listTasks(self):
        for task in self.tasks:
            print(task + '\n')
