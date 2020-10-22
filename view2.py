from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, scrolledtext
import tkinter.messagebox
import psycopg2
import pandas as pd

con_path = r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Archive"
sys.path.insert(1, con_path)

from postgres_db import connect_to_database

conn, cur = connect_to_database()

"""
This is in alpha mode right now because 
I still need to get the scrollbar to work.
Not sure exactly what is going on and why
it isn't working.
"""


tb = "inv_testing3"

sql = f"SELECT * from {tb}"
cur.execute(sql)
rows = cur.fetchall()
total = cur.rowcount
print(f"Total Data Entries: {total}")

win = Tk()
frm = Frame(win)
# frm.pack(side=tk.LEFT, padx=20)
frm.grid(row=5, column=0)

# ---------------------Trying to style the Treeview--------------------
style = ttk.Style()
style.configure(
    "mystyle.Treeview", highlightthickness=0.5, bd=0, font=("Calibri", 11)
)  # Modify the font of the body
style.configure(
    "mystyle.Treeview.Heading", font=("Calibri", 13, "bold")
)  # Modify the heading font
style.layout(
    "mystyle.Treeview", [("mystyle.Treeview.treearea", {"sticky": "nswe"})]
)  # Remove borders
# ---------------------------------------------------------------------

tv = ttk.Treeview(
    frm,
    columns=(
        1,2,3,4,5,6,7,8,9,10,11,
        12,13,14,15,16,17,18,19,20,21,22,
        23,24,25,26,27,28,29,30,31,32,33,
    ),
    displaycolumns="#all",
    show="headings",
    selectmode="extended",
    style="mystyle.Treeview",
)
# tv.pack()
tv.grid(row=4, column=1, padx=5)

# https://docs.python.org/3/library/tkinter.ttk.html#scrollable-widget-options
# https://docs.python.org/3/library/tkinter.ttk.html#column-identifiers
# https://docs.python.org/3/library/tkinter.ttk.html
# https://docs.python.org/3/library/tkinter.ttk.html#treeview
names = [
    "1st",
    "2nd",
    "3rd",
    "4th",
    "5th",
    "6th",
    "7th",
    "8th",
    "9th",
    "10th",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "s",
    "w",
    "2",
    "a",
    "4",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "s",
    "w",
    "2",
    "4",
]

for i in range(33):
    tv.heading(i + 1, text=names[i])
    tv.column(i + 1, minwidth=0, width=150, stretch=NO)
# Actually using my head for once and just making the for loop above and using that instead of defining each thing individually.

# tv.heading(1,text="Name")
# tv.heading(2,text="Age")
# tv.heading(3,text="Email")
# tv.heading(4,text="Naem")
# tv.heading(5,text="sfld")
# tv.heading(6,text="120")
# tv.heading(7,text="jh")
# tv.heading(8,text="aksdf")
# tv.heading(9,text="s;df")
# tv.heading(10,text="ljd")

scrlbr = ttk.Scrollbar(win, orient="horizontal", command=tv.xview)
scrlbr.grid(row=10, column=3, columnspan=5)
# scrlbr.place(x=205, y=20, height=10)
# scrlbr.pack(side='bottom', fill='x')
# tv.configure(xscrollcommand=scrlbr.set)

for i in rows:
    tv.insert("", "end", values=i)

win.title("Customer Data")
win.geometry("700x300")

# win.resizable(False, False)
win.mainloop()
