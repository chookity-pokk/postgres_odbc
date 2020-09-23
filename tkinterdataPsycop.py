from tkinter import *
import psycopg2
import pandas as pd
import tkinter.messagebox
from tkinter import scrolledtext
import os
from tkinter import filedialog
import time

"""
Add button to the top of the window ie a menu
Maybe add a few things to that menu, like contact info
or allow importing and exporting csvs through there.
"""



"""
Maybe look into adding a drop down menu that lets you pick the database you are 
looking to use.
"""

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
root.geometry("1000x400")
tb = "inv_testing3"


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


"""
Probably add a try and except here.
"""


def add_to_row():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to commit data to database?"
    )
    if answer == "yes":
        try:
            sql = f"""INSERT INTO {tb} (model, dimensions, frame, housing, tank_size,
                    tank_mat, compressor_hp, condenser, process_pump_hp, gpm_at_25psi,
                    weight, conn_size, conn_type, chiller_pump_hp,
                    heat_exchanger, controls, electrical_enclosure, shipping_weight,
                    decibals_at_10_feet, refrigerant, _230_1_FLA, _230_1_MCA, _230_1_MCO,
                    _230_3_FLA, _230_3_MCA, _230_3_MCO, _460_3_FLA, _460_3_MCA, _460_3_MCO,
                    _20F, _30F, _40F) VALUES ('{model.get()}', '{dimensions.get()}', '{frame.get()}', 
                    '{housing.get()}', {tank_size.get()}, '{tank_mat.get()}', '{compressor_hp.get()}', 
                    '{condenser.get()}', {process_pump_hp.get()}, {gpm_at_25psi.get()},{weight.get()}, 
                    '{conn_size.get()}', '{conn_type.get()}', '{chiller_pump_hp.get()}','{heat_exchanger.get()}', 
                    '{controls.get()}', '{electrical_enclosure.get()}', '{shipping_weight.get()}',
                    {decibals_at_10_feet.get()}, '{refrigerant.get()}', '{_230_1_FLA.get()}', 
                    '{_230_1_MCA.get()}', '{_230_1_MCO.get()}','{_230_3_FLA.get()}', '{_230_3_MCA.get()}', 
                    '{_230_3_MCO.get()}', '{_460_3_FLA.get()}', '{_460_3_MCA.get()}', 
                    '{_460_3_MCO.get()}', '{_20F.get()}', '{_30F.get()}', '{_40F.get()}')
                    """
            print(sql)
            cur.execute(sql)
            tkinter.messagebox.showinfo(
                "G&D Chilllers", f"You have added {model.get()} to your database."
            )
            # This deletes the entries of the box after submitting the data.
            model.delete(0, END)
            dimensions.delete(0, END)
            frame.delete(0, END)
            housing.delete(0, END)
            tank_size.delete(0, END)
            tank_mat.delete(0, END)
            compressor_hp.delete(0, END)
            condenser.delete(0, END)
            process_pump_hp.delete(0, END)
            gpm_at_25psi.delete(0, END)
            weight.delete(0, END)
            conn_size.delete(0, END)
            conn_type.delete(0, END)
            connection_size.delete(0, END)
            chiller_pump_hp.delete(0, END)
            heat_exchanger.delete(0, END)
            controls.delete(0, END)
            electrical_enclosure.delete(0, END)
            shipping_weight.delete(0, END)
            decibals_at_10_feet.delete(0, END)
            refrigerant.delete(0, END)
            _230_1_FLA.delete(0, END)
            _230_1_MCA.delete(0, END)
            _230_1_MCO.delete(0, END)
            _230_3_FLA.delete(0, END)
            _230_3_MCA.delete(0, END)
            _230_3_MCO.delete(0, END)
            _460_3_FLA.delete(0, END)
            _460_3_MCA.delete(0, END)
            _460_3_MCO.delete(0, END)
            _20F.delete(0, END)
            _30F.delete(0, END)
            _40F.delete(0, END)
            conn.commit()
        except:
            warning = "Make sure that the entries are the proper data type ie numbers or words."
            tkinter.messagebox.showinfo(
                "G&D Chillers", f"Unable to add the data to the database. {warning}"
            )
    else:
        pass


def editdb():
    print("Working")
    try:
        sql = f"""UPDATE {tb} set model='{model_editor.get()}',dimensions='{dimensions_editor.get()}',frame='{frame_editor.get()}',
                housing='{housing_editor.get()}',tank_size={tank_size_editor.get()},tank_mat='{tank_mat_editor.get()}',
                compressor_hp='{compressor_hp_editor.get()}',condenser='{condenser_editor.get()}',
                process_pump_hp={process_pump_hp_editor.get()},gpm_at_25psi={gpm_at_25psi_editor.get()},
                weight={weight_editor.get()},conn_size='{conn_size_editor.get()}',conn_type='{conn_type_editor.get()}',
                connection_size='{connection_size_editor.get()}',chiller_pump_hp='{chiller_pump_hp_editor.get()}',
                heat_exchanger='{heat_exchanger_editor.get()}',controls='{controls_editor.get()}',
                electrical_enclosure='{electrical_enclosure_editor.get()}',shipping_weight='{shipping_weight_editor.get()}',
                decibals_at_10_feet={decibals_at_10_feet_editor.get()},refrigerant='{refrigerant_editor.get()}',
                _230_1_FLA='{_230_1_FLA_editor.get()}',_230_1_MCA='{_230_1_MCA_editor.get()}',_230_1_MCO='{_230_1_MCO_editor.get()}',
                _230_3_FLA='{_230_3_FLA_editor.get()}',_230_3_MCA='{_230_3_MCA_editor.get()}',_230_3_MCO='{_230_3_MCO_editor.get()}',
                _460_3_FLA='{_460_3_FLA_editor.get()}',_460_3_MCA='{_460_3_MCA_editor.get()}',_460_3_MCO='{_460_3_MCO_editor.get()}',
                _20F='{_20F_editor.get()}',_30F='{_30F_editor.get()}',_40F='{_40F_editor.get()}' WHERE model='{model_editor.get()}'
             """

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
        #   print("Working again")
        cur.execute(sql)
        print("Still working")
        conn.commit()
        tkinter.messagebox.showinfo(
            "G&D Chillers", f"You have edited {model_editor.get()}"
        )
        editor.destroy()
        print("Mission accomplished!")
    except:
        tkinter.messagebox.showinfo(
            "G&D Chillers",
            "You were unable to edit records. Make sure you have values for all the text boxes.",
        )


def editing():
    print("This is working")
    global editor
    editor = Tk()
    editor.title("Update Record")
    editor.geometry("1000x400")
    editor.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    # ---------------------------------Global Variables-----------------------------------------
    # These are all global because it gets rid of having to have a function inside of a function.
    global model_editor
    global dimensions_editor
    global frame_editor
    global housing_editor
    global tank_size_editor
    global tank_mat_editor
    global compressor_hp_editor
    global condenser_editor
    global process_pump_hp_editor
    global gpm_at_25psi_editor
    global weight_editor
    global conn_size_editor
    global conn_type_editor
    global connection_size_editor
    global chiller_pump_hp_editor
    global heat_exchanger_editor
    global controls_editor
    global electrical_enclosure_editor
    global shipping_weight_editor
    global decibals_at_10_feet_editor
    global refrigerant_editor
    global _230_1_FLA_editor
    global _230_1_MCA_editor
    global _230_1_MCO_editor
    global _230_3_FLA_editor
    global _230_3_MCA_editor
    global _230_3_MCO_editor
    global _460_3_FLA_editor
    global _460_3_MCA_editor
    global _460_3_MCO_editor
    global _20F_editor
    global _30F_editor
    global _40F_editor

    # --------------------------------Database Entries-----------------------------------------
    model_editor = Entry(editor, width=30)
    model_editor.grid(row=0, column=1, padx=5)
    dimensions_editor = Entry(editor, width=30)
    dimensions_editor.grid(row=1, column=1, padx=5)
    frame_editor = Entry(editor, width=30)
    frame_editor.grid(row=2, column=1, padx=5)
    housing_editor = Entry(editor, width=30)
    housing_editor.grid(row=3, column=1, padx=5)
    tank_size_editor = Entry(editor, width=30)
    tank_size_editor.grid(row=4, column=1, padx=5)
    tank_mat_editor = Entry(editor, width=30)
    tank_mat_editor.grid(row=5, column=1, padx=5)
    compressor_hp_editor = Entry(editor, width=30)
    compressor_hp_editor.grid(row=6, column=1, padx=5)
    condenser_editor = Entry(editor, width=30)
    condenser_editor.grid(row=7, column=1, padx=5)
    process_pump_hp_editor = Entry(editor, width=30)
    process_pump_hp_editor.grid(row=8, column=1, padx=5)
    gpm_at_25psi_editor = Entry(editor, width=30)
    gpm_at_25psi_editor.grid(row=9, column=1, padx=5)
    weight_editor = Entry(editor, width=30)
    weight_editor.grid(row=10, column=1, padx=5)
    conn_size_editor = Entry(editor, width=30)
    conn_size_editor.grid(row=0, column=3, padx=5)
    conn_type_editor = Entry(editor, width=30)
    conn_type_editor.grid(row=1, column=3, padx=5)
    connection_size_editor = Entry(editor, width=30)
    connection_size_editor.grid(row=2, column=3, padx=5)
    chiller_pump_hp_editor = Entry(editor, width=30)
    chiller_pump_hp_editor.grid(row=3, column=3, padx=5)
    heat_exchanger_editor = Entry(editor, width=30)
    heat_exchanger_editor.grid(row=4, column=3, padx=5)
    controls_editor = Entry(editor, width=30)
    controls_editor.grid(row=5, column=3, padx=5)
    electrical_enclosure_editor = Entry(editor, width=30)
    electrical_enclosure_editor.grid(row=6, column=3, padx=5)
    shipping_weight_editor = Entry(editor, width=30)
    shipping_weight_editor.grid(row=7, column=3, padx=5)
    decibals_at_10_feet_editor = Entry(editor, width=30)
    decibals_at_10_feet_editor.grid(row=8, column=3, padx=5)
    refrigerant_editor = Entry(editor, width=30)
    refrigerant_editor.grid(row=9, column=3, padx=5)
    _230_1_FLA_editor = Entry(editor, width=30)
    _230_1_FLA_editor.grid(row=10, column=3, padx=5)
    _230_1_MCA_editor = Entry(editor, width=30)
    _230_1_MCA_editor.grid(row=0, column=5, padx=5)
    _230_1_MCO_editor = Entry(editor, width=30)
    _230_1_MCO_editor.grid(row=1, column=5, padx=5)
    _230_3_FLA_editor = Entry(editor, width=30)
    _230_3_FLA_editor.grid(row=2, column=5, padx=5)
    _230_3_MCA_editor = Entry(editor, width=30)
    _230_3_MCA_editor.grid(row=3, column=5, padx=5)
    _230_3_MCO_editor = Entry(editor, width=30)
    _230_3_MCO_editor.grid(row=4, column=5, padx=5)
    _460_3_FLA_editor = Entry(editor, width=30)
    _460_3_FLA_editor.grid(row=5, column=5, padx=5)
    _460_3_MCA_editor = Entry(editor, width=30)
    _460_3_MCA_editor.grid(row=6, column=5, padx=5)
    _460_3_MCO_editor = Entry(editor, width=30)
    _460_3_MCO_editor.grid(row=7, column=5, padx=5)
    _20F_editor = Entry(editor, width=30)
    _20F_editor.grid(row=8, column=5, padx=5)
    _30F_editor = Entry(editor, width=30)
    _30F_editor.grid(row=9, column=5, padx=5)
    _40F_editor = Entry(editor, width=30)
    _40F_editor.grid(row=10, column=5, padx=5)
    # ----------------------------Create text box labels-------------------------
    model_editor_label = Label(editor, text="Model", pady=1)
    model_editor_label.grid(row=0, column=0)
    dimensions_editor_label = Label(editor, text="Dimensions", pady=1)
    dimensions_editor_label.grid(row=1, column=0)
    frame_editor_label = Label(editor, text="Frame", pady=1)
    frame_editor_label.grid(row=2, column=0)
    housing_editor_label = Label(editor, text="Housing", pady=1)
    housing_editor_label.grid(row=3, column=0)
    tank_size_editor_label = Label(editor, text="Tank Size", pady=1)
    tank_size_editor_label.grid(row=4, column=0)
    tank_mat_editor_label = Label(editor, text="Tank Material", pady=1)
    tank_mat_editor_label.grid(row=5, column=0)
    compressor_hp_editor_label = Label(editor, text="Compressor HP", pady=1)
    compressor_hp_editor_label.grid(row=6, column=0)
    condenser_editor_label = Label(editor, text="Condenser", pady=1)
    condenser_editor_label.grid(row=7, column=0)
    process_pump_hp_editor_label = Label(editor, text="Process Pump HP", pady=1)
    process_pump_hp_editor_label.grid(row=8, column=0)
    gpm_at_25psi_editor_label = Label(editor, text="GPM at 25 PSI", pady=1)
    gpm_at_25psi_editor_label.grid(row=9, column=0)
    weight_editor_label = Label(editor, text="Weight", pady=1)
    weight_editor_label.grid(row=10, column=0)
    conn_size_editor_label = Label(editor, text="ConnSize", pady=1)
    conn_size_editor_label.grid(row=0, column=2)
    conn_type_editor_label = Label(editor, text="Connection Type", pady=1)
    conn_type_editor_label.grid(row=1, column=2)
    connection_size_editor_label = Label(editor, text="Connection Size", pady=1)
    connection_size_editor_label.grid(row=2, column=2)
    chiller_pump_hp_editor_label = Label(editor, text="Chiller Pump HP", pady=1)
    chiller_pump_hp_editor_label.grid(row=3, column=2)
    heat_exchanger_editor_label = Label(editor, text="Heat Exchanger", pady=1)
    heat_exchanger_editor_label.grid(row=4, column=2)
    controls_editor_label = Label(editor, text="Controls", pady=1)
    controls_editor_label.grid(row=5, column=2)
    electrical_enclosure_editor_label = Label(
        editor, text="Electrical Enclosure", pady=1
    )
    electrical_enclosure_editor_label.grid(row=6, column=2)
    shipping_weight_editor_label = Label(editor, text="Shipping Weight", pady=1)
    shipping_weight_editor_label.grid(row=7, column=2)
    decibals_at_10_feet_editor_label = Label(editor, text="Decibals at 10 feet", pady=1)
    decibals_at_10_feet_editor_label.grid(row=8, column=2)
    refrigerant_editor_label = Label(editor, text="Refrigerant", pady=1)
    refrigerant_editor_label.grid(row=9, column=2)
    _230_1_FLA_editor_label = Label(editor, text="230-1-FLA", pady=1)
    _230_1_FLA_editor_label.grid(row=10, column=2)
    _230_1_MCA_editor_label = Label(editor, text="230-1-MCA", pady=1)
    _230_1_MCA_editor_label.grid(row=0, column=4)
    _230_1_MCO_editor_label = Label(editor, text="230-1-MCO", pady=1)
    _230_1_MCO_editor_label.grid(row=1, column=4)
    _230_3_FLA_editor_label = Label(editor, text="230-3-FLA", pady=1)
    _230_3_FLA_editor_label.grid(row=2, column=4)
    _230_3_MCA_editor_label = Label(editor, text="230-3-MCA", pady=1)
    _230_3_MCA_editor_label.grid(row=3, column=4)
    _230_3_MCO_editor_label = Label(editor, text="230-3-MCO", pady=1)
    _230_3_MCO_editor_label.grid(row=4, column=4)
    _460_3_FLA_editor_label = Label(editor, text="460-3-FLA", pady=1)
    _460_3_FLA_editor_label.grid(row=5, column=4)
    _460_3_MCA_editor_label = Label(editor, text="460-3-MCA", pady=1)
    _460_3_MCA_editor_label.grid(row=6, column=4)
    _460_3_MCO_editor_label = Label(editor, text="460-3-MCO", pady=1)
    _460_3_MCO_editor_label.grid(row=7, column=4)
    _20F_editor_label = Label(editor, text="20 F", pady=1)
    _20F_editor_label.grid(row=8, column=4)
    _30F_editor_label = Label(editor, text="30 F", pady=1)
    _30F_editor_label.grid(row=9, column=4)
    _40F_editor_label = Label(editor, text="40 F", pady=1)
    _40F_editor_label.grid(row=10, column=4)
    # ----------------------------Grabbing the info------------------------------
    get_model = model_editor.get()
    get_dimensions = dimensions_editor.get()
    get_frame = frame_editor.get()
    get_housing = housing_editor.get()
    get_tank_size = tank_size_editor.get()
    get_tank_mat = tank_mat_editor.get()
    get_compressor_hp = compressor_hp_editor.get()
    get_condenser = condenser_editor.get()
    get_process_pump_hp = process_pump_hp_editor.get()
    get_gpm_at_25psi = gpm_at_25psi_editor.get()
    get_weight = weight_editor.get()
    get_conn_size = conn_size_editor.get()
    get_conn_type = conn_type_editor.get()
    get_connection_size = connection_size_editor.get()
    get_chiller_pump_hp = chiller_pump_hp_editor.get()
    get_heat_exchanger = heat_exchanger_editor.get()
    get_controls = controls_editor.get()
    get_electrical_enclosure = electrical_enclosure_editor.get()
    get_shipping_weight = shipping_weight_editor.get()
    get_decibals_at_10_feet = decibals_at_10_feet_editor.get()
    get_refrigerant = refrigerant_editor.get()
    get_230_1_FLA = _230_1_FLA_editor.get()
    get_230_1_MCA = _230_1_MCA_editor.get()
    get_230_1_MCO = _230_1_MCO_editor.get()
    get_230_3_FLA = _230_3_FLA_editor.get()
    get_230_3_MCA = _230_3_MCA_editor.get()
    get_230_3_MCO = _230_3_MCO_editor.get()
    get_460_3_FLA = _460_3_FLA_editor.get()
    get_460_3_MCA = _460_3_MCA_editor.get()
    get_460_3_MCO = _460_3_MCO_editor.get()
    get_20F = _20F_editor.get()
    get_30F = _30F_editor.get()
    get_40F = _40F_editor.get()
    # ---------------------------------Save button----------------------------------
    edit = "Save Editted Record"
    edit_button = Button(editor, text=edit, command=editdb)
    edit_button.grid(row=12, column=2, columnspan=2, pady=5, padx=5, ipadx=130)


"""
The query function button is commented out below becuase it basically
serves no real purpose when you have more than a handful of entries in
the database because it will take over the entire screen.
"""


def query():
    sql = f"SELECT * FROM {tb}"
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


# This deletes the database entry by the model name. Not sure how to deal with it.
def delete():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to delete data to database?"
    )
    if answer == "yes":
        try:
            sql = f"DELETE from {tb} WHERE model = '{model.get()}'"
            cur.execute(sql)
            print(f"Model {model.get()} was deleted from {tb}")
            tkinter.messagebox.showinfo(
                "G&D Chillers", f"{model.get()} has been deleted from the database"
            )
            model.delete(0, END)
            dimensions.delete(0, END)
            frame.delete(0, END)
            housing.delete(0, END)
            tank_size.delete(0, END)
            tank_mat.delete(0, END)
            compressor_hp.delete(0, END)
            condenser.delete(0, END)
            process_pump_hp.delete(0, END)
            gpm_at_25psi.delete(0, END)
            weight.delete(0, END)
            conn_size.delete(0, END)
            conn_type.delete(0, END)
            connection_size.delete(0, END)
            chiller_pump_hp.delete(0, END)
            heat_exchanger.delete(0, END)
            controls.delete(0, END)
            electrical_enclosure.delete(0, END)
            shipping_weight.delete(0, END)
            decibals_at_10_feet.delete(0, END)
            refrigerant.delete(0, END)
            _230_1_FLA.delete(0, END)
            _230_1_MCA.delete(0, END)
            _230_1_MCO.delete(0, END)
            _230_3_FLA.delete(0, END)
            _230_3_MCA.delete(0, END)
            _230_3_MCO.delete(0, END)
            _460_3_FLA.delete(0, END)
            _460_3_MCA.delete(0, END)
            _460_3_MCO.delete(0, END)
            _20F.delete(0, END)
            _30F.delete(0, END)
            _40F.delete(0, END)
            conn.commit()
        except:
            d_text = (
                "Unable to delete entry from database. Make sure that the model name"
            )
            tkinter.messagebox.showinfo(
                "G&D Chillers",
                f"{d_text} matches a model name from the database. Email hank@gdchillers.com if you have issues.",
            )
    else:
        pass


def add_to_csv():
    """
    This function will take the contents of the table in PostgreSQL
    and put them to a csv. May be needed if peole want to externally save the
    contents of the database in a public place that people can easily access
    i.e. pushing the csv to a public folder for the company to look at.
    """
    csv_exp = Tk()
    csv_exp.title("Update a record")
    csv_exp.geometry("300x300")
    csv_exp.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    csv_lab = "Click here to export CSV file"
    csv_button = Button(csv_exp, text=csv_lab, command=save_file)
    csv_button.grid(row=3, column=3, columnspan=2, pady=5, padx=5, ipadx=66)


# Adds the option to push a csv into the database.
def csv_to_postgres():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to import data from a CSV?"
    )
    if answer == "yes":

        csv_imp = Tk()
        csv_imp.title("Update a record")
        csv_imp.geometry("300x300")
        csv_imp.iconbitmap(
            r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
        )
        csv_lab = "Click here to impport a CSV file"
        csv_button = Button(csv_imp, text=csv_lab, command=file_opener)
        csv_button.grid(row=3, column=3, columnspan=2, pady=5, padx=5, ipadx=66)


def file_opener():
    # This is connected to csv_to_postgres
    # https://www.tutorialspoint.com/askopenfile-function-in-python-tkinter
    input = filedialog.askopenfile(
        initialdir="/", filetypes=[("CSV", "*.csv"), ("XLSX", "*.xlsx")]
    )
    tb = "inv_testing3"
    try:
        sql = f"""COPY {tb} FROM STDIN DELIMITER ',' CSV HEADER;"""
        with open(input.name) as f:
            cur.copy_expert(sql, f)
        conn.commit()
        tkinter.messagebox.showinfo(
            "G&D Chillers", f"Your data has been imported from {input.name} to {tb}."
        )
    except:
        words = """It is likely because it doesn't have the same column names.
        Please check and if you can't resolve the issue email hank@gdchillers.com"""
        tkinter.messagebox.showinfo(
            "G&D Chillers", f"There was an error uploading {input.name}. {words}"
        )


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
        print(df)
        df.sort_values("tank_size", inplace=True)
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


def csv_2_xlsx():
    input = filedialog.asksaveasfilename(initialdir="/", filetypes=[("CSV", "*.csv")])
    try:
        from openpyxl import Workbook
        import csv

        tb = "inv_testing3"
        sql1 = """ SELECT * FROM {}""".format(tb)
        rows = cur.execute(sql1)
        col_headers = [i[0] for i in cur.description]
        rows = [list(i) for i in cur.fetchall()]
        df = pd.DataFrame(rows, columns=col_headers)
        print(df)
        df.sort_values(
            "tank_size", inplace=True
        )  # This line is sorting the output of the database. FML, without having inplace=True it doesn't fucking work.
        print(df)
        df.to_csv(input + ".csv", index=False)
        print(f"{input}")
        tkinter.messagebox.showinfo("G&D Chillers", f"Your CSV was saved at {input}")
        ans = tkinter.messagebox.askquestion(
            "G&D Chillers", "Would you like to convert the CSV to an Excel file?"
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
            print(
                f"Your csv has been converted to an Excel file and stored here {xlsx_path}"
            )
            tkinter.messagebox.showinfo(
                "G&D Chillers", f"Your Excel file was saved at {xlsx_path}"
            )
    except:
        tkinter.messagebox.showinfo(
            "G&D Chillers",
            f"You were unable to save your file {input}, {input}. If this issue continues please email hank@gdchillers.com",
        )


"""
ADD THE option to delete the code after an amount of time or 
hitting a button.
Added in the stuff in comments but can't figure out how to get 
it to work because it just goes to sleep before even filling 
in the boxes then the page is just frozen for the amount of time
chosen in time.sleep(X) then resets. So I don't know how to 
implement it.
"""

"""
Add a try and except and if it isn't an available option
to autofill/autocomplete then list the available chillers
that can be filled.
"""

def autofill():
    print(model.get())
    if model.get() == "GD-1.5H" or model.get() == "gd-1.5h":
        dimensions.insert(0, "30x30x30")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, "12")
        tank_mat.insert(0, "SST")
        condenser.insert(0, "Air-Cooled")
        compressor_hp.insert(0, 1)
        process_pump_hp.insert(0, 0.5)
        gpm_at_25psi.insert(0, 20)
        weight.insert(0, 250)
        conn_size.insert(0, '1"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1" FPT')
        chiller_pump_hp.insert(0, 0)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Single Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "")
        decibals_at_10_feet.insert(0, 0)
        refrigerant.insert(0, "")
        _230_1_FLA.insert(0, 16)
        _230_1_MCA.insert(0, 19)
        _230_1_MCO.insert(0, 29)
        _230_3_FLA.insert(0, 14)
        _230_3_MCA.insert(0, 16)
        _230_3_MCO.insert(0, 24)
        _460_3_FLA.insert(0, 0)
        _460_3_MCA.insert(0, 0)
        _460_3_MCO.insert(0, 0)
        _20F.insert(0, 8460)
        _30F.insert(0, 10200)
        _40F.insert(0, 12400)

    elif model.get() == "GD-3H" or model.get() == "gd-3h":
        dimensions.insert(0, "32x48x35")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 30)
        tank_mat.insert(0, "SST")
        compressor_hp.insert(0, 3)
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 0.75)
        gpm_at_25psi.insert(0, 25)
        weight.insert(0, 810)
        conn_size.insert(0, '1"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1" FPT')
        chiller_pump_hp.insert(0, 0)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Single Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "700 lbs")
        decibals_at_10_feet.insert(0, 62)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 27)
        _230_1_MCA.insert(0, 30)
        _230_1_MCO.insert(0, 51)
        _230_3_FLA.insert(0, 18)
        _230_3_MCA.insert(0, 21)
        _230_3_MCO.insert(0, 32)
        _460_3_FLA.insert(0, 8)
        _460_3_MCA.insert(0, 10)
        _460_3_MCO.insert(0, 15)
        _20F.insert(0, 17213)
        _30F.insert(0, 21436)
        _40F.insert(0, 26098)

    elif model.get() == "GD-5H" or model.get() == "gd-5h":
        dimensions.insert(0, "45x61x49")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 60)
        tank_mat.insert(0, "SST")
        compressor_hp.insert(0, 5)
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 1.5)
        gpm_at_25psi.insert(0, 40)
        weight.insert(0, 1450)
        conn_size.insert(0, '1"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1" FPT')
        chiller_pump_hp.insert(0, 0)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Single Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "1200 lbs")
        decibals_at_10_feet.insert(0, 65)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 48)
        _230_1_MCA.insert(0, 56)
        _230_1_MCO.insert(0, 90)
        _230_3_FLA.insert(0, 33)
        _230_3_MCA.insert(0, 38)
        _230_3_MCO.insert(0, 58)
        _460_3_FLA.insert(0, 8)
        _460_3_MCA.insert(0, 10)
        _460_3_MCO.insert(0, 15)
        _20F.insert(0, 32717)
        _30F.insert(0, 40850)
        _40F.insert(0, 49965)

    elif model.get() == "GD-7H" or model.get() == "gd-7h":
        dimensions.insert(0, "45x61x49")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 60)
        tank_mat.insert(0, "SST")
        compressor_hp.insert(0, 7)
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 1.5)
        gpm_at_25psi.insert(0, 40)
        weight.insert(0, 1450)
        conn_size.insert(0, '1"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1" FPT')
        chiller_pump_hp.insert(0, 0)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Single Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "1200 lbs")
        decibals_at_10_feet.insert(0, 65)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 0)
        _230_1_MCA.insert(0, 0)
        _230_1_MCO.insert(0, 0)
        _230_3_FLA.insert(0, 41)
        _230_3_MCA.insert(0, 47)
        _230_3_MCO.insert(0, 74)
        _460_3_FLA.insert(0, 16)
        _460_3_MCA.insert(0, 19)
        _460_3_MCO.insert(0, 30)
        _20F.insert(0, 41395)
        _30F.insert(0, 51046)
        _40F.insert(0, 61824)

    elif model.get() == "GD-10H" or model.get() == "gd-10h":
        dimensions.insert(0, "48x73x57")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 110)
        tank_mat.insert(0, "SST")
        compressor_hp.insert(0, 10)
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 2)
        gpm_at_25psi.insert(0, 65)
        weight.insert(0, 2320)
        conn_size.insert(0, '1.5"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1.5" FPT')
        chiller_pump_hp.insert(0, 0)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Single Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "1600 lbs")
        decibals_at_10_feet.insert(0, 67)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 0)
        _230_1_MCA.insert(0, 0)
        _230_1_MCO.insert(0, 0)
        _230_3_FLA.insert(0, 49)
        _230_3_MCA.insert(0, 58)
        _230_3_MCO.insert(0, 92)
        _460_3_FLA.insert(0, 25)
        _460_3_MCA.insert(0, 29)
        _460_3_MCO.insert(0, 46)
        _20F.insert(0, 64218)
        _30F.insert(0, 79372)
        _40F.insert(0, 96495)

    elif model.get() == "GD-13.5H" or model.get() == "gd-13.5h":
        dimensions.insert(0, "48x73x57")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 110)
        tank_mat.insert(0, "SST")
        compressor_hp.insert(0, 13.5)
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 2)
        gpm_at_25psi.insert(0, 65)
        weight.insert(0, 2370)
        conn_size.insert(0, '1.5"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1.5" FPT')
        chiller_pump_hp.insert(0, 0)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Single Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "1650 lbs")
        decibals_at_10_feet.insert(0, 68)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 0)
        _230_1_MCA.insert(0, 0)
        _230_1_MCO.insert(0, 0)
        _230_3_FLA.insert(0, 59)
        _230_3_MCA.insert(0, 70)
        _230_3_MCO.insert(0, 115)
        _460_3_FLA.insert(0, 30)
        _460_3_MCA.insert(0, 40)
        _460_3_MCO.insert(0, 60)
        _20F.insert(0, 77911)
        _30F.insert(0, 95082)
        _40F.insert(0, 114193)

    elif model.get() == "GD-5x5H" or model.get() == "gd-5x5h":
        dimensions.insert(0, "48x84x62")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 115)
        tank_mat.insert(0, "SST")
        compressor_hp.insert(0, "5(x2)")
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 1.5)
        gpm_at_25psi.insert(0, 40)
        weight.insert(0, 2350)
        conn_size.insert(0, '1.5"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1.5" FPT')
        chiller_pump_hp.insert(0, 0)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Multi Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "1850 lbs")
        decibals_at_10_feet.insert(0, 65)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 85)
        _230_1_MCA.insert(0, 95)
        _230_1_MCO.insert(0, 127)
        _230_3_FLA.insert(0, 57)
        _230_3_MCA.insert(0, 62)
        _230_3_MCO.insert(0, 82)
        _460_3_FLA.insert(0, 26)
        _460_3_MCA.insert(0, 29)
        _460_3_MCO.insert(0, 38)
        _20F.insert(0, 65434)
        _30F.insert(0, 81700)
        _40F.insert(0, 99930)

    elif model.get() == "GD-7x7H" or model.get() == "gd-7x7h":
        dimensions.insert(0, "48x84x62")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 115)
        tank_mat.insert(0, "SST")
        compressor_hp.insert(0, "7(x2)")
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 2)
        gpm_at_25psi.insert(0, 65)
        weight.insert(0, 2468)
        conn_size.insert(0, '1.5"')
        conn_type.insert(0, "FPT")
        connection_size.insert(0, '1.5" FPT')
        chiller_pump_hp.insert(0, 1.5)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Multi Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "1850 lbs")
        decibals_at_10_feet.insert(0, 65)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 0)
        _230_1_MCA.insert(0, 0)
        _230_1_MCO.insert(0, 0)
        _230_3_FLA.insert(0, 68)
        _230_3_MCA.insert(0, 75)
        _230_3_MCO.insert(0, 101)
        _460_3_FLA.insert(0, 30)
        _460_3_MCA.insert(0, 33)
        _460_3_MCO.insert(0, 44)
        _20F.insert(0, 82790)
        _30F.insert(0, 102092)
        _40F.insert(0, 123648)

    elif model.get() == "GD-20H" or model.get() == "gd-20h":
        dimensions.insert(0, "48x120x81")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 230)
        tank_mat.insert(0, "PEX")
        compressor_hp.insert(0, "10(x2)")
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 5)
        gpm_at_25psi.insert(0, 150)
        weight.insert(0, 3910)
        conn_size.insert(0, '2"')
        conn_type.insert(0, "CTS Flange")
        connection_size.insert(0, '2" CTS Flange')
        chiller_pump_hp.insert(0, 1.5)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Multi Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "2200 lbs")
        decibals_at_10_feet.insert(0, 68)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 0)
        _230_1_MCA.insert(0, 0)
        _230_1_MCO.insert(0, 0)
        _230_3_FLA.insert(0, 101)
        _230_3_MCA.insert(0, 110)
        _230_3_MCO.insert(0, 145)
        _460_3_FLA.insert(0, 52)
        _460_3_MCA.insert(0, 55)
        _460_3_MCO.insert(0, 72)
        _20F.insert(0, 128436)
        _30F.insert(0, 158744)
        _40F.insert(0, 192990)

    elif model.get() == "GD-27H" or model.get() == "gd-27h":
        dimensions.insert(0, "48x120x81")
        frame.insert(0, "Powder Coated Steel")
        housing.insert(0, "Powder Coated Aluminum")
        tank_size.insert(0, 230)
        tank_mat.insert(0, "PEX")
        compressor_hp.insert(0, "13.5(2)")
        condenser.insert(0, "Air-Cooled")
        process_pump_hp.insert(0, 5)
        gpm_at_25psi.insert(0, 150)
        weight.insert(0, 3960)
        conn_size.insert(0, '2"')
        conn_type.insert(0, "CTS Flange")
        connection_size.insert(0, '2" CTS Flange')
        chiller_pump_hp.insert(0, 1.5)
        heat_exchanger.insert(0, "Stainless Steel Brazed Plate")
        controls.insert(0, "Multi Stage Digital")
        electrical_enclosure.insert(0, "NEMA 3R")
        shipping_weight.insert(0, "2250 lbs")
        decibals_at_10_feet.insert(0, 70)
        refrigerant.insert(0, "R404A")
        _230_1_FLA.insert(0, 0)
        _230_1_MCA.insert(0, 0)
        _230_1_MCO.insert(0, 0)
        _230_3_FLA.insert(0, 122)
        _230_3_MCA.insert(0, 133)
        _230_3_MCO.insert(0, 178)
        _460_3_FLA.insert(0, 62)
        _460_3_MCA.insert(0, 68)
        _460_3_MCO.insert(0, 91)
        _20F.insert(0, 155822)
        _30F.insert(0, 190164)
        _40F.insert(0, 228386)


def delete_text():
    model.delete(0, END)
    dimensions.delete(0, END)
    frame.delete(0, END)
    housing.delete(0, END)
    tank_size.delete(0, END)
    tank_mat.delete(0, END)
    compressor_hp.delete(0, END)
    condenser.delete(0, END)
    process_pump_hp.delete(0, END)
    gpm_at_25psi.delete(0, END)
    weight.delete(0, END)
    conn_size.delete(0, END)
    conn_type.delete(0, END)
    connection_size.delete(0, END)
    chiller_pump_hp.delete(0, END)
    heat_exchanger.delete(0, END)
    controls.delete(0, END)
    electrical_enclosure.delete(0, END)
    shipping_weight.delete(0, END)
    decibals_at_10_feet.delete(0, END)
    refrigerant.delete(0, END)
    _230_1_FLA.delete(0, END)
    _230_1_MCA.delete(0, END)
    _230_1_MCO.delete(0, END)
    _230_3_FLA.delete(0, END)
    _230_3_MCA.delete(0, END)
    _230_3_MCO.delete(0, END)
    _460_3_FLA.delete(0, END)
    _460_3_MCA.delete(0, END)
    _460_3_MCO.delete(0, END)
    _20F.delete(0, END)
    _30F.delete(0, END)
    _40F.delete(0, END)


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
conn_size.grid(row=0, column=3, padx=5)

conn_type = Entry(root, width=30)
conn_type.grid(row=1, column=3, padx=5)

connection_size = Entry(root, width=30)
connection_size.grid(row=2, column=3)

chiller_pump_hp = Entry(root, width=30)
chiller_pump_hp.grid(row=3, column=3, padx=5)

heat_exchanger = Entry(root, width=30)
heat_exchanger.grid(row=4, column=3, padx=5)

controls = Entry(root, width=30)
controls.grid(row=5, column=3, padx=5)

electrical_enclosure = Entry(root, width=30)
electrical_enclosure.grid(row=6, column=3, padx=5)

shipping_weight = Entry(root, width=30)
shipping_weight.grid(row=7, column=3, padx=5)

decibals_at_10_feet = Entry(root, width=30)
decibals_at_10_feet.grid(row=8, column=3, padx=5)

refrigerant = Entry(root, width=30)
refrigerant.grid(row=9, column=3, padx=5)

_230_1_FLA = Entry(root, width=30)
_230_1_FLA.grid(row=10, column=3, padx=5)

_230_1_MCA = Entry(root, width=30)
_230_1_MCA.grid(row=0, column=5, padx=5)

_230_1_MCO = Entry(root, width=30)
_230_1_MCO.grid(row=1, column=5, padx=5)

_230_3_FLA = Entry(root, width=30)
_230_3_FLA.grid(row=2, column=5, padx=5)

_230_3_MCA = Entry(root, width=30)
_230_3_MCA.grid(row=3, column=5, padx=5)

_230_3_MCO = Entry(root, width=30)
_230_3_MCO.grid(row=4, column=5, padx=5)

_460_3_FLA = Entry(root, width=30)
_460_3_FLA.grid(row=5, column=5, padx=5)

_460_3_MCA = Entry(root, width=30)
_460_3_MCA.grid(row=6, column=5, padx=5)

_460_3_MCO = Entry(root, width=30)
_460_3_MCO.grid(row=7, column=5, padx=5)

_20F = Entry(root, width=30)
_20F.grid(row=8, column=5, padx=5)

_30F = Entry(root, width=30)
_30F.grid(row=9, column=5, padx=5)

_40F = Entry(root, width=30)
_40F.grid(row=10, column=5, padx=5)


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
conn_size_label.grid(row=0, column=2)

conn_type_label = Label(root, text="ConnType", pady=1)
conn_type_label.grid(row=1, column=2)

connection_size_label = Label(root, text="Connection Size", pady=1)
connection_size_label.grid(row=2, column=2)

chiller_pump_hp_label = Label(root, text="Chiller Pump HP", pady=1)
chiller_pump_hp_label.grid(row=3, column=2)
# From here I want to split the window. Either that or at 16 becuase it'll split it in half, or maybe thirds.

heat_exchanger_label = Label(root, text="Heat Exchanger", pady=1)
heat_exchanger_label.grid(row=4, column=2)

controls_label = Label(root, text="Controls", pady=1)
controls_label.grid(row=5, column=2)

electrical_enclosure_label = Label(root, text="Electrical Enlcosure", pady=1)
electrical_enclosure_label.grid(row=6, column=2)

shipping_weight_label = Label(root, text="Shipping Weight", pady=1)
shipping_weight_label.grid(row=7, column=2)

decibals_at_10_feet_label = Label(root, text="Decibals at 10 feet", pady=1)
decibals_at_10_feet_label.grid(row=8, column=2)

refrigerant_label = Label(root, text="Refrigerant", pady=1)
refrigerant_label.grid(row=9, column=2)

_230_1_FLA_label = Label(root, text="230-1-FLA", pady=1)
_230_1_FLA_label.grid(row=10, column=2)

_230_1_MCA_label = Label(root, text="230-1-MCA", pady=1)
_230_1_MCA_label.grid(row=0, column=4)

_230_1_MCO_label = Label(root, text="230-1-MCO", pady=1)
_230_1_MCO_label.grid(row=1, column=4)

_230_3_FLA_label = Label(root, text="230-3-FLA", pady=1)
_230_3_FLA_label.grid(row=2, column=4)

_230_3_MCA_label = Label(root, text="230-3-MCA", pady=1)
_230_3_MCA_label.grid(row=3, column=4)

_230_3_MCO_label = Label(root, text="230-3-MCO", pady=1)
_230_3_MCO_label.grid(row=4, column=4)

_460_3_FLA_label = Label(root, text="460-3-FLA", pady=1)
_460_3_FLA_label.grid(row=5, column=4)

_460_3_MCA_label = Label(root, text="460-3-MCA", pady=1)
_460_3_MCA_label.grid(row=6, column=4)

_460_3_MCO_label = Label(root, text="460-3-MCO", pady=1)
_460_3_MCO_label.grid(row=7, column=4)

_20F_label = Label(root, text="20 F", pady=1)
_20F_label.grid(row=8, column=4)

_30F_label = Label(root, text="30 F", pady=1)
_30F_label.grid(row=9, column=4)

_40F_label = Label(root, text="40 F", pady=1)
_40F_label.grid(row=10, column=4)

# ------------------Making a menu button for deleting entries-------------------
menubar = Menu(root)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=file)
file.add_command(label="Delete", command = delete_text)
file.add_command(label="BLah", command=None)

# -------------Create buttons to submit data------------------------------------
# Submits data to the database then clears the data.
# [X]This is completed with the new data
sub = "Add record to database"
submit_button = Button(root, text=sub, command=add_to_row)
submit_button.grid(row=18, column=1, columnspan=2, pady=5, padx=5, ipadx=100)

# ----------------------Creat query button--------------------------------------
# This will show all the records in the database, probably not useful.
# 9/14/2020 Commenting out this button because the database will almost certainly be too big to see
# In one window
# que = "See records"
# que_button = Button(root, text=que, command=query)
# que_button.grid(row=18, column=3, columnspan=2, pady=5, padx=5, ipadx=131)

# --------------------Autofill button-------------------------------------------
# [X] If there is an X here then this is working for all entries
fill = "Auto Complete Based on Model Name"
fill_button = Button(root, text=fill, command=autofill)
fill_button.grid(row=21, column=1, columnspan=4, pady=5, padx=5, ipadx=127)

# ---------------------Edit quantity button--------------------------------------
# [X]This needs to be verified
edit = "Edit Record"
edit_button = Button(root, text=edit, command=editing)
edit_button.grid(row=18, column=3, columnspan=2, pady=5, padx=5, ipadx=130)

# -------------------Create buttons to delete data-------------------------------
# [X]Hasn't been added into the backend
erase = "Delete record from database"
del_button = Button(root, text=erase, command=delete)
del_button.grid(row=19, column=1, columnspan=2, pady=5, padx=5, ipadx=85)

# ----------------Print out CSV button------------------------------------------
# [X] This works
csv_lab = "Print out to a CSV(Excel)"  # add_to_csv
csv_button = Button(root, text=csv_lab, command=csv_2_xlsx)
csv_button.grid(row=19, column=3, columnspan=2, pady=5, padx=5, ipadx=97.5)

# ---------------------Delete entries button--------------------------------------
dele = "Delete Text Box Entries"
delete_button = Button(root, text=dele, command=delete_text)
delete_button.grid(row=22, column=1, columnspan=4, pady=5, padx=5, ipadx=100)

# -------------Create buttons to add csv data------------------------------------
# Submits data to the database then clears the data.
# [X]This works but only when the columns are the same name but that will always be a restriction.
imp = "Import csv record to database"  # csv_to_postgres
submit_button = Button(root, text=imp, command=file_opener)
submit_button.grid(row=20, column=1, columnspan=4, pady=5, padx=5, ipadx=150)

# This will make it so the window can't be resized. Might be worth doing if I
# Can't figure out how to make it change dynamically with grid.
root.config(menu=menubar)
root.resizable(0, 0)
root.mainloop()
