import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

def Menu_Secundario():
    global Menu
    Menu=Tk()
    Menu.geometry("1200x700")
    Menu.title("Herramienta KZAJPJ - Menu principal")
    #Menu.resizable(0,-30)
    """style = ttk.Style()
    style.configure("BW.TLabel", foreground="white", background="#8B1C0E") 
    style = ttk.Style()
    style.map("C.TButton",
    foreground=[('!disabled', 'white'), ('active', 'black')],
    background=[('!disabled', '#8B1C0E'), ('active', '#8B1C0E')], padding=3)"""

    Menu.configure(background="white")
    Label(Menu, text="Acceso al sistema", bg="white", fg="black", width="300", height="3", font=("Arial", 15)).pack()
    #Label(text="").pack()
    
    #btn1=ttk.Button(Menu, style="C.TButton", text="Seleccionar")
    btn1=Button(Menu,bg="#8B1C0E", fg="white", text="Seleccionar", height="2", width="15")
    btn1.place(x=1000, y= 600)
    #Label(text="").pack()
    bt2=Button(Menu, bg="#8B1C0E", text="Agregar", fg="white", height="2", width="15")
    bt2.place(x=1000, y=30)
    btn3=Button(Menu, text="Configuración", width="10", command=Configuracion)
    btn3.place(x=15, y=600)

    Menu.mainloop()


def Configuracion():
    global settings
    settings=Toplevel(Menu)
    settings.geometry("350x380")
    settings.title("Configuración")
    settings.configure(background="white")
    #foto=ImageTk.PhotoImage(Image.open("logotecnica.png"))

    Label(settings, text="Hola").pack()
    #background=Label(Config, image=ImageTk.PhotoImage(Image.open("logotecnica.png")), text="")
    #background.place(x=0, y=0)
    #Config.configure(background=Label1)


Menu_Secundario()