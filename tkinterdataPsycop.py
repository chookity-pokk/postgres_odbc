from tkinter import *
import psycopg2
import pandas as pd
import tkinter.messagebox
from tkinter import scrolledtext
import os
from tkinter import filedialog

"""
8/7/2020
This is currently set up to connect to the same database but is using
psycopg2 instead of pyodbc because the syntax is easier to work with in psycopg2
and tkinter as apposed to pyodbc. If needed I can convert it to pyodbc without
a ton of challenges but I honesly don't want to. I have a similar script running
on pyodbc but the functionality isn't as good because it is more annoying to work with.
"""

"""
Make it so that the window closes after exporting or importing from the csv.
Currently the window stays open and I want it to close after submitting your
desired location.
"""

"""
This is now able to push stuff to the database
About freaking time. 3:44pm 8/4/2020
Added a bunch of new buttons but jeez, this is so damn frustrating
1:28pm 8/5/2020

Updating an entry in a database
UPDATE 'Bike Stuff' SET quantity = 5 WHERE 'part name' = 'Goodyear Bike Tire Model 123'
9:17am 8/6/2020

Make a function to clear the database as a whole

"""

# Connection modules
root = Tk()
root.title("G&D Chillers")
#This can be changed to any .ico files (use png or jpeg to ico converter online)
#It shows up in the top left corner of the display window.
# TODO: Needs to be added to all the windows.
root.iconbitmap(r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico")
root.geometry('400x400')
tb = 'guitable'
column_change = 'testing'
fieldnames=['first_name', 'last_name']
def connect_to_database(databasename='testdb', databaseIP='localhost', databaseport='5432', username='postgres',
                      password='postgres'):
   """Module takes arguments to connect to a PostgreSQL database using PostgreSQL and returns a connection.
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

def disconnect_from_db(dbconnection, cursor):
#closes connecttion to database
    cursor.close()
    dbconnection.close()

def add_to_row():
    answer = tkinter.messagebox.askquestion("G & D Chillers", 'Are you sure you want to commit data to database?')
    if answer == 'yes':
        cur.execute("INSERT INTO guitable (first_name, last_name) VALUES (%s, %s)", (f_name.get(), l_name.get()))
        f_name.delete(0,END)
        l_name.delete(0,END)
        conn.commit()
    else:
        pass



"""
I think that this needs to be editted in that edit_quant.get() is being called
but that is also calling the same functio. So I think what needs to be done
is something similar as to what is done for the add_csv function where the
function is within the same function itself.
Because if I manually add in an oid then it works just fine but added in the
edit_quant.get() call then we get an error. So for testing purposes I am going
to add in an oid manually and make sure the rest is working before fixing the initial
issue.
Lol, it is just calling itself and making more of the same window. I should have
seen that coming.
"""

def edit_quantity():
    editor = Tk()
    editor.title("Update a record")
    editor.geometry('400x400')
    record_id = "SELECT * FROM guitable WHERE oid = 10"#.format(str(edit_quant.get()))
    #sql = "SELECT * FROM guitable WHERE oid = {}".format(record_id)
    #cur.execute("SELECT * FROM guitable WHERE oid = " + record_id)
    cur.execute(record_id)
    records = cur.fetchall()
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
    #Loop through results and print them out.
    print_records = ''
    for record in records:
        # can change str(record) to str(record[0]) to get the first item and so on
        # Or so str(record[0]) + str(record[1]) to get the first two columns
        # \t puts a tab in, could be useful.
        print_records += str(record) + '\n'
    # ---------------Entry for database. create text boxes-------------------------
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0,column=1, padx=5)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1,column=1, padx=5)
    #can be changed to use for taking inventory out or putting it in
    edit_quant_editor = Entry(editor, width=30)
    edit_quant_editor.grid(row=2, column=1, padx=5)
    # ---------------Create text box label-----------------------------------------
    f_name_label = Label(editor, text="First Name", pady=1)
    f_name_label.grid(row=0,column=0)
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    edit_quant_label = Label(editor, text="ID number")
    edit_quant_label.grid(row=2, column=0)
    get_f = f_name.get()
    get_l = l_name.get()
    get_edit_quant = edit_quant.get()
    #----------Save Button-----------------------------------------------------
    edit = "Save Editted Record"
    edit_button = Button(editor, text=edit, command=edit_quantity)
    edit_button.grid(row=3, column=0,columnspan=2,pady=5,padx=5,ipadx=130)

    #sql = "UPDATE guitable SET first_name = %s, last_name = %s WHERE oid=1"
    """
    The below sql code will change multiple columns at once
    UPDATE guitable
    SET first_name = 'Test',
    last_name = 'Table'
    WHERE oid=1
    """
    #cur.execute(sql,(f_name.get(), l_name.get()))
    f_name.delete(0,END)
    l_name.delete(0,END)
    conn.commit()


def query():
    sql = "SELECT * FROM {}".format(tb)
    cur.execute(sql)
    records = cur.fetchall()
    #Loop through results and print them out.
    print_records = ''
    for record in records:
        # can change str(record) to str(record[0]) to get the first item and so on
        # Or so str(record[0]) + str(record[1]) to get the first two columns
        # \t puts a tab in, could be useful.
        print_records += str(record) + '\n'
    query_label = Label(root, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)
    conn.commit()

def delete():
    answer = tkinter.messagebox.askquestion("G & D Chillers", 'Are you sure you want to delete data to database?')
    if answer == 'yes':
        sql = "DELETE from guitable WHERE oid = {}".format(edit_quant.get())
        cur.execute(sql)
        f_name.delete(0,END)
        l_name.delete(0,END)
        edit_quant.delete(0,END)
        conn.commit()
    else:
        pass
def add_to_csv():

    def csv():
        sql1 = """ SELECT * FROM {}""".format(tb)
        rows = cur.execute(sql1)
        col_headers = [ i[0] for i in cur.description ]
        rows = [ list(i) for i in cur.fetchall()]
        df = pd.DataFrame(rows, columns=col_headers)
        path = r"C:\Users\Hank\Documents\Random Python Scripts\GUI and Tkinter\ "

        name = str(csv_name.get())+".csv"
        df.to_csv(path + name, index=False)
        csv_name.delete(0,END)
        tkinter.messagebox.showinfo("G&D Chillers", "Your data has been exported to "+ path+name)
    """
    This function will take the contents of the table in PostgreSQL
    and put them to a csv. May be needed if peole want to externally save the
    contents of the database in a public place that people can easily access
    i.e. pushing the csv to a public folder for the company to look at.
    """

    answer = tkinter.messagebox.askquestion("G & D Chillers", 'Are you sure you want to export data to a CSV?')

    if answer == 'yes':

        csv_imp = Tk()
        csv_imp.title("Update a record")
        csv_imp.geometry('300x300')
        csv_imp.iconbitmap(r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico")
        csv_lab = "Click here to export CSV file"
        csv_button = Button(csv_imp,text=csv_lab, command=save_file)
        csv_button.grid(row=3,column=3, columnspan=2, pady=5, padx=5, ipadx=66)
        """
        Can also add asksaveasfilename from tkinter which will also open the
        file manager so it will help to pick the location for the saved file.
        Looks like this needs to be changed below to instead have it so that it
        is just opening a file manager
        """
        #try:
        #    csv_add = Tk()
        #    csv_add.title("Update a record")
        #    csv_add.geometry('300x300')
        #    csv_add.iconbitmap(r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico")
        #    csv_name = Entry(csv_add, width=30)
        #    csv_name.grid(row=0,column=3, padx=5)
        #    added_csv_name = csv_name.get()
        #    csv_name_label = Label(csv_add, text="Add CSV Name", pady=1)
        #    csv_name_label.grid(row=2,column=3)
        #    csv_lab = "Print out to a CSV(Excel)"
            #path = r"C:\Users\Hank\Documents\Random Python Scripts\GUI and Tkinter\ "+csv_name.get()+".csv"
            #added_csv_name = csv_name.get()
        #    csv_button = Button(csv_add,text=csv_lab, command=csv)
        #    csv_button.grid(row=3,column=3, columnspan=2, pady=5, padx=5, ipadx=66)
        #except:
        """
        Obviously change the error message here. We don't want this going straight to Tim
        and honestly who knows if I even want my email attached to this or if
        it is even going to get implemented. ¯\_(ツ)_/¯
        """
        #    words = "If this continues please contact hank@gdchillers.com"
        #    tkinter.messagebox.showinfo("G&D Chillers", f"There was an error downloading the csv. " + words)


    else:
        pass

def csv_add_button():
    answer = tkinter.messagebox.askquestion("G & D Chillers", 'Are you sure you want to export data to a CSV?')


#Adds the option to push a csv into the database.
def csv_to_postgres():
    answer = tkinter.messagebox.askquestion("G & D Chillers", 'Are you sure you want to import data from a CSV?')
    if answer == 'yes':
        csv_imp = Tk()
        csv_imp.title("Update a record")
        csv_imp.geometry('300x300')
        csv_imp.iconbitmap(r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico")
        csv_lab = "Click here to import CSV file"
        csv_button = Button(csv_imp,text=csv_lab, command=file_opener)
        csv_button.grid(row=3,column=3, columnspan=2, pady=5, padx=5, ipadx=66)
#csv_to_postgres()


def file_opener():
    #This is connected to csv_to_postgres
    #https://www.tutorialspoint.com/askopenfile-function-in-python-tkinter
    input = filedialog.askopenfile(initialdir='/', filetypes=[('CSV', '*.csv')])
    path1 = r'C:\Users\Hank\Documents'
    tb = 'test29'
    try:
        sql = f"""COPY {tb} FROM STDIN DELIMITER ',' CSV HEADER;"""
        with open(input.name) as f:
            cur.copy_expert(sql,f)
        conn.commit()
        tkinter.messagebox.showinfo("G&D Chillers", f"Your data has been imported from {input.name}")
    except:
        """
        Obviously change the error message here. We don't want this going straight to Tim
        and honestly who knows if I even want my email attached to this or if
        it is even going to get implemented. ¯\_(ツ)_/¯
        """
        words = "It is likely because it doesn't have the same column names. Please check and if you can't resolve the issue email timh@gdchillers.com"
        tkinter.messagebox.showinfo("G&D Chillers", f"There was an error uploading {input.name}." + words)
        """
        Put in a box to close the window
        """
def save_file():
    #This is connected to add_to_csv
    #https://www.tutorialspoint.com/asksaveasfile-function-in-python-tkinter
    input = filedialog.asksaveasfilename(initialdir='/', filetypes=[('CSV', '*.csv')])
    try:
        sql1 = """ SELECT * FROM {}""".format(tb)
        rows = cur.execute(sql1)
        col_headers = [ i[0] for i in cur.description ]
        rows = [ list(i) for i in cur.fetchall()]
        df = pd.DataFrame(rows, columns=col_headers)
        """
        The two df.to_csv seem to either be working or not depending on how it is
        feeling because it was working then I did something then it wasn't working
        so I reverted back to the first df.to_csv (which I am not using because it is
        requiring that '.csv' is added into it). After using that a few times though I
        went and tried the second df.to_csv and it was magically working again.
        They are both currently working but who knows how long that'll last.
        Fucking tkinter doing me dirty.
        """
        #df.to_csv(input, index=False)
        df.to_csv(input+".csv", index=False)
        tkinter.messagebox.showinfo("G&D Chillers", f"Your data has been exported to {input}")
    except:
        words = "If this continues please email hank@gdchillers.com"
        tkinter.messagebox.showinfo("G&D Chillers", f"There was an error downloading {input}.csv" + words)

# ---------------Entry for database. create text boxes-------------------------
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=5)

l_name = Entry(root, width=30)
l_name.grid(row=1,column=1, padx=5)

#can be changed to use for taking inventory out or putting it in
edit_quant = Entry(root, width=30)
edit_quant.grid(row=2, column=1, padx=5)

# ---------------Create text box label-----------------------------------------
f_name_label = Label(root, text="First Name", pady=1)
f_name_label.grid(row=0,column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

edit_quant_label = Label(root, text="ID number")
edit_quant_label.grid(row=2, column=0)

get_f = f_name.get()
get_l = l_name.get()
get_edit_quant = edit_quant.get()

# -------------Create buttons to submit data------------------------------------
#Submits data to the database then clears the data.
sub = "Add record to database"
submit_button = Button(root,text=sub, command=add_to_row)
submit_button.grid(row=6,column=0, columnspan=2, pady=5,padx=5, ipadx=100)

# ----------------------Creat query button--------------------------------------
#This will show all the records in the database, probably not useful.
que = "See records"
que_button = Button(root, text=que, command=query)
que_button.grid(row=8, column=0,columnspan=2,pady=5,padx=5,ipadx=131)

#---------------------Edit quantity button--------------------------------------
edit = "Edit Record"
edit_button = Button(root, text=edit, command=edit_quantity)
edit_button.grid(row=10, column=0,columnspan=2,pady=5,padx=5,ipadx=130)

#-------------------Create buttons to delete data-------------------------------
"""
Make a window pop up saying that the data will be deleted and are you sure?
"""
erase = "Delete record from database"
del_button = Button(root,text=erase, command=delete)
del_button.grid(row=11,column=0, columnspan=2, pady=5,padx=5, ipadx=85)


# ----------------Print out CSV button------------------------------------------
"""
When you print out to CSV make a window pop up saying that
the data has successfully been exported to a csv.
"""
csv_lab = "Print out to a CSV(Excel)"
csv_button = Button(root,text=csv_lab, command=add_to_csv)
csv_button.grid(row=7,column=0, columnspan=2, pady=5, padx=5, ipadx=97.5)

# -------------Create buttons to add csv data------------------------------------
#Submits data to the database then clears the data.
imp = "Import csv record to database"
submit_button = Button(root,text=imp, command=csv_to_postgres)
submit_button.grid(row=12,column=0, columnspan=2, pady=5,padx=5, ipadx=83)


# ------------------------Canvas------------------------------------------------
canvas = Canvas(root)


# -----------------Scroll Bar---------------------------------------------------
ybar = Scrollbar(root, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=ybar.set)
ybar.grid(row=1,column=5, sticky="ns")

resize = Label(root)
resize.grid(row=1, column=2,sticky='nsew')


#This will make it so the window can't be resized. Might be worth doing if I
# Can't figure out how to make it change dynamically with grid.
root.resizable(0,0)
root.mainloop()
