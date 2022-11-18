from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import *

import pymysql


# connect to the database

def Ventana():
    global root
    root = tk.Tk()
    root.geometry("1400x600")
    #root.title("Prueba en ventana")
    #tk.LabelFrame(root,text="ventana de prueba", bg="#8B1C0E")
    #global combo
    #global results_for_combobox 
    #results_for_combobox = StringVar()
    B_maestros()
    global ident
    
    global tree
    tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="ID")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="Materia")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="Creditos")

    tree.column("#4", anchor=tk.CENTER)

    tree.heading("#4", text="Semestre")
    tree.column("#5", anchor=tk.CENTER)

    tree.heading("#5", text="Hola")
    #tree.bind("<<TreeviewSelect>>", on_tree_select)

    tree.place(x=200, y=100, width=600)
    scroll_databaseH = Scrollbar(root, orient="horizontal", command=tree.xview)
    scroll_databaseH.place(x=200, y=325, width=600)
    tree.configure(xscrollcommand=scroll_databaseH.set)

    item = tree.identify_row(0)
    tree.selection_set(item)
    tree.focus(item)
    ident=Entry(root, textvariable = "", borderwidth=1, relief="solid")
    ident.pack()
    
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
    
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="SQLATb3ar2019",
        db="escuela008"
        )
    fcursor=bd.cursor()

    fcursor.execute("SELECT * FROM materia;")
    tree.delete(*tree.get_children())
    
    
    for fila in fcursor:
        tree.insert("",END, values=(fila[0],fila[1],fila[2], fila[3]))
        tree.bind("<Double-1>", rama_seleccionada)
          
    bd.close() 
        
def item_opened():
    x=tree.selection()
    Label(root, text=x, bg="blue", fg="white").pack()
    print(tree.selection)
    
def rama_seleccionada(event):
    current_item = tree.focus()
    if not current_item:
        return
    #data = StringVar()
    data = tree.item(current_item)
    global id, nombre, creditos, semestre
    id = StringVar()
    id, nombre, creditos, semestre = data["values"]
    ident.insert(0,"%i"%id)
    print(id, nombre, creditos, semestre)
    
    Segunda_ventana()
    
    #Entry(root, textvariable = Nombre.get, borderwidth=1, relief="solid").pack()
    #Entry(root, textvariable = creditos.get, borderwidth=1, relief="solid").pack()
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
    V2.mainloop()

def Calificaciones():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="SQLATb3ar2019",
        db="escuela008"
        )
    fcursor=bd.cursor()

    fcursor.execute("SELECT matricula_id1 , calificacion From mat_alu, mat_pro, alumno WHERE (profe_id=%s AND materia_id1=%i AND matricula_id=matricula_id1) group by matricula_id1;"%(selection,id))
    tree2.delete(*tree2.get_children())
    #fila = fcursor.fetchone()
   # tree.insert("", END, values=fila)
    
    for fila in fcursor:
        tree2.insert("",END, values=(fila[0],fila[1]))
        #tree2.bind("<<TreeviewSelect>>", rama_seleccionada)
       

    bd.close() 

def B_maestros():
    global combo
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="SQLATb3ar2019",
        db="escuela008"
        )
    fcursor=bd.cursor()

    fcursor.execute("SELECT Prof_id FROM profesor;")
    fila = fcursor.fetchall()
    
    bd.close() 
    #tree2.bind("<<TreeviewSelect>>", rama_seleccionada)
    #tree2.delete(*tree2.get_children())
    #fila = fcursor.fetchone()
    # tree.insert("", END, values=fila)
    results_for_combobox = [result[0] for result in fila]
    
    combo = ttk.Combobox(root,state="readonly",
    values = results_for_combobox)
    combo.bind("<<ComboboxSelected>>", selection_changed)
    combo.place(x=50, y=50)

    
def selection_changed(event):
    global selection
    selection = combo.get()
    """messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )"""

Ventana()

