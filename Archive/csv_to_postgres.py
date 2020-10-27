import pandas as pd
import psycopg2
import os

"""
Trying to update the script to have it update the column names of a new table to fit the column
"""


def connect_to_database(
    databasename="testdb",
    databaseIP="localhost",
    databaseport="5432",
    username="postgres",
    password="postgres",
):
    """Module takes arguments to connect to a PostgreSQL database using SQL Alchemy and returns a connection.
    Args:
        databasename: Name of the database to connect. Default livingdb
        databaseIP: IP address of the database server.
        databaseport: Port of the database server
        username: DB username
        password: User password
    Returns:
        connection: connection to the database
        cursor: cursor for database connection
    """
    # Create the connection
    connection = psycopg2.connect(
        host=databaseIP, user=username, password=password, dbname=databasename
    )
    cursor = connection.cursor()
    return connection, cursor


conn, cur = connect_to_database()


path1 = r"C:\Users\Hank\Documents"
tb = "test"
path = os.path.join(path1, "Testing.csv")
print(
    os.path.exists(path)
)  # This will return True or False depending on if the file exists
# --------------------------------------------------------------------
# This gets the names of the columns from the table and can be used as the column names of the csv.
#https://stackoverflow.com/questions/10252247/how-do-i-get-a-list-of-column-names-from-a-psycopg2-cursor
cur.execute("SELECT * FROM test29 LIMIT 0")
col_names = [desc[0] for desc in cur.description]
# --------------------------------------------------------------------
def csv_to_postgres():
    sql = f"""COPY {tb} FROM STDIN DELIMITER ',' CSV HEADER;"""
    with open(path) as f:
        cur.copy_expert(sql, f)
    conn.commit()
    print(f"Printing to {tb} was successful from {path}.")


# csv_to_postgres()

"""
https://www.youtube.com/watch?v=A7E18apPQJs
That is a video for adding a python path in windows 10. Fucking windows 10.
"""

"""
Object oriented programming in python
"""
class person:
    """Documentation for person

    """
    def __init__(self,name):
        super(person, self).__init__()
        self.name = name
p = person("Hank")
print(p.name)
        
        
