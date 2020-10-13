from tkinter import *
from tkinter import filedialog, scrolledtext

import pandas as pd
import psycopg2

Add try and excepts throughout this bad boy.


"""
May need to put this in its own
folder labeled 'Parts' just to 
organize the code
"""

tb = "condenser_db"

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


def cond_db():
    # ---------------------------------Global Vars--------------------------
    global cond
    global cond_model
    global cond_hp
    global cond_size
    # --------------------------------Stuff---------------------------------
    cond = Tk()
    cond.title("Condensers")
    cond.geometry("600x200")
    cond.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    
    # ---------------------------------Entries------------------------------
    cond_size = Entry(cond, width=30)
    cond_size.grid(row=0, column=1, padx=5)
    cond_model = Entry(cond, width=30)
    cond_model.grid(row=1, column=1, padx=5)
    cond_hp = Entry(cond, width=30)
    cond_hp.grid(row=2, column=1, padx=5)
    # ----------------------------------Text box labels---------------------
    cond_size_label = Label(cond, text="Condenser Size", pady=1)
    cond_size_label.grid(row=0, column=0)
    cond_model_label = Label(cond, text="Condenser Model", pady=1)
    cond_model_label.grid(row=1, column=0)
    cond_hp_label = Label(cond, text="Condenser HP", pady=1)
    cond_hp_label.grid(row=2, column=0)
    # -------------------------------Save Button----------------------------
    save_text = "Saved Condenser HP"
    save_button = Button(cond, text=save_text, command=cond_save)
    save_button.grid(row=4, column=0, columnspan=1, pady=5, padx=5, ipadx=60)
    # ------------------------------Autofill Button-------------------------
    fill = "Auto complete based on model name"
    fill_button = Button(cond, text=fill, command=cond_autofill)
    fill_button.grid(row=4, column=1, columnspan=1, pady=5, padx=5, ipadx=60)
    # -----------------------------Key Bindings-----------------------------
    cond.bind_all("<Control-a>", cond_autofill)
    cond.bind_all("<Control-s>", cond_save)
    
    cond.mainloop()
    

def cond_autofill():
    record_id = cond_model.get()
    sql = f"SELECT * FROM {tb} where model = '{cond_model.get()}'"
    print(sql)
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        cond_size.insert(0, record[1])
        cond_hp.insert(0, record[2])


def cond_save():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to save data to database?"
    )
    if answer == "yes":
        try:
            sql = f"""INSERT INTO {tb} {cond_size, cond_hp} VALUES
                   ('{cond_size.get()}', '{cond_hp.get()}')"""
            print(sql)
            cur.execute(sql)
            cond_size.delete(0, END)
            cond_hp.delete(0, END)
            cond.destroy()
        except Except as e:
            print(f"This is what is happening with this bad boy: {e}")
            
    else:
        pass
