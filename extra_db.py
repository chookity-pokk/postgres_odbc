import os
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog, scrolledtext

import pandas as pd
import psycopg2
#import tkinterdataPsycopg as T

# Probably need to change the window name because
# the window name is the same as the function name.

#[X]TODO: Break this up into multiple scripts.

"""
Planning on making this a script for editing the different
parts and whatnot.
"""
# These will probably need their whole own tkinter window
# So depending on the size these all might need to be their
# own scripts for the sake of being organized.


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


def save():
    print("Save")


def parts_save():
    print("Parts Savings")
    
def comp_save():
    print("Compressor Saving")


def cond_autofill():
    print("Autofill")


def comp_autofill():
    print("Compressor Autofill")


def db_switching():
    """
    Here's what needs to be in here, I need just a function 
    That will switch tb name and pull up a new tkinter window.
    """
    if tkvar.get() == "Condenser":
        edit_cond()
    if tkvar.get() == "Compressor":
        edit_comp()
    if tkver.get() == "Parts":
        edit_parts()
    # print("Opens")
    # global db_switching
    # db_switching = Tk()
    # db_switching.title("")
    pass


def edit_cond():
    # global edit_cond
    edit_cond = Tk()
    edit_cond.title("Condensers")
    edit_cond.geometry("700x300")
    edit_cond.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    # -------------------------------------- Entries ----------------------------------------------------------
    cond_size = Entry(edit_cond, width=30)
    cond_size.grid(row=0, column=1, padx=5)
    cond_model = Entry(edit_cond, width=30)
    cond_model.grid(row=2, column=1, padx=5)
    cond_hp = Entry(edit_cond, width=30)
    cond_hp.grid(row=2, column=1, padx=5)
    # --------------------------------------Text box labels ----------------------------------------------------
    cond_size_label = Label(edit_cond, text="Condenser Size", pady=1)
    cond_size_label.grid(row=0, column=0)
    cond_model_label = Label(edit_cond, text="Condenser Model", pady=1)
    cond_model_label.grid(row=1, column=0)
    cond_hp_label = Label(edit_cond, text="Condenser HP", pady=1)
    cond_hp_label.grid(row=2, column=0)
    # ------------------------------------Grabbing the info ----------------------------------------------------
    get_cond_size = cond_size.get()
    get_cond_model = cond_model.get()
    get_cond_hp = cond_hp.get()
    # ------------------------------------------Save button ----------------------------------------------------
    """
    Need to add the commands here and edit them properly
    """
    save_text = "Saved Condensor HP"
    save_button = Button(edit_cond, text=save_text, command=save)
    save_button.grid(row=5, column=1, columnspan=2, pady=5, padx=5, ipadx=100)
    # -----------------------------------------Autofill button--------------------------------------------------
    """
    Can't actually use autofill here because it is set to 
    a specific database.
    """
    fill = "Auto Complete Based on Condenser Name"
    fill_button = Button(edit_cond, text=fill, command=cond_autofill)
    fill_button.grid(row=5, column=3, columnspan=2, pady=5, padx=5, ipadx=115)
    # ----------------------------------------- Key Bindings ---------------------------------------------------
    edit_cond.bind_all("<Control-a>", cond_autofill)
    edit_cond.bind_all("<Control-s>", save)


def edit_comp():
    comp = Tk()
    comp.title("Compressors")
    comp.geometry("400x200")
    comp.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    # --------------------------------------------Entries--------------------------------------------------------
    comp_size = Entry(comp, width=30)
    comp_size.grid(row=0, column=1, padx=5)
    comp_model = Entry(comp, width)
    comp_model.grid(row=1, column=1, padx=5)
    comp_hp = Entry(comp, width=30)
    comp_hp.grid(row=2, column=1, padx=5)
    # -----------------------------------------Text box labels--------------------------------------------------
    comp_size_label = Label(comp, text="Compressor Size", pady=1)
    comp_size_label.grid(row=0, column=0)
    comp_model_label = Label(comp, text="Compressor Model", pady=1)
    comp_model_label.grid(row=1, column=0)
    comp_hp_label = Label(comp, text="Compressor HP", pady=1)
    # ----------------------------------------Save Button ------------------------------------------------------
    save_text = "Saved Compressor HP"
    save_button = Button(comp, text=save_text, command=comp_save)
    save_button.grid(row=5, column=1, columnspan=2, pady=5, padx=5, ipadx=100)
    # ----------------------------------------Autofill button --------------------------------------------------
    fill = "Autofill based on compressor name"
    fill_button = Button(comp, text=fill, command=comp_autofill)
    fill_button.grid(row=5, column=3, columnspan=2, pady=5, padx=5, ipadx=100)
    # ---------------------------------------- Key Bindings ----------------------------------------------------
    comp.bind_all("<Control-a>", comp_autofill)
    comp.bind_all("<Control-s>", save)


def edit_parts():
    parts = Tk()
    parts.title("Parts")
    part.geometry("400x200")
    part.iconbitmap(
        r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico"
    )
    # ------------------------------------------------Entries-----------------------------------------------------
    part_num = Entry(parts, width=30)
    part_num.grid(row=0, column=1, padx=5)
    # -------------------------------------------- Save Button ---------------------------------------------------
    save_text = "Save Part in Database"
    save_button = Button(parts, text=save_text, command=parts_save)
    save_button.grid(row=3, column=1, columnspan=1, pady=5, padx=5, ipadx=100)
    # -------------------------------------------Key Bindings------------------------------------------------------
    parts.bind_all("<Control-s>", parts_save)


#root.mainloop()

