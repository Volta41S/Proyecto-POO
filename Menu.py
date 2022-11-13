import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def Menu_Secundario():
    global Menu
    Menu=tk.Tk()
    Menu.geometry("1200x700")
    Menu.title("Herramienta KZAJPJ - Menu principal")
    foto = tk.PhotoImage(file="images1.png")
    #Menu.resizable(0,-30)
    
    Menu.configure(background="white")
    Label(Menu, text="Acceso al sistema", bg="white", fg="black", width="300", height="3", font=("Arial", 15)).pack()
    #Label(text="").pack()
    
    #btn1=ttk.Button(Menu, style="C.TButton", text="Seleccionar")
    btn1=Button(Menu,bg="#8B1C0E", fg="white", text="Seleccionar", height="2", width="15")
    btn1.place(x=1000, y= 600)
    #Label(text="").pack()
    bt2=Button(Menu, bg="#8B1C0E", text="Agregar", fg="white", height="2", width="15", command=Agregar_grupo)
    bt2.place(x=1000, y=30)
   # btn3=Button(Menu, text="Configuración", width="10", command=Configuracion)
   #btn3.place(x=15, y=600)

    btn_C=ttk.Button(Menu, image= foto, command=Configuracion)
    btn_C.place(x=15, y=600)

    Menu.mainloop()


def Configuracion():
    global settings
    settings=Toplevel(Menu)
    settings.geometry("350x380")
    settings.title("Configuración")
    settings.configure(background="white")
    settings.resizable(0,0) 
    
    Label(settings, text="Configuración", bg="white").pack()

    btn1=Button(settings, bg="#8B1C0E", fg="white", text="Cambiar contraseña", width="15")
    btn1.place(x=115, y=150)

    btn2=Button(settings, bg="#8B1C0E", fg="white", text="Reportar errores", width="15")
    btn2.place(x=115, y=200)

    Label(settings, text="Versión 1.0.0", bg="white", fg="gray").place(x=125, y=360)

def Agregar_grupo():
    #from AgregarGrupo import A_Grupo
    global AgreGrupo
    AgreGrupo=Toplevel(Menu)
    AgreGrupo.title("Agregar grupo")
    AgreGrupo.config(width=550,height=350,padx=10,pady=20)

    Tit1=Label(AgreGrupo,text="Agregar Grupo",font=("Arial",20))
    Tit1.grid(column=0,row=0,columnspan=5,pady=(0,10), padx=10)
    CodGru_label=Label(AgreGrupo,text="Codigo de grupo:",font=("Arial",10))
    CodGru_label.grid(column=1,row=1,pady=(0,10))
    NomGru_label=Label(AgreGrupo,text="Nombre de grupo:",font=("Arial",10))
    NomGru_label.grid(column=1,row=2,pady=(0,10), padx=10)

    CodGru=StringVar()
    CodGru_Entry = Entry(AgreGrupo, textvariable=CodGru, state="normal", width=15)
    CodGru_Entry.grid(column=2, row=1, sticky=W)

    NomGru=StringVar()
    NomGru_entry = Entry(AgreGrupo, textvariable=CodGru, state="normal", width=30)
    NomGru_entry.grid(column=2, row=2, columnspan=5,sticky=W)

    Bus_boton=ttk.Button(AgreGrupo,text="Buscar")
    Bus_boton.grid(column=3,row=1,sticky=E,padx=10)

    Can_boton=ttk.Button(AgreGrupo,text="Cancelar",command=AgreGrupo.destroy)
    Can_boton.grid(column=1,row=3,padx=10)

    Ace_boton=ttk.Button(AgreGrupo,text="Aceptar")
    Ace_boton.grid(column=2,row=3,padx=10,columnspan=2)

    espacioder_label = Label(AgreGrupo,width=5)
    espacioder_label.grid(column=5,row=0,rowspan=10,padx=2,columnspan=2)

    espacioizq_label = Label(AgreGrupo,width=5)
    espacioizq_label.grid(column=0,row=0,rowspan=10,padx=2)
   


Menu_Secundario()