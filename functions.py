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
    cnx = mysql.connector.connect(**gl.logIn)
    cursor = cnx.cursor()
    cursor.execute(f'CREATE DATABASE %s', (gl.logIn['database']))

    # Adds tables to the database
    createTaskTable = """
    CREATE TABLE tasks (
        id TEXT PRIMARY KEY,
        name VARCHAR(255),
        notes TEXT,
        created DATETIME,
        timeFrame VARCHAR(255),
        deadline DATETIME
        priority VARCHAR(255)
        status VARCHAR(255)
    )    
    """
    cursor.execute(createTaskTable)


def addGoal():
    'Adds a Goal to goals'
    id = str(uuid.uuid4())


def addTask():
    'Adds a task to tasks'
    id = str(uuid.uuid4())


def save():
    pass
