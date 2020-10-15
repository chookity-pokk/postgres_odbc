import os
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog, scrolledtext

import pandas as pd
import psycopg2

"""
NEED TO CHANGE THE SIZING FOR THIS WINDOW BECAUSE
IT THE TEXT BOXES ARE TOO BIG BUT I CAN SHRINK THE
SECTIONS FOR THE TEXT.
"""

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

def editdb(event=None):
    print("Working")
    try:
        sql = f"""UPDATE {tb} set model='{get_model}',dimensions='{get_dimensions}',frame='{get_frame}',
                housing='{get_housing}',tank_size={get_tank_size},tank_mat='{get_tank_mat}',
                compressor_hp='{get_compressor_hp}',condenser='{get_condenser}',
                process_pump_hp={get_process_pump_hp},gpm_at_25psi={get_gpm_at_25psi},
                weight={get_weight},conn_size='{get_conn_size}',conn_type='{get_conn_type}',
                connection_size='{get_connection_size}',chiller_pump_hp='{get_chiller_pump_hp}',
                heat_exchanger='{get_heat_exchanger}',controls='{get_controls}',
                electrical_enclosure='{get_electrical_enclosure}',shipping_weight='{get_shipping_weight}',
                decibals_at_10_feet={get_decibals_at_10_feet},refrigerant='{get_refrigerant}',
                _230_1_FLA='{get_230_1_FLA}',_230_1_MCA='{get_230_1_MCA}',_230_1_MCO='{get_230_1_MCO}',
                _230_3_FLA='{get_230_3_FLA}',_230_3_MCA='{get_230_3_MCA}',_230_3_MCO='{get_230_3_MCO}',
                _460_3_FLA='{get_460_3_FLA}',_460_3_MCA='{get_460_3_MCA}',_460_3_MCO='{get_460_3_MCO}',
                _20F='{get_20F}',_30F='{get_30F}',_40F='{get_40F}' WHERE model='{get_model}'
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
    except Exception as e:
        print(f"this is your error for editdb: \n {e}")
        tkinter.messagebox.showinfo(
            "G&D Chillers",
            "You were unable to edit records. Make sure you have values for all the text boxes.",
        )

"""
NEED TO CHANGE THE SIZING FOR THIS WINDOW BECAUSE
IT THE TEXT BOXES ARE TOO BIG BUT I CAN SHRINK THE
SECTIONS FOR THE TEXT.
"""

def editing(event=None):
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
    edit = "Save Editted Record (control+e)"
    edit_button = Button(editor, text=edit, command=editdb)
    edit_button.grid(row=12, column=1, columnspan=2, pady=5, padx=5, ipadx=110)
    # --------------------------------Autofill button ------------------------------
    fill = "Auto Complete Based on Model Name (control+a)"
    fill_button = Button(editor, text=fill, command=edit_autofill)
    fill_button.grid(row=12, column=3, columnspan=2, pady=5, padx=5, ipadx=65)
    # -------------------------------Key Bindings ----------------------------------
    editor.bind_all("<Control-a>", edit_autofill)
    editor.bind_all("<Control-e>", editdb)


def edit_autofill(event=None):
    record_id = model_editor.get()
    sql = f"SELECT * FROM {tb} where model = '{model_editor.get()}'"
    print(sql)
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        dimensions_editor.insert(0, record[1])
        frame_editor.insert(0, record[2])
        housing_editor.insert(0, record[3])
        tank_size_editor.insert(0, record[4])
        tank_mat_editor.insert(0, record[5])
        condenser_editor.insert(0, record[6])
        compressor_hp_editor.insert(0, record[7])
        process_pump_hp_editor.insert(0, record[8])
        gpm_at_25psi_editor.insert(0, record[9])
        weight_editor.insert(0, record[10])
        conn_size_editor.insert(0, record[11])
        conn_type_editor.insert(0, record[12])
        connection_size_editor.insert(0, record[13])
        chiller_pump_hp_editor.insert(0, record[14])
        heat_exchanger_editor.insert(0, record[15])
        controls_editor.insert(0, record[16])
        electrical_enclosure_editor.insert(0, record[17])
        shipping_weight_editor.insert(0, record[18])
        decibals_at_10_feet_editor.insert(0, record[19])
        refrigerant_editor.insert(0, record[20])
        _230_1_FLA_editor.insert(0, record[21])
        _230_1_MCA_editor.insert(0, record[22])
        _230_1_MCO_editor.insert(0, record[23])
        _230_3_FLA_editor.insert(0, record[24])
        _230_3_MCA_editor.insert(0, record[25])
        _230_3_MCO_editor.insert(0, record[26])
        _460_3_FLA_editor.insert(0, record[27])
        _460_3_MCA_editor.insert(0, record[28])
        _460_3_MCO_editor.insert(0, record[29])
        _20F_editor.insert(0, record[30])
        _30F_editor.insert(0, record[31])
        _40F_editor.insert(0, record[32])
