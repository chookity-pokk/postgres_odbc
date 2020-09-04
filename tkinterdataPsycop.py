from tkinter import *
import psycopg2
import pandas as pd
import tkinter.messagebox
from tkinter import scrolledtext
import os
from tkinter import filedialog

"""
dyanically changing oid:
This won't work as an oid is a primary key so it can not be changed.
Though there can be up to 2^32 -1 oid's so there is plenty of room
to space them out to make room for them to be inserted at a later time.
Though I do need to look into having the database ordered alphabetically.
Or rather look into organizing them before storing into the database.
"""


"""
8/7/2020
This is currently set up to connect to the same database but is using
psycopg2 instead of pyodbc because the syntax is easier to work with in psycopg2
and tkinter as apposed to pyodbc. If needed I can convert it to pyodbc without
a ton of challenges but I honesly don't want to. I have a similar script running
on pyodbc but the functionality isn't as good because it is more annoying to work with.
"""

# Connection modules
root = Tk()
root.title("G&D Chillers")
root.iconbitmap(
    r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
)
root.geometry("800x500")
tb = "invtest5"
column_change = "testing"  # These can also probably be deleted
fieldnames = ["first_name", "last_name"]  # These can also probably be deleted


def connect_to_database(
    databasename="testdb",
    databaseIP="localhost",
    databaseport="5432",
    username="postgres",
    password="postgres",
):
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
    connection = psycopg2.connect(
        host=databaseIP, user=username, password=password, dbname=databasename
    )
    cursor = connection.cursor()
    return connection, cursor


conn, cur = connect_to_database()


def disconnect_from_db(dbconnection, cursor):
    # closes connecttion to database
    cursor.close()
    dbconnection.close()


def add_to_row():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to commit data to database?"
    )
    if answer == "yes":
        cur.execute(
            "INSERT INTO guitable (first_name, last_name) VALUES (%s, %s)",
            (f_name.get(), l_name.get()),
        )
        f_name.delete(0, END)
        l_name.delete(0, END)
        conn.commit()
    else:
        pass

#This as well
def editdb():
    try:
        # record_id = "SELECT * FROM guitable WHERE oid=10"
        # cur.execute(record_id)
        # records = cur.fetchall()
        # for record in records:
        #    f_name_editor.insert(0, record[0])
        #    l_name_editor.insert(0, record[1])
        # print_records = ''
        # for record in records:
        #    print_records += str(record) + '\n'
        """
        the code in this comment chunk should auto complete the existing data in
        the database.
        cur.execute(f"SELECT * FROM {tb} WHERE oid={input_value}")
        records = cur.fetchall()
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            oid_number.insert(0, record[2])
        """
        print("this is also working")
        sql = f"UPDATE guitable SET first_name='{f_name_editor.get()}', last_name='{l_name_editor.get()}' WHERE oid={edit_oid.get()}"
        print(sql)
        # Just want to leave this in here to shame it. Using a dictionary for every query is fucking stupid.
        # cur.execute("""UPDATE guitable SET
        # first_name = :first,
        # last_name = :last
        # WHERE oid = 47
        # """,
        # {
        #'first':f_name_editor.get(),
        #'last':l_name_editor.get()
        # }
        # )
        # This whole setup in code above here is the same thing as my 'sql' line. One is a good coding practice and the other isn't.
        print("Working again")
        cur.execute(sql)
        print("Still working")
        conn.commit()
        editor.destroy()
        print("Mission accomplished!")
    except:
        tkinter.messagebox.showinfo(
            "G&D Chillers",
            "You were unable to edit records. Make sure you have values for all the text boxes.",
        )

#This needs to be editted so it can handle all of the variables
def editing():
    print("This is working")
    global editor
    editor = Tk()
    editor.title("Update Record")
    editor.geometry("400x400")
    editor.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    # ------------------Entry for Database ------------------------------------
    global f_name_editor
    global l_name_editor
    global edit_oid
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=5)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=5)
    edit_oid = Entry(editor, width=30)
    edit_oid.grid(row=2, column=1, padx=5)
    # ------------------Create text box labels----------------------------------
    f_name_label = Label(editor, text="First Name", pady=1)
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(editor, text="Last Name", pady=1)
    l_name_label.grid(row=1, column=0)
    edit_oid_label = Label(editor, text="Insert OID", pady=1)
    edit_oid_label.grid(row=2, column=0)
    global get_f
    global get_l
    get_f = f_name_editor.get()
    get_l = l_name_editor.get()
    # -------------------Save button--------------------------------------------
    edit = "Save Editted Record"
    edit_button = Button(editor, text=edit, command=editdb)
    edit_button.grid(row=3, column=0, columnspan=2, pady=5, padx=5, ipadx=130)


def query():
    sql = "SELECT * FROM {}".format(tb)
    cur.execute(sql)
    records = cur.fetchall()
    # Loop through results and print them out.
    print_records = ""
    for record in records:
        # can change str(record) to str(record[0]) to get the first item and so on
        # Or so str(record[0]) + str(record[1]) to get the first two columns
        # \t puts a tab in, could be useful.
        print_records += str(record) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)
    conn.commit()


def delete():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to delete data to database?"
    )
    if answer == "yes":
        sql = "DELETE from guitable WHERE oid = {}".format(edit_quant.get())
        cur.execute(sql)
        f_name.delete(0, END)
        l_name.delete(0, END)
        edit_quant.delete(0, END)
        conn.commit()
    else:
        pass


def add_to_csv():
    """
    This function will take the contents of the table in PostgreSQL
    and put them to a csv. May be needed if peole want to externally save the
    contents of the database in a public place that people can easily access
    i.e. pushing the csv to a public folder for the company to look at.
    """
    global csv_exp
    csv_exp = Tk()
    csv_exp.title("Update a record")
    csv_exp.geometry("300x300")
    csv_exp.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    csv_lab = "Click here to export CSV file"
    csv_button = Button(csv_exp, text=csv_lab, command=save_file)
    csv_button.grid(row=3, column=3, columnspan=2, pady=5, padx=5, ipadx=66)


def csv_add_button():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to export data to a CSV?"
    )


# Adds the option to push a csv into the database.
def csv_to_postgres():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to import data from a CSV?"
    )
    if answer == "yes":
        global csv_imp
        csv_imp = Tk()
        csv_imp.title("Update a record")
        csv_imp.geometry("300x300")
        csv_imp.iconbitmap(
            r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
        )
        csv_lab = "Click here to import CSV file"
        csv_button = Button(csv_imp, text=csv_lab, command=file_opener)
        csv_button.grid(row=3, column=3, columnspan=2, pady=5, padx=5, ipadx=66)


# csv_to_postgres()


def file_opener():
    # This is connected to csv_to_postgres
    # https://www.tutorialspoint.com/askopenfile-function-in-python-tkinter
    input = filedialog.askopenfile(
        initialdir="/", filetypes=[("CSV", "*.csv"), ("XLSX", "*.xlsx")]
    )
    tb = "invtest5"
    try:
        sql = f"""COPY {tb} FROM STDIN DELIMITER ',' CSV HEADER;"""
        with open(input.name) as f:
            cur.copy_expert(sql, f)
        conn.commit()
        tkinter.messagebox.showinfo(
            "G&D Chillers", f"Your data has been imported from {input.name} to {tb}."
        )
    except:
        """
        Obviously change the error message here. We don't want this going straight to Tim
        and honestly who knows if I even want my email attached to this or if
        it is even going to get implemented. ¯\_(ツ)_/¯
        """
        words = """It is likely because it doesn't have the same column names.
        Please check and if you can't resolve the issue email hank@gdchillers.com"""
        tkinter.messagebox.showinfo(
            "G&D Chillers", f"There was an error uploading {input.name}. {words}"
        )

    # finally:
    #    csv_imp.destroy()


def save_file():
    # This is connected to add_to_csv
    # https://www.tutorialspoint.com/asksaveasfile-function-in-python-tkinter
    input = filedialog.asksaveasfilename(initialdir="/", filetypes=[("CSV", "*.csv")])
    try:
        sql1 = """ SELECT * FROM {}""".format(tb)
        rows = cur.execute(sql1)
        col_headers = [i[0] for i in cur.description]
        rows = [list(i) for i in cur.fetchall()]
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
        # df.to_csv(input, index=False)
        df.to_csv(input + ".csv", index=False)
        tkinter.messagebox.showinfo(
            "G&D Chillers", f"Your data has been exported to {input}"
        )
    except:
        words = " If this continues please email hank@gdchillers.com"
        tkinter.messagebox.showinfo(
            "G&D Chillers", f"There was an error downloading {input}.csv" + words
        )
    # finally:
    #     csv_exp.destroy()


"""
This function probably needs a button to save as a xlsx
that will take the database, convert it into a csv then
convert that csv into a xlsx file. Postgres doesn't natively
allow exporting a xlsx file so it has to be pulled out
as a csv and then converted into the xlsx.

This is now supported by having it save the CSV then ask
if the user would like to convert it to a csv as well.
"""


def csv_2_xlsx():
    input = filedialog.asksaveasfilename(initialdir="/", filetypes=[("CSV", "*.csv")])
    try:
        from openpyxl import Workbook
        import csv

        tb = "invtest5"
        sql1 = """ SELECT * FROM {}""".format(tb)
        rows = cur.execute(sql1)
        col_headers = [i[0] for i in cur.description]
        rows = [list(i) for i in cur.fetchall()]
        df = pd.DataFrame(rows, columns=col_headers)
        print("Working step 1")
        df.to_csv(input + ".csv", index=False)
        print(f"{input}")
        tkinter.messagebox.showinfo("G&D Chillers", f"Your CSV was saved at {input}")
        ans = tkinter.messagebox.askquestion(
            "G&D Chillers", "Would you like to convert the CSV to xlsx?"
        )
        if ans == "yes":
            print(f"{input}")
            wb = Workbook()
            ws = wb.active
            path = input + ".csv"
            print("Working Step 2")
            with open(path, "r") as f:
                for row in csv.reader(f):
                    ws.append(row)
            print("Working Step 3")
            xlsx_path = input + ".xlsx"
            wb.save(xlsx_path)
            print(f"Your csv has been converted to an xlsx and stored {xlsx_path}")
            tkinter.messagebox.showinfo(
                "G&D Chillers", f"Your xlsx was saved at {xlsx_path}"
            )
    except:
        tkinter.messagebox.showinfo(
            "G&D Chillers",
            f"You were unable to save your file {input}, {input}. If this issue continues please email hank@gdchillers.com",
        )


# csv_2_xlsx()

# ----------------Testing proper entries for DB ------------------------------
"""
There are 33 entries here so the only way to make it even is 3 rows of 11.
"""

model = Entry(root, width=30)
model.grid(row=0, column=1, padx=5)

dimensions = Entry(root, width=30)
dimensions.grid(row=1, column=1, padx=5)

frame = Entry(root, width=30)
frame.grid(row=2, column=1, padx=5)

housing = Entry(root, width=30)
housing.grid(row=3, column=1, padx=5)

tank_size = Entry(root, width=30)
tank_size.grid(row=4, column=1, padx=5)

tank_mat = Entry(root, width=30)
tank_mat.grid(row=5, column=1, padx=5)

compressor_hp = Entry(root, width=30)
compressor_hp.grid(row=6, column=1, padx=5)

condenser = Entry(root, width=30)
condenser.grid(row=7, column=1, padx=5)

process_pump_hp = Entry(root, width=30)
process_pump_hp.grid(row=8, column=1, padx=5)

gpm_at_25psi = Entry(root, width=30)
gpm_at_25psi.grid(row=9, column=1, padx=5)

weight = Entry(root, width=30)
weight.grid(row=10, column=1, padx=5)

conn_size = Entry(root, width=30)
conn_size.grid(row=11, column=1, padx=5)

conn_type = Entry(root, width=30)
conn_type.grid(row=12, column=1, padx=5)

chiller_pump_hp = Entry(root, width=30)
chiller_pump_hp.grid(row=13, column=1, padx=5)

shipping_weight = Entry(root, width=30)
shipping_weight.grid(row=14, column=1, padx=5)

heat_exchanger = Entry(root, width=30)
heat_exchanger.grid(row=15, column=1, padx=5)

controls = Entry(root, width=30)
controls.grid(row=0, column=3, padx=5)

electrical_enclosure = Entry(root, width=30)
electrical_enclosure.grid(row=1, column=3, padx=5)

shipping_weight = Entry(root, width=30)
shipping_weight.grid(row=2, column=3, padx=5)

decibals_at_10_feet = Entry(root, width=30)
decibals_at_10_feet.grid(row=3, column=3, padx=5)

refrigerant = Entry(root, width=30)
refrigerant.grid(row=4, column=3, padx=5)

_230_1_FLA = Entry(root, width=30)
_230_1_FLA.grid(row=5, column=3, padx=5)

_230_1_MCA = Entry(root, width=30)
_230_1_MCA.grid(row=6, column=3, padx=5)

_230_1_MCO = Entry(root, width=30)
_230_1_MCO.grid(row=7, column=3, padx=5)

_230_3_FLA = Entry(root, width=30)
_230_3_FLA.grid(row=8, column=3, padx=5)

_230_3_MCA = Entry(root, width=30)
_230_3_MCA.grid(row=9, column=3, padx=5)

_230_3_MCO = Entry(root, width=30)
_230_3_MCO.grid(row=10, column=3, padx=5)

_460_3_FLA = Entry(root, width=30)
_460_3_FLA.grid(row=11, column=3, padx=5)

_460_3_MCA = Entry(root, width=30)
_460_3_MCA.grid(row=12, column=3, padx=5)

_460_3_MCO = Entry(root, width=30)
_460_3_MCO.grid(row=13, column=3, padx=5)

_20F = Entry(root, width=30)
_20F.grid(row=14, column=3, padx=5)

_30F = Entry(root, width=30)
_30F.grid(row=15, column=3, padx=5)

_40F = Entry(root, width=30)
_40F.grid(row=16, column=3, padx=5)


# ------------------Test Proper Entries for the database (text boxes) --------------------
model_label = Label(root, text="Model Name", pady=1)
model_label.grid(row=0, column=0)

dimensions_label = Label(root, text="Dimensions", pady=1)
dimensions_label.grid(row=1, column=0)

frame_label = Label(root, text="Frame", pady=1)
frame_label.grid(row=2, column=0)

housing_label = Label(root, text="Housing", pady=1)
housing_label.grid(row=3, column=0)

tank_size_label = Label(root, text="Tank Size", pady=1)
tank_size_label.grid(row=4, column=0)

tank_mat_label = Label(root, text="TankMat", pady=1)
tank_mat_label.grid(row=5, column=0)

compressor_hp_label = Label(root, text="Compressor HP", pady=1)
compressor_hp_label.grid(row=6, column=0)

condenser_label = Label(root, text="Condenser", pady=1)
condenser_label.grid(row=7, column=0)

process_pump_hp_label = Label(root, text="Process Pump HP", pady=1)
process_pump_hp_label.grid(row=8, column=0)

gpm_at_25psi_label = Label(root, text="GPM at 25 PSI", pady=1)
gpm_at_25psi_label.grid(row=9, column=0)

weight_label = Label(root, text="Weight", pady=1)
weight_label.grid(row=10, column=0)

conn_size_label = Label(root, text="ConnSize", pady=1)
conn_size_label.grid(row=11, column=0)

conn_type_label = Label(root, text="ConnType", pady=1)
conn_type_label.grid(row=12, column=0)

connection_size_label = Label(root, text="Connection Size", pady=1)
connection_size_label.grid(row=13, column=0)

chiller_pump_hp_label = Label(root, text="Chiller Pump HP", pady=1)
chiller_pump_hp_label.grid(row=14, column=0)
# From here I want to split the window. Either that or at 16 becuase it'll split it in half, or maybe thirds.

heat_exchanger_label = Label(root, text="Heat Exchanger", pady=1)
heat_exchanger_label.grid(row=15, column=0)

controls_label = Label(root, text="Controls", pady=1)
controls_label.grid(row=0, column=2)

electrical_enclosure_label = Label(root, text="Electrical Enlcosure", pady=1)
electrical_enclosure_label.grid(row=1, column=2)

shipping_weight_label = Label(root, text="Shipping Weight", pady=1)
shipping_weight_label.grid(row=2, column=2)

decibals_at_10_feet_label = Label(root, text="Decibals at 10 feet", pady=1)
decibals_at_10_feet_label.grid(row=3, column=2)

refrigerant_label = Label(root, text="Refrigerant", pady=1)
refrigerant_label.grid(row=4, column=2)

_230_1_FLA_label = Label(root, text="230-1-FLA", pady=1)
_230_1_FLA_label.grid(row=5, column=2)

_230_1_MCA_label = Label(root, text="230-1-MCA", pady=1)
_230_1_MCA_label.grid(row=6, column=2)

_230_1_MCO_label = Label(root, text="230-1-MCO", pady=1)
_230_1_MCO_label.grid(row=7, column=2)

_230_3_FLA_label = Label(root, text="230-3-FLA", pady=1)
_230_3_FLA_label.grid(row=8, column=2)

_230_3_MCA_label = Label(root, text="230-3-MCA", pady=1)
_230_3_MCA_label.grid(row=9, column=2)

_230_3_MCO_label = Label(root, text="230-3-MCO", pady=1)
_230_3_MCO_label.grid(row=10, column=2)

_460_3_FLA_label = Label(root, text="460-3-FLA", pady=1)
_460_3_FLA_label.grid(row=11, column=2)

_460_3_MCA_label = Label(root, text="460-3-MCA", pady=1)
_460_3_MCA_label.grid(row=12, column=2)

_460_3_MCO_label = Label(root, text="460-3-MCO", pady=1)
_460_3_MCO_label.grid(row=13, column=2)

_20F_label = Label(root, text="20 F", pady=1)
_20F_label.grid(row=14, column=2)

_30F_label = Label(root, text="30 F", pady=1)
_30F_label.grid(row=15, column=2)

_40F_label = Label(root, text="40 F", pady=1)
_40F_label.grid(row=16, column=2)

# -------------Create buttons to submit data------------------------------------
# Submits data to the database then clears the data.
sub = "Add record to database"
submit_button = Button(root, text=sub, command=add_to_row)
submit_button.grid(row=18, column=0, columnspan=2, pady=5, padx=5, ipadx=100)

# ----------------------Creat query button--------------------------------------
# This will show all the records in the database, probably not useful.
que = "See records"
que_button = Button(root, text=que, command=query)
que_button.grid(row=18, column=2, columnspan=2, pady=5, padx=5, ipadx=131)

# ---------------------Edit quantity button--------------------------------------
edit = "Edit Record"
edit_button = Button(root, text=edit, command=editing)
edit_button.grid(row=19, column=0, columnspan=2, pady=5, padx=5, ipadx=130)

# -------------------Create buttons to delete data-------------------------------
"""
Make a window pop up saying that the data will be deleted and are you sure?
"""
erase = "Delete record from database"
del_button = Button(root, text=erase, command=delete)
del_button.grid(row=19, column=2, columnspan=2, pady=5, padx=5, ipadx=85)


# ----------------Print out CSV button------------------------------------------
csv_lab = "Print out to a CSV(Excel)"  # add_to_csv
csv_button = Button(root, text=csv_lab, command=csv_2_xlsx)
csv_button.grid(row=20, column=0, columnspan=2, pady=5, padx=5, ipadx=97.5)

# -------------Create buttons to add csv data------------------------------------
# Submits data to the database then clears the data.
imp = "Import csv record to database"  # csv_to_postgres
submit_button = Button(root, text=imp, command=file_opener)
submit_button.grid(row=20, column=2, columnspan=2, pady=5, padx=5, ipadx=83)


# ------------------------Canvas------------------------------------------------
canvas = Canvas(root)


# -----------------Scroll Bar---------------------------------------------------
"""
This needs to be figured out or I guess I can just try a bunch of different sizes
and just use root.resizable(0,0) instead and make it so no one can edit the size
of the window.
"""

# ybar = Scrollbar(root, orient='vertical', command=canvas.yview)
# canvas.configure(yscrollcommand=ybar.set)
# ybar.grid(row=1,column=5, sticky="ns")

# resize = Label(root)
# resize.grid(row=1, column=2,sticky='nsew')


# This will make it so the window can't be resized. Might be worth doing if I
# Can't figure out how to make it change dynamically with grid.
# root.resizable(0, 0)
root.mainloop()
