import os
from tkinter import *
from tkinter import filedialog, scrolledtext
import tkinter.messagebox

import pandas as pd
import psycopg2

tb = "parts_db"

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


def parts_db():
    # --------------------------------------- Global Vars -------------------------------------------------------
    global parts
    global part_num
    # ---------------------------------------Other Stuff---------------------------------------------------------
    parts = Tk()
    parts.title("Parts")
    parts.geometry("400x200")
    parts.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    # ------------------------------------------------Entries-----------------------------------------------------
    part_num = Entry(parts, width=30)
    part_num.grid(row=0, column=1, padx=5)
    part_name = Entry(parts, width=30)
    part_name.grid(row=1, column=1, padx=5)
    part_num_label = Label(parts, text="Part Number", pady=1)
    part_num_label.grid(row=0,column=0)
    part_name_label = Label(parts, text="Part Name", pady=1)
    part_name_label.grid(row=1,column=0)
    # -------------------------------------------- Save Button ---------------------------------------------------
    save_text = "Save Part in Database"
    save_button = Button(parts, text=save_text, command=parts_save)
    save_button.grid(row=3, column=1, columnspan=1, pady=5, padx=5, ipadx=80)
    # -------------------------------------------Key Bindings------------------------------------------------------
    parts.bind_all("<Control-s>", parts_save)
    
    parts.mainloop()

    

def parts_save():
    # sql = f"""INSERT INTO {tb} {cond_size, cond_hp} VALUES
    #       ('{cond_size.get()}', '{cond_hp.get()}')"""
    # print(sql)
    # cur.execute(sql)
    # cond_size.delete(0, END)
    # cond_hp.delete(0, END)
    print("Figure out what needs to be added here.")
    parts.quit()
    parts.destroy()
    #answer = tkinter.messagebox.askquestion(
    #    "G & D Chillers", "Are you sure you want to save data to database?"
    #)
    #if answer == "yes":
    #    try:
    #        sql = f"""INSERT INTO {tb} (cond_size, cond_hp) VALUES
    #               ('{cond_size.get()}', '{cond_hp.get()}')"""
    #        print(sql)
    #        cur.execute(sql)
    #        conn.commit()
    #        cond_size.delete(0, END)
    #        cond_hp.delete(0, END)
    #        parts.destroy()
    #    except Exception as e:
    #        print(f"This is what is happening with this bad boy: {e}")
    #        
    #else:
    #    pass
