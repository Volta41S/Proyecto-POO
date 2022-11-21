from tkinter import *
from tkinter import ttk
import tkinter as tk


def VerCFinal():
    Final=Tk()
    Final.title("Calificaciones finales")
    Final.geometry("1200x600")
    Final.iconbitmap("logotecnica.ico")
    Final.config(background="white")
    Final.resizable(0,0)

    global tree3

    tree3 = ttk.Treeview(Final, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings')

    tree3.column("#1", anchor=tk.CENTER, width=110)

    tree3.heading("#1", text="Folio de Alumno")

    tree3.column("#2", anchor=S)

    tree3.heading("#2", text="N.L.")

    tree3.column("#3", anchor=tk.CENTER)

    tree3.heading("#3", text="Nombre")

    tree3.column("#4", anchor=tk.CENTER)

    tree3.heading("#4", text="Trimestre 1")

    tree3.column("#5", anchor=tk.CENTER)

    tree3.heading("#5", text="Trimestre 2")

    tree3.column("#6", anchor=tk.CENTER)

    tree3.heading("#6", text="Trimestre 3")

    tree3.column("#7", anchor=tk.CENTER)

    tree3.heading("#7", text="Calificación final")

    tree3.place(x=80, y=130, width=1000, height=350)

    scroll_databaseH = Scrollbar(Final, orient="horizontal", command=tree3.xview)
    scroll_databaseH.place(x=80, y=480, width=1000)
    tree3.configure(xscrollcommand=scroll_databaseH.set)

    button1 = tk.Button(Final,text="Regresar",bg="#8B1C0E", fg="white")
    button1.place(x=80, y=550)

    Final.mainloop()
VerCFinal()