import os, sys
from tkinter import *
from tkinter import filedialog, scrolledtext
import tkinter.messagebox

import pandas as pd
import psycopg2

con_path = r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Archive"
sys.path.insert(1, con_path)

from postgres_db import connect_to_database

tb = "compressor_db"

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
        
    # --------------------------------------------Entries-------------------------------------------------------
    comp_model = Entry(comp, width=30)
    comp_model.grid(row=0, column=1, padx=5)
    comp_size = Entry(comp, width=30)
    comp_size.grid(row=1, column=1, padx=5)
    comp_hp = Entry(comp, width=30)
    comp_hp.grid(row=2, column=1, padx=5)
    # -----------------------------------------Text box labels--------------------------------------------------
    comp_model_label = Label(comp, text="Compressor Model", pady=1)
    comp_model_label.grid(row=0, column=0)
    comp_size_label = Label(comp, text="Compressor Size", pady=1)
    comp_size_label.grid(row=1, column=0)
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
    

def comp_autofill(event=None):
    record_id = comp_model.get()
    sql = f"SELECT * FROM {tb} where comp_model = '{comp_model.get()}'"
    print(sql)
    cur.execute(sql)
    records = cur.fetchall()
    for record in records:
        comp_size.insert(0, record[1])
        comp_hp.insert(0, record[2])


def comp_save():
    answer = tkinter.messagebox.askquestion(
        "G & D Chillers", "Are you sure you want to save data to database?"
    )
    if answer == "yes":
        try:
            sql = f"""INSERT INTO {tb} (comp_model, comp_size, comp_hp) VALUES 
                      ('{comp_model.get()}','{comp_size.get()}', {comp_hp.get()})"""

            print(sql)
            cur.execute(sql)
            conn.commit()
            comp_size.delete(0, END)
            comp_model.delete(0,END)
            comp_hp.delete(0, END)
            comp.quit()
            comp.destroy()
        except Exception as e:
            print(f"This is what is happening with this bad boy: \n {e}")
            
    else:
        pass


