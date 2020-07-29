import pyodbc
import time
"""
at some point I will switch all 'dbconnection.commit()' to
cnxn.commit() because I think that should be the proper syntax though
'dbconnection.commit()' seems to be working just fine. So who knows.
"""


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
#This will need to be adjusted for QuickBooks, I'll add a link when I find one
#cnxn = pyodbc.connect('DSN=QuickBooks')


# Create a cursor from the connection

#cursor = cnxn.cursor()

#cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
#cnxn.setencoding(encoding='utf-8')
#print("You have made it this far in {0} second. Good job,I guess. Set higher goals for yourself.".format(time.time()-start_time))

conn, cur = connect_to_database()
"""
This will create a table in the postgres database.
"""
#changing newtablename to tb... I'll fix that later
def create_table(dbconnection, cursor, tb):
    sql = '''CREATE TABLE {0} (oid serial PRIMARY KEY)'''.format(tb)
    cursor.execute(sql)
    dbconnection.commit()
#create_table(conn, cur, 'DeleteMe')

"""
Takes the connection to the database and adds a new field information and updates the
table with a new field.
"""
def add_field(dbconnection, cursor, tablename, fieldname='newfield',fieldtype='TEXT'):
    sql = '''ALTER TABLE {0} ADD COLUMN {1} {2}'''.format(tablename, fieldname, fieldtype)
    cursor.execute(sql)
    dbconnection.commit()

def add_to_row(dbconnection, cursor, tablename,fieldnames):
    #sql = '''INSERT INTO {}(id,names) values(?,?)'''.format(tablename),'pyodbc','el biblioteca'
    #sql = "insert into {}(id, names) values (?,?)".format(tablename), 'pyodbc', 'awesome library'
    #cursor.execute(sql)
    """
    This isn't working though the line that isn't calling sql but instead have it
    all within the 'execute()' function then it seems to be working.
    Maybe just adding in those functions into the execute function would
    fix the error. I will try that post lunch. 7/29/2020 2:38

    """
    sql = "insert into {0}(id, names) values (?,?)".format(tablename)#, 'pyodbc', 'awesome library' #cnxn.commit()
    #sql = '''INSERT INTO {0}({1},{2}) VALUES (?,?)'''.format(tablename,fieldnames[0],fieldnames[1]), 'pyodbc', 'awesome library'
    cursor.execute(sql, 'pyodbc', 'awesome library')
    #So this seems to work below here but above here is having a problem. It is literally
    #the same exact thing so I don't know what the hold up is.
    #cur.execute("insert into {}(id, names) values (?,?)".format(tb), 'pyodbc', 'awesome library')
    dbconnection.commit()
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
    #This will be changed to the name of the columns
    fieldnames = ['id', 'names']
    #The below line needs to be edited as it is trying to edit the rows of the
    #database but those rows don't currently exist so I need to make a function
    # to add rows to the database then have the line below edit those rows.
    #cur.execute("insert into products(id, name) values (?,?)", 'pyodbc', 'awesome library')
    for name in fieldnames:
        #Going to need to change 'papers' to whatever the inventory table is called
        add_field(conn, cur, tb, fieldname=name, fieldtype='TEXT')
    #cur.execute("insert into {}(id, names) values (?,?)".format(tb), 'pyodbc', 'awesome library')
    add_to_row(conn, cur, tb,fieldnames=fieldnames)
    conn.close()
main()

#cur.execute("insert into products(id, name) values (?,?)", 'pyodbc', 'awesome library')
#cursor.commit()
print("Time to run function {0}. Could be faster though; I'm not impressed.".format(time.time()-start_time))
