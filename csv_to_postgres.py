import pandas as pd
import psycopg2
import os
"""
This now needs to be integrated into the larger tool.
"""
"""
UPDATE public.test29
	SET oid=?, id=?, names=?
	WHERE <condition>;
Go to PgAdmin and right click on a table and hit scripts and it will give a very
basic sample script such as the one above. Use the one above and it can update/edit
the current table.
"""


#Path to csv r'C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\testing.csv'
def connect_to_database(databasename='testdb', databaseIP='localhost', databaseport='5432', username='postgres',
                       password='postgres'):
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
    connection = psycopg2.connect(host=databaseIP, user=username, password=password, dbname=databasename)
    cursor = connection.cursor()
    return connection, cursor
conn, cur = connect_to_database()


path1 = r'C:\Users\Hank\Documents'
tb = 'test29'
path = os.path.join(path1,"Testing.csv")
print(os.path.exists(path))#This will return True or False depending on if the file exists
def csv_to_postgres():
    sql = f"""COPY {tb} FROM STDIN DELIMITER ',' CSV HEADER;"""
    with open(path) as f:
        cur.copy_expert(sql,f)
    conn.commit()
    print(f"Printing to {tb} was successful from {path}.")
csv_to_postgres()
"""
Just FINALLY fixed this, jeez this was an absolute hassel. 
"""

def blck_test():
    list = [ ]
    x =13
    while x <20 :
        x+= 1
        list.append(x)
        print(list)
    print(f"This is each added value to x: {list}")
#blck_test()
#The above function only exists so that I can test the blacken function in Emacs. 11:36 8/14/2020 STATUS: Not working
