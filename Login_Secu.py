import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def menu_Inicio():
    global Inicio
    Inicio=Tk()
    Inicio.geometry("350x400")
    Inicio.title("Iniciar sesión")
    Inicio.config(background="white")
    #Inicio.resizable(0,0)

    foto = ImageTk.PhotoImage(Image.open("logotecnica.png"))
    Label( Inicio, image = foto, fg="white", text="", font=("Arial", 15)).pack()
    
    #label1.place(x = 0, y = 0)  label1 = 

    Label(text="Bienvenido a la herramienta", bg="white", fg="black", width="300", height="3", font=("Arial", 13)).pack()
    Label(text="", bg="white").pack()

    Button(bg="#8B1C0E", fg="white", text="Iniciar sesión", height="2", width="15", command=Inicio_sesion).pack()
    Label(text="o", bg="white").pack()
    Button(bg="#8B1C0E", fg="white", text="Cerrar", height="2", width="15", command=Cerrar_ventana).pack()
    #place(x=160, y=175)

    Inicio.mainloop()

def Inicio_sesion():
    Inicio.withdraw()
    
    global InicioS
    InicioS = Toplevel(Inicio)
    InicioS.geometry("350x380")
    InicioS.title("Iniciar sesion")
    InicioS.config(background="white")

    Label(InicioS, text="Por favor, ingrese su Usuario y Contraseña a continuación", bg="white").pack()
    Label(InicioS, text="", bg="white").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(InicioS, text="Usuario", bg="white").pack()
    nombre_usuario_entry = Entry(InicioS, textvariable = nombreusuario_verify, borderwidth=1, relief="solid")
    nombre_usuario_entry.pack()
    Label(InicioS, bg="white").pack()

    Label(InicioS, text="Contraseña", bg="white").pack()
    contrasena_usuario_entry = Entry(InicioS, textvariable = contrasenausuario_verify, show= "*", borderwidth=1, relief="solid")
    contrasena_usuario_entry.pack()
    Label(InicioS, bg="white").pack()

    Button(InicioS, bg="#8B1C0E", fg="white", text="Iniciar sesion",width="10", command=validar_datos).pack()
    Label(InicioS, text="o", bg="white").pack()

    Button(InicioS, bg="#8B1C0E", fg="white", text="Regresar", width="10" ,command=Cerrar_registro).pack()
#height="2", width="15",
    
    

def validar_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="SQLATb3ar2019",
        db="Prueba"
        )
    fcursor=bd.cursor()
    fcursor.execute("SELECT contraseña FROM Profesor WHERE Nombre_p='"+nombreusuario_verify.get()+"' and contraseña='"+contrasenausuario_verify.get()+"'")

    if fcursor.fetchall():
         messagebox.showinfo(title="Inicio de sesion correcto", message= "Usuario y contraseña correcta")
         Inicio.destroy()
         from Menu import Menu_Secundario

    else:
        messagebox.showinfo(title="Inicio de sesion incorrecto", message= "Usuario y contraseña incorrecta")

    bd.close()

def Cerrar_ventana():
    Inicio.destroy()

def Cerrar_registro():
    Inicio.deiconify()
    InicioS.destroy()
        
menu_Inicio()