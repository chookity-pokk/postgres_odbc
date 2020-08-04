import pyodbc
import pandas as pd
import argparse
"""
At some point I will switch all 'dbconnection.commit()' to
cnxn.commit() because I think that should be the proper syntax though
'dbconnection.commit()' seems to be working just fine. So who knows.
Will also add better comments and clean up the code as it is currently a bit messy
7/29/2020 3:15pm
"""


def connect_to_database():
    """
    This function will make a database, so I am not sure how useful
    it will be because I still need to understand what they want done
    with their database. Because if I can just make a server that will
    pull their inventory daily then I  won't need this.
    """
    #You have to put in the exact driver name here.
    #UID is username and PWD is the password
    cnxn = pyodbc.connect('DRIVER={PostgreSQL Unicode}; SERVER=localhost;DATABASE=testdb;UID=postgres;PWD=postgres')
    cursor = cnxn.cursor()
    cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    cnxn.setencoding(encoding='utf-8')
    return cnxn, cursor

# Specifying the ODBC driver, server name, database, etc. directly
"""
Using a DSN, but providing a password as well
This will need to be adjusted for QuickBooks, I'll add a link when I find one
https://code.google.com/archive/p/pyodbc/wikis/ConnectionStrings.wiki
https://doc.4d.com/4Dv17/4D/17/Using-a-connection-string.200-3786162.en.html
https://groups.google.com/forum/#!msg/sqlalchemy/N892Ab1kpSA/fEIazjSf-S4J
I believe what I have now is good enough with the password and the
UID (user ID, basically your username) needing to be changed when that all
gets sorted out.
"""
#cnxn = pyodbc.connect('DSN=QuickBooks;UID=Admin;PWD=InsertPassword')

conn, cur = connect_to_database()
#The fieldnames will either have to be changed or may even not need to be included
#as I may not be needing to name the columns depending on the structure of the table
fieldnames = ['id', 'names']
#tb = str(input("Input name of the table: \n " ))

#changing newtablename to tb... I'll fix that later
def create_table(cnxn, cursor, tb):
    """
    This will create a table in the postgres database.
    """
    sql = '''CREATE TABLE {0} (oid serial PRIMARY KEY)'''.format(tb)
    cursor.execute(sql)
    cnxn.commit()


def add_field(cnxn, cursor, tablename, fieldname='newfield',fieldtype='TEXT'):
    """
    Takes the connection to the database and adds a new field information and updates the
    table with a new field.
    """
    sql = '''ALTER TABLE {0} ADD COLUMN {1} {2}'''.format(tablename, fieldname, fieldtype)
    cursor.execute(sql)
    cnxn.commit()

def add_to_row(cnxn, cursor, tablename,fieldnames):
    sql = '''INSERT INTO {0}({1},{2}) VALUES (?,?)'''.format(tablename,fieldnames[0],fieldnames[1])
    cursor.execute(sql, 'Python Stuff', 'Named Entry')
    """
    pyodbc and awesome library(values from the line above) are currently just
    filler lines to put entrees into the table to make sure this function was
    working. Those will be changed when needed.
    """
    cnxn.commit()


def disconnect_from_database(cnxn, cursor):
    """
    This will disconnect you from the database though also running conn.close()
    will also do the same thing so either one works. I'm just keeping this in
    incase someone wants to work with this later.
    """
    cursor.close()
    cnxn.close()

def add_to_csv(cnxn, cursor, tb):
    """
    This function will take the contents of the table in PostgreSQL
    and put them to a csv. May be needed if peole want to externally save the
    contents of the database in a public place that people can easilt access
    i.e. pushing the csv to a public folder for the company to look at.
    """
    sql1 = """ SELECT * FROM {}""".format(tb)
    #sql2 = """COPY {} to STDOUT WITH CSV HEADER""".format(tb)
    rows = cursor.execute(sql1)

    #This will obviously need to be editted to a company path as apposed to a personal folder
    #Also, boo having to use Windows. smh.
    #Need to add a section to make the csv in the first place
    #path1 = "C:\\Users\\Hank\\Documents\\Testin\\Testing.csv"
    #pd.DataFrame(path1,index=False)
    #with open(path1, 'wb') as csvfile:
    #    filewriter = csv.writer(csvfile, delimiter=',')
    #This is currently working and writing the table to the csv.
    col_headers = [ i[0] for i in cursor.description ]
    rows = [ list(i) for i in cursor.fetchall()]
    df = pd.DataFrame(rows, columns=col_headers)
    #Boo, Windows path... :'(
    path = r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\testing.csv"
    df.to_csv(path, index=False)

    """
    path = "C:\\Users\\Hank\\Documents\\Testin\\test.csv"
    with open(path, "w", newline='') as output:
        writer = csv.writer(output)
        writer.writerows([x[0] for x in cursor.description])
        for row in rows:
            writer.writerows(row)
        #cnxn.cursor().copy_expert(cursor.execute(sql), output)
    cnxn.commit()
    """
"""
Notes on how to implement into QuickBooks. Seems like anything with '_line_inv'
at the end of it is an inventory item. Check out the pdf sent by time on 7/29/2020
if confused. (Add a link to pdf when available for future reference).
_inv_adjust is inventory adjustments
Honestly may have been able to just connect it through Microsoft Access. If that
is the case then I may just write a much smaller script to launch that and
have it pull the inventory daily. Page 17 of the report.
The pdf is very helpful but also is mostly for getting access through Excel
or Access.
"""
"""
def main():
    connect_to_database()
    tb = str(input("Input new table name: \n " ))
    create_table(conn, cur, tb)
    #This will be changed to the name of the columns
    fieldnames = ['id', 'names']
    for name in fieldnames:
        #Going to need to change 'papers' to whatever the inventory table is called
        add_field(conn, cur, tb, fieldname=name, fieldtype='TEXT')
    add_to_row(conn, cur, tb,fieldnames=fieldnames)
    add_to_csv(conn, cur, tb)
    conn.close()
#main()
"""
#add_to_row(conn, cur, tb, fieldnames=fieldnames)
#add_to_csv(conn, cur, tb)

def printl(cnxn, cursor,tb):
    """
    This will print out the contents of the 'sql1' query. In this context it will
    print out everything that is in the tablename entered. Or everything that is
    within the oid (object ID) range that I put in. This could potentiall be useful
    for testing smaller datasets as it will print out the contents of the table
    after I have written to the table so that I can immediately see if the script
    is working rather than have to check pgadmin every time. Could be useless for
    some and the print out definitely isn't pretty.
    """
    sql1 = """ SELECT * FROM {} WHERE oid < 10 AND oid > 4""".format(tb)
    #sql2 = """COPY {} to STDOUT WITH CSV HEADER""".format(tb)
    rows = cursor.execute(sql1)
    col_headers = [ i[0] for i in cursor.description ]
    rows = [ list(i) for i in cursor.fetchall()]
    print(rows)
#printl(conn, cur, tb)
"""
parser = argparse.ArgumentParser()
parser.add_argument('--db'. dest='Table',choices=['test29','NewTestTable'],
                    help='Pick table name here')
args = parser.parse_args()
fmt = args.Table
"""

"""
Below is an command line argument parser. What this will do is give you the
option to choose which table to pick when this is run from the command line.
so you would go to your directory that this is downloaded at, maybe something
like /home/username/git/postgres-odbc/(linux) and enter
'python postgres_odbc.py --db 'tablename'' where 'tablename' is the name of the
table that you are wanting to write to in your postgres database.
If you don't want to run it like that then you can just go to the bottom and
uncomment out 'main()' and you'll be able to run it just fine like that. 
"""
parse = argparse.ArgumentParser()
# choices limits argument values to the
# given list
parse.add_argument('--db',dest='Table', choices=['test29', 'newtesttable'],
                   help='Pick table name here')

args = parse.parse_args()
fmt = args.Table
if fmt == 'test29':
    def main():
        connect_to_database()
        tb = str(input("Input new table name: \n " ))
        tb = 'test29'
        create_table(conn, cur, tb)
        #This will be changed to the name of the columns
        fieldnames = ['id', 'names']
        for name in fieldnames:
            #Going to need to change 'papers' to whatever the inventory table is called
            add_field(conn, cur, tb, fieldname=name, fieldtype='TEXT')
        add_to_row(conn, cur, tb,fieldnames=fieldnames)
        add_to_csv(conn, cur, tb)
        printl(conn, cur, tb)
        conn.close()
    #main()
if fmt == 'NewTestTable':
    def main():
        connect_to_database()
        tb = str(input("Input new table name: \n " ))
        tb = 'NewTestTable'
        create_table(conn, cur, tb)
        #This will be changed to the name of the columns
        fieldnames = ['id', 'names']
        for name in fieldnames:
            #Going to need to change 'papers' to whatever the inventory table is called
            add_field(conn, cur, tb, fieldname=name, fieldtype='TEXT')
        add_to_row(conn, cur, tb,fieldnames=fieldnames)
        add_to_csv(conn, cur, tb)
        printl(conn, cur, tb)
        conn.close()
    #main()

def main():
    connect_to_database()
    tb = str(input("Input new table name: \n " ))
    create_table(conn, cur, tb)
    #This will be changed to the name of the columns
    fieldnames = ['id', 'names']
    for name in fieldnames:
        #Going to need to change 'papers' to whatever the inventory table is called
        add_field(conn, cur, tb, fieldname=name, fieldtype='TEXT')
    add_to_row(conn, cur, tb,fieldnames=fieldnames)
    add_to_csv(conn, cur, tb)
    printl(conn, cur, tb)
    conn.close()
#main()
