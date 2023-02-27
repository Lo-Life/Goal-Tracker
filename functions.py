# Goal Tracker
# functions.py
# By Lo

import mysql.connector
import uuid
import globals as gl


def checkForDB():
    'Returns True if the goalTracker database exsists'
    cnx = mysql.connector.connect(**gl.logIn)
    cursor = cnx.cursor()
    # Execute a query to check if the database exists
    cursor.execute(
        f'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s', (gl.logIn['database']))
    result = cursor.fetchone()
    if result:
        if cnx.is_conected():
            cursor.close()
            cnx.close()
        return True
    else:
        if cnx.is_conected():
            cursor.close()
            cnx.close()
        return False


def createDB():
    'Creates the goalTracker database'
    # Connect to server
    cnx = mysql.connector.connect(**gl.logIn)
    cursor = cnx.cursor()
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
    if cnx.is_conected():
        cursor.close()
        cnx.close()


def addGoal():
    'Adds a Goal to goals'
    id = str(uuid.uuid4())


def addTask():
    'Adds a task to tasks'
    id = str(uuid.uuid4())


def save():
    pass
