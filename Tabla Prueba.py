from tkinter import ttk

import tkinter as tk
from tkinter import *

import pymysql

"""def connect():

    con1 = sqlite3.connect("<path/database_name>")

    cur1 = con1.cursor()

    cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

    con1.commit()

    con1.close()

# connect to the database

def Ventana():

    root = tk.Tk()
    global tree
    tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="ID")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="Materia")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="Creditos")

    tree.column("#4", anchor=tk.CENTER)

    tree.heading("#4", text="Semestre")

    tree.pack()

    button1 = tk.Button(text="Display data", command=view)

    button1.pack(pady=10)

    root.mainloop()

"""
def view():
    my_w = tk.Tk()
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="SQLATb3ar2019",
        db="escuela008"
        )
    fcursor=bd.cursor()

    fcursor.execute("SELECT * FROM materia;")

    """row = fcursor.fetchall()
    for row in fcursor:

        print(row) 

        tree.insert("", tk.END, values=row)"""

    
####### end of connection ####
    
    i=0 
    for student in fcursor: 
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    my_w.mainloop()
        
    bd.close() 

view()

