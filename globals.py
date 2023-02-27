# Goal Tracker
# globals.py
# By Lo

# mySQL database login information
logIn = {
    'user': 'Lo',
    'password': '0784786589',
    'host': 'LoDesktop',
    'database': 'goalTracker'
}

# Table schema
createTasksTable = """
    CREATE TABLE tasks (
        id TEXT PRIMARY KEY,
        name VARCHAR(255),
        notes TEXT,
        created DATETIME,
        timeFrame VARCHAR(255),
        deadline DATETIME,
        priority VARCHAR(255),
        status VARCHAR(255)
    )    
    """
createGoalsTable = """
    CREATE TABLE goals (
        id TEXT PRIMARY KEY,
        name VARCHAR(255),
        notes TEXT,
        created DATETIME,
        timeFrame VARCHAR(255),
        deadline DATETIME,
        priority VARCHAR(255),
        status VARCHAR(255)
    )    
    """
createGoalTasksTable = """
    CREATE TABLE goalTasks (
        goalID TEXT PRIMARY KEY,
        taskID TEXT,
        FOREIGN KEY (goalID) REFERENCES goals(id)
    )
    """

createSprintsTable = """
    CREATE TABLE sprints (
        id TEXT PRIMARY KEY,
        name VARCHAR(255),
        start DATETIME,
        length VARCHAR(255)
    )
    """

createSprintTasksTable = """
    CREATE TABLE sprintTasks (
        sprintID TEXT PRIMARY KEY,
        taskID TEXT,
        FOREIGN KEY (sprintID) REFERENCES sprints(id)
    )
    """

createSprintToDoTable = """
    CREATE TABLE sprintToDo (
        sprintID TEXT PRIMARY KEY,
        taskID TEXT,
        FOREIGN KEY (sprintID) REFERENCES sprints(id)
    )
    """

createSprintInProgressTable = """
    CREATE TABLE sprintInProgress (
        sprintID TEXT PRIMARY KEY,
        taskID TEXT,
        FOREIGN KEY (sprintID) REFERENCES sprints(id)
    )
    """

createSprintDoneTable = """
    CREATE TABLE sprintDone (
        sprintID TEXT PRIMARY KEY,
        taskID TEXT,
        FOREIGN KEY (sprintID) REFERENCES sprints(id)
    )
    """


goals = []
sprints = []
