from tkinter import *
from tkinter import filedialog, scrolledtext

import pandas as pd
import psycopg2

add a bunch of try and excepts in this bad boy.

"""
May need to put this in its own
folder labeled 'Parts' just to 
organize the code
"""

tb = "compressor_db"

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


def comp_db():
    # -------------------------Global Vars---------------------
    global comp
    global comp_size
    global comp_model
    global comp_hp
    #-------------------------------Other Stuff--------------------
    comp = Tk()
    comp.title("Compressors")
    comp.geometry("600x200")
    comp.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
        
    # --------------------------------------------Entries--------------------------------------------------------
    comp_size = Entry(comp, width=30)
    comp_size.grid(row=0, column=1, padx=5)
    comp_model = Entry(comp, width=30)
    comp_model.grid(row=1, column=1, padx=5)
    comp_hp = Entry(comp, width=30)
    comp_hp.grid(row=2, column=1, padx=5)
    # -----------------------------------------Text box labels--------------------------------------------------
    comp_size_label = Label(comp, text="Compressor Size", pady=1)
    comp_size_label.grid(row=0, column=0)
    comp_model_label = Label(comp, text="Compressor Model", pady=1)
    comp_model_label.grid(row=1, column=0)
    comp_hp_label = Label(comp, text="Compressor HP", pady=1)
    comp_hp_label.grid(row=2, column=0)
    # ----------------------------------------Save Button ------------------------------------------------------
    save_text = "Saved Compressor HP"
    save_button = Button(comp, text=save_text, command=comp_save)
    save_button.grid(row=5, column=0, columnspan=1, pady=5, padx=5, ipadx=70)
    # ----------------------------------------Autofill button --------------------------------------------------
    fill = "Autofill based on compressor name"
    fill_button = Button(comp, text=fill, command=comp_autofill)
    fill_button.grid(row=5, column=1, columnspan=1, pady=5, padx=5, ipadx=50)
    # ---------------------------------------- Key Bindings ----------------------------------------------------
    comp.bind_all("<Control-a>", comp_autofill)
    comp.bind_all("<Control-s>", comp_save)
    
    comp.mainloop()
    

def comp_autofill():
    record_id = comp_model.get()
    sql = f"SELECT * FROM {tb} where model = '{comp_model.get()}'"
    print(sql)
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        """
        Insert stuff here.
        """
        comp_size.insert(0, record[1])
        comp_hp.insert(0, record[2])


def comp_save():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to save data to database?"
    )
    if answer == "yes":
        try:
            sql = f"""INSERT INTO {tb} {comp_size, comp_hp} VALUES 
                      ('{comp_size.get()}', '{comp_hp.get()}')"""

            print(sql)
            cur.execute(sql)
            comp_size.delete(0, END)
            comp_hp.delete(0, END)
            comp.destroy()
        except Except as e:
            print(f"This is what is happening with this bad boy: {e}")
            
    else:
        pass


