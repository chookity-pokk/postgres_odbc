from tkinter import *
import psycopg2
import pandas as pd
import tkinter.messagebox
import postgres_odbc as pod

"""
This is a document to refactor the mistakes I made with the other 
tkinter gui. I am not writing the functions in here unless it is
necessary as I instead will just be importing them.
"""
# Connection modules
root = Tk()
root.title("G&D Chillers")
#This can be changed to any .ico files (use png or jpeg to ico converter online)
#It shows up in the top left corner of the display window.
# TODO: Needs to be added to all the windows.
root.iconbitmap(r"C:\Users\Hank\Documents\Random Python Scripts\postgres-odbc\Icons\IconForTkinter.ico")
root.geometry('400x400')
tb = 'guitable'
column_change = 'testing'
fieldnames=['first_name', 'last_name']


def add_to_csv():

    def csv():
        sql1 = """ SELECT * FROM {}""".format(tb)
        rows = cur.execute(sql1)
        col_headers = [ i[0] for i in cur.description ]
        rows = [ list(i) for i in cur.fetchall()]
        df = pd.DataFrame(rows, columns=col_headers)
        path = r"C:\Users\Hank\Documents\Random Python Scripts\GUI and Tkinter\ "
        name = str(csv_name.get())+".csv"
        df.to_csv(path + name, index=False)
        csv_name.delete(0,END)
        tkinter.messagebox.showinfo("G&D Chillers", "Your data has been exported to "+ path+name)
    """
    This function will take the contents of the table in PostgreSQL
    and put them to a csv. May be needed if peole want to externally save the
    contents of the database in a public place that people can easily access
    i.e. pushing the csv to a public folder for the company to look at.
    """

    answer = tkinter.messagebox.askquestion("G & D Chillers", 'Are you sure you want to export data to a CSV?')

    if answer == 'yes':
        csv_add = Tk()
        csv_add.title("Update a record")
        csv_add.geometry('300x300')
        csv_name = Entry(csv_add, width=30)
        csv_name.grid(row=0,column=3, padx=5)
        added_csv_name = csv_name.get()
        csv_name_label = Label(csv_add, text="Add CSV Name", pady=1)
        csv_name_label.grid(row=2,column=3)
        csv_lab = "Print out to a CSV(Excel)"
        #path = r"C:\Users\Hank\Documents\Random Python Scripts\GUI and Tkinter\ "+csv_name.get()+".csv"
        #added_csv_name = csv_name.get()
        csv_button = Button(csv_add,text=csv_lab, command=csv)
        csv_button.grid(row=3,column=3, columnspan=2, pady=5, padx=5, ipadx=66)

        #Don't want this, I just want a box that will have an input and say
        # "What do you want this named?" and it will then use .get() and put that
        # at the end of the pth above and then put this window up asking if they are sure.
        #question = tkinter.messagebox.askquestion("G&D Chillers", "What would you like to name this CSV?")


    else:
        pass

    







def csv_add_button():
    answer = tkinter.messagebox.askquestion("G & D Chillers", 'Are you sure you want to export data to a CSV?')

# ---------------Entry for database. create text boxes-------------------------
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=5)

l_name = Entry(root, width=30)
l_name.grid(row=1,column=1, padx=5)

#can be changed to use for taking inventory out or putting it in
edit_quant = Entry(root, width=30)
edit_quant.grid(row=2, column=1, padx=5)

# ---------------Create text box label-----------------------------------------
f_name_label = Label(root, text="First Name", pady=1)
f_name_label.grid(row=0,column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

edit_quant_label = Label(root, text="ID number")
edit_quant_label.grid(row=2, column=0)

get_f = f_name.get()
get_l = l_name.get()
get_edit_quant = edit_quant.get()

# -------------Create buttons to submit data------------------------------------
#Submits data to the database then clears the data.
sub = "Add record to database"
submit_button = Button(root,text=sub, command=add_to_row)
submit_button.grid(row=6,column=0, columnspan=2, pady=5,padx=5, ipadx=100)

# ----------------------Creat query button--------------------------------------
#This will show all the records in the database, probably not useful.
que = "See records"
que_button = Button(root, text=que, command=query)
que_button.grid(row=8, column=0,columnspan=2,pady=5,padx=5,ipadx=131)

#---------------------Edit quantity button--------------------------------------
edit = "Edit Record"
edit_button = Button(root, text=edit, command=edit_quantity)
edit_button.grid(row=10, column=0,columnspan=2,pady=5,padx=5,ipadx=130)

#-------------------Create buttons to delete data-------------------------------
"""
Make a window pop up saying that the data will be deleted and are you sure?
"""
erase = "Delete record from database"
del_button = Button(root,text=erase, command=delete)
del_button.grid(row=11,column=0, columnspan=2, pady=5,padx=5, ipadx=85)


# ----------------Print out CSV button------------------------------------------
"""
When you print out to CSV make a window pop up saying that
the data has successfully been exported to a csv.
"""
csv_lab = "Print out to a CSV(Excel)"
csv_button = Button(root,text=csv_lab, command=add_to_csv)
csv_button.grid(row=7,column=0, columnspan=2, pady=5, padx=5, ipadx=97.5)


#This will make it so the window can't be resized. Might be worth doing if I
# Can't figure out how to make it change dynamically with grid.
root.resizable(0,0)
root.mainloop()
