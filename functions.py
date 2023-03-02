# Goal Tracker
# functions.py
# By Lo

import mysql.connector
import uuid
import globals as gl


def createDB():
    'Creates the goalTracker database'
    # Connect to server
    db = mysql.connector.connect(**gl.logIn)
    cursor = db.cursor()
    cursor.execute(f'CREATE DATABASE %s', (gl.logIn['database']))

    # Adds tables to the database
    cursor.execute(gl.createTasksTable)
    cursor.execute(gl.createGoalsTable)
    cursor.execute(gl.createGoalTasksTable)
    cursor.execute(gl.createSprintsTable)
    cursor.execute(gl.createSprintTasksTable)
    cursor.execute(gl.createSprintToDoTable)
    cursor.execute(gl.createSprintInProgressTable)
    cursor.execute(gl.createSprintDoneTable)

    # Close connection to database
    if db.is_conected():
        cursor.close()
        db.close()


def checkForDB():
    'Returns True if the goalTracker database exsists'
    db = mysql.connector.connect(**gl.logIn)
    cursor = db.cursor()
    # Execute a query to check if the database exists
    cursor.execute(
        f'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s', (gl.logIn['database']))
    result = cursor.fetchone()
    if result:
        if db.is_conected():
            cursor.close()
            db.close()
        return True
    else:
        createDB()


def updateTasks():
    # Connect to server
    db = mysql.connector.connect(**gl.logIn)
    cursor = db.cursor()
    for task in gl.tasks:
        if task.newData == True:
            sql = f'UPDATE tasks SET name = {task.name}, notes = {task.notes}, created = {task.created}, timeFrame = {task.timeFrame}, deadline = {task.deadline}, priority = {task.priority}, status = {task.status} WHERE id = {task.id};'
            cursor.execute(sql)
            task.newData = False
    db.commit()
    cursor.close()
    db.close()


def updateGoals():
    # Connect to server
    db = mysql.connector.connect(**gl.logIn)
    cursor = db.cursor()
    for goal in gl.goals:
        if goal.newData == True:
            sql = f'UPDATE goals SET name = {goal.name}, notes = {goal.notes}, created = {goal.created} timeFrame = {goal.timeFrame}, deadline = {goal.deadline}, priority = {goal.priority}, status = {goal.status} WHERE id = {goal.id};'
            cursor.execute(sql)
            goal.newData = False
    db.commit()
    cursor.close()
    db.close()


def updateSprints():
    # Connect to server
    db = mysql.connector.connect(**gl.logIn)
    cursor = db.cursor()
    for sprint in gl.sprints:
        if sprint.newData == True:
            sql = f'UPDATE goals SET name = {sprint.name}, created = {sprint.created}, start = {sprint.start}, length = {sprint.length} WHERE id = {sprint.id};'
            cursor.execute(sql)
            sprint.newData = False
    db.commit()
    cursor.close()
    db.close()
