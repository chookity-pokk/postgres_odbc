import pyodbc
import time

start_time = time.time()

def connect_to_database():
    """
    This function will make a database, so I am not sure how useful
    it will be because I still need to understand what they want done
    with their database. Because if I can just make a server that will
    pull their inventory daily then I  won't need this.
    """
    cnxn = pyodbc.connect('DRIVER={PostgreSQL Unicode}; SERVER=localhost;DATABASE=testdb;UID=postgres;PWD=postgres')
    cursor = cnxn.cursor()
    cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    cnxn.setencoding(encoding='utf-8')
    return cnxn, cursor

# Specifying the ODBC driver, server name, database, etc. directly
#cnxn = pyodbc.connect(databasename='testdb',databaseIP='localhost',databaseport='5432',username='postgres',password='postgres')

#cnxn = pyodbc.connect('DRIVER={PostgreSQL Unicode};SERVER=localhost;DATABASE=testdb;UID=postgres;PWD=postgres')

# Using a DSN, but providing a password as well
#cnxn = pyodbc.connect('DSN=QuickBooks')
def function(x,y):
    print(x*y**2)
function(2,32)

# Create a cursor from the connection

#cursor = cnxn.cursor()

#cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
#cnxn.setencoding(encoding='utf-8')
#print("You have made it this far in {0} second. Good job,I guess. Set higher goals for yourself.".format(time.time()-start_time))

conn, cur = connect_to_database()
"""
This will create a table in the postgres database.
"""
def create_table(dbconnection, cursor, newtablename):
    sql = '''CREATE TABLE {0} (oid serial PRIMARY KEY)'''.format(newtablename)
    cursor.execute(sql)
    dbconnection.commit()
#create_table(conn, cur, 'DeleteMe')

"""
This will disconnect you from the database
"""
def disconnect_from_database(dbconnection, cursor):
    cursor.close()
    dbconnection.close()

"""
This is the main function, which is currently being used for testing purposes
because I will be calling the other functions within it to make sure I can connect,
disconnect and create tables in the postgres database. Fingers crossed. 7/28/2020, 4:16pm
Ayo, seems to be working just fine now that I editted it to make the table name an input.
Issue comes in when a table already exists with the name but that makes sense.
"""
def main():
    connect_to_database()
    tb = str(input("Input new table name: \n " ))
    create_table(conn, cur, tb)
    #The below line needs to be edited as it is trying to edit the rows of the
    #database but those rows don't currently exist so I need to make a function
    # to add rows to the database then have the line below edit those rows.
    cur.execute("insert into products(id, name) values (?,?)", 'pyodbc', 'awesome library')
    conn.close()
main()

#cur.execute("insert into products(id, name) values (?,?)", 'pyodbc', 'awesome library')
#cursor.commit()
print("Time to run function {0}. Could be faster though; I'm not impressed.".format(time.time()-start_time))
