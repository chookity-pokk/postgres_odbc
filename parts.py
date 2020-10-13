from tkinter import *
from tkinter import filedialog, scrolledtext

import pandas as pd
import psycopg2

# import tkinterdataPsycop
# from tkinterdataPsycop import *

"""
May need to put this in its own
folder labeled 'Parts' just to 
organize the code
"""

#[] TODO
#Connect each of these part scripts to the database.

tb = "parts_db"
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
    part_num_label = Label(parts, text="Parts Number", pady=1)
    part_num_label.grid(row=0,column=0)
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

"""
parts = Tk()
parts.title("Parts")
parts.geometry("400x200")
parts.iconbitmap(
)
# ------------------------------------------------Entries-----------------------------------------------------
part_num = Entry(parts, width=30)
part_num.grid(row=0, column=1, padx=5)
part_num_label = Label(parts, text="Parts Number", pady=1)
part_num_label.grid(row=0,column=0)
# -------------------------------------------- Save Button ---------------------------------------------------
save_text = "Save Part in Database"
save_button = Button(parts, text=save_text, command=parts_save)
save_button.grid(row=3, column=1, columnspan=1, pady=5, padx=5, ipadx=80)
# -------------------------------------------Key Bindings------------------------------------------------------
parts.bind_all("<Control-s>", parts_save)

parts.mainloop()
"""
