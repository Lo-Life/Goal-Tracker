# Goal Tracker
# Task.py
# By Lo

import datetime as dt


class Task:
    'The Task object'

    def __init__(self, id, name, notes, created, timeFrame, deadline, priority, status):
        self.id = id
        self.name = name
        self.notes = notes
        self.created = created
        self.timeFrame = timeFrame
        self.deadLine = deadline
        self.priority = priority
        self.status = status

    def __str__(self):
        return f'Name: {self.name} \nPriority: {self.priority} \nStatus: {self.status}'

    def complete(self):
        self.status = 'Completed at ' + str(dt.datetime.now())
