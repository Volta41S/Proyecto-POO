from tkinter import*
from tkinter import ttk
import tkinter as tk


seleccion=tk.Tk()
seleccion.title("Grupo seleccionado")
seleccion.iconbitmap("logotecnica.ico")
seleccion.config(width=550,height=350,padx=10,pady=20)
seleccion.resizable(0,0)


Tit1=Label(seleccion,text="Nombre de grupo",font=("Arial",20))
Tit1.grid(column=0,row=0,columnspan=5,padx=(40,0),pady=10)
CodGru_label=Label(seleccion,text="Calificaciones",font=("Arial",15))
CodGru_label.grid(column=0,row=1,columnspan=5,padx=(40,0),pady=(10,43))

PriTri_boton=Button(seleccion,text="1er trimestre", bg="#8B1C0E",fg="white")
PriTri_boton.grid(column=0,row=2,padx=0,pady=10)

SegTri_boton=Button(seleccion,text="2do trimestre",bg="#8B1C0E",fg="white")
SegTri_boton.grid(column=1,row=2,padx=0,pady=10)

TerTri_boton=Button(seleccion,text="3er trimestre",bg="#8B1C0E",fg="white")
TerTri_boton.grid(column=2,row=2,padx=10,pady=10)

Prom_boton=Button(seleccion,text="Promedio del ciclo escolar",bg="#8B1C0E",fg="white")
Prom_boton.grid(column=0,row=3,columnspan=5, padx=(50,10),pady=10)

Reg_boton=Button(seleccion,text="Regresar",bg="#8B1C0E",fg="white", command=seleccion.destroy)
Reg_boton.grid(column=0,row=4,padx=20,pady=10)

espacioder_label = Label(seleccion,width=5)
espacioder_label.grid(column=5,row=0,rowspan=10,padx=2,)

espacioizq_label = Label(seleccion,width=5)
espacioizq_label.grid(column=0,row=0,rowspan=10,padx=2)

seleccion=mainloop()