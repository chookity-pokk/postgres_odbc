import pyodbc
import pandas as pd
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
tb = str(input("Input name of the table: \n " ))

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
    """
    This isn't working though the line that isn't calling sql but instead have it
    all within the 'execute()' function then it seems to be working.
    Maybe just adding in those functions into the execute function would
    fix the error. I will try that post lunch. 7/29/2020 2:38pm
    Jeez, this finally works now. 7/29/2020 2:43pm
    """
    #sql = "insert into {0}(id, names) values (?,?)".format(tablename)#, 'pyodbc', 'awesome library' #cnxn.commit()
    """
    I believe the line below will work a bit better and will change it to the
    default way soon enough but want to test it out first, just have to get
    rid of the 'pyodbc' and 'awesome library' and put that in my cursor.execute()
    section.
    It's been tested and is now the way to go as it will put the fieldnames in
    by default rather than having to put those values in now.
    """
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

"""
This is the main function, which is currently being used for testing purposes
because I will be calling the other functions within it to make sure I can connect,
disconnect and create tables in the postgres database. Fingers crossed. 7/28/2020, 4:16pm
Ayo, seems to be working just fine now that I editted it to make the table name an input.
Issue comes in when a table already exists with the name but that makes sense.
"""

def add_to_csv(cnxn, cursor, tb):
    """
    This function will take the contents of the table in PostgreSQL
    and put them to a csv. May be needed if peole want to externally save the
    contents of the database in a public place that people can easilt access
    i.e. pushing the csv to a public folder for the company to look at.
    """
    sql1 = """ SELECT * FROM {}""".format(tb)
    sql2 = """COPY {} to STDOUT WITH CSV HEADER""".format(tb)
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
#add_to_row(conn, cur, tb, fieldnames=fieldnames)
add_to_csv(conn, cur, tb)
"""
Commented out the main function because I believe the testing on this is all but
done. I added the line just below this one to get that one working and see if
it was also adding entries into the columns to see if that was working and
results were positive as it was able to add entries into the table.
"""
