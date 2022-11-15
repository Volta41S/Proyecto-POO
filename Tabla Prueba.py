from tkinter import ttk

import tkinter as tk
from tkinter import *

import pymysql


# connect to the database

def Ventana():
    global root
    root = tk.Tk()
    root.geometry("1400x600")
    
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
    #tree.bind("<<TreeviewSelect>>", on_tree_select)

    tree.place(x=400, y=100)
    item = tree.identify_row(0)
    tree.selection_set(item)
    tree.focus(item)
    
    Button(root, text="Show Selected", command=item_opened).pack()
    button1 = tk.Button(text="Display data", command=view)
    """b1 = Button(
    root, 
    text="Browse",
    pady=20,
    command=selectmode_browse
    )
    b1.pack(side=LEFT, fill=X, expand=True)"""

    button1.pack(pady=10)

    

    root.mainloop()


def view():
    
    #my_w = tk.Tk()
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="SQLATb3ar2019",
        db="escuela008"
        )
    fcursor=bd.cursor()

    fcursor.execute("SELECT * FROM materia;")
    tree.delete(*tree.get_children())
    #fila = fcursor.fetchone()
   # tree.insert("", END, values=fila)
    
    for fila in fcursor:
        tree.insert("",END, values=(fila[0],fila[1],fila[2], fila[3]))
        tree.bind("<<TreeviewSelect>>", rama_seleccionada)
        #tree.tag_bind("<Double-1>", item_opened)
        #for j in range(len(fila)):
            #tree.grid(row=i, column=j) 
            
        


        #print(row) 

        

    bd.close() 
####### end of connection ####
    
   #i=0 
    """for student in fcursor: 
        for j in range(len(student)):
            e = Entry(my_w, width=30, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    my_w.mainloop()"""
        
def item_opened():
    x=tree.selection()
    Label(root, text=x, bg="blue", fg="white").pack()
    print(tree.selection)
    #iid = tree.selection()
    #item=tree.identify('item', event.x,event.y)
    #Label(root,text=tree.item(item,"text")).place(x=0, y=0)
    #Label(root,text="Hola").place(x=0, y=0)
   #input_id = tree.selection()
   #input_item = tree.item(input_id,"text")
   #from Login_Secu import Inicio_app

"""def selectmode_browse():
    tree['selectmode']="browse"""
def rama_seleccionada(event):
    current_item = tree.focus()
    if not current_item:
        return
    #data = StringVar()
    data = tree.item(current_item)
    global id, nombre, creditos, semestre
    id = StringVar()
    id, nombre, creditos, semestre = data["values"]
    print(id, nombre, creditos, semestre)
    Segunda_ventana()
    #Entry(root, textvariable = id, borderwidth=1, relief="solid").pack()
    #Entry(root, textvariable = Nombre, borderwidth=1, relief="solid").pack()
    #Entry(root, textvariable = creditos, borderwidth=1, relief="solid").pack()
    #Entry(root, textvariable = semestre, borderwidth=1, relief="solid").pack()
def Segunda_ventana():
    V2 = Toplevel(root)
    V2.geometry("1400x600")
    global tree2
    tree2 = ttk.Treeview(V2, column=("c1", "c2"), show='headings')

    tree2.column("#1", anchor=tk.CENTER)

    tree2.heading("#1", text="ID_alumno")

    tree2.column("#2", anchor=tk.CENTER)

    tree2.heading("#2", text="Calificación")

    
    tree2.place(x=400, y=100)
    Calificaciones()
    """item = tree2.identify_row(0)
    tree.selection_set(item)
    tree.focus(item)"""
    
    #Button(root, text="Show Selected", command=item_opened).pack()
    #button1 = tk.Button(text="Display data", command=view)
    #button1.pack(pady=10)

    

    V2.mainloop()

def Calificaciones():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="SQLATb3ar2019",
        db="escuela008"
        )
    fcursor=bd.cursor()

    fcursor.execute("SELECT matricula_id1 , calificacion From mat_alu, mat_pro, alumno WHERE (profe_id=1 AND materia_id1=%i AND matricula_id=matricula_id1) group by matricula_id1;"%(id))
    tree2.delete(*tree2.get_children())
    #fila = fcursor.fetchone()
   # tree.insert("", END, values=fila)
    
    for fila in fcursor:
        tree2.insert("",END, values=(fila[0],fila[1]))
        #tree2.bind("<<TreeviewSelect>>", rama_seleccionada)
       

    bd.close() 

Ventana()

