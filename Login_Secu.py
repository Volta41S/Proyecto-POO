import tkinter
import pymysql
#import cv2
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def menu_Inicio():
    global Inicio
    Inicio=Tk()
    Inicio.geometry("350x350")
    Inicio.title("Iniciar sesión")
    #Inicio.config(background="white")
    Inicio.iconbitmap("logotecnica.ico")
    Inicio.resizable(0,0)
    #foto1 = cv2.imread('logotecnica.png',0)
    #cv2.imshow('logotecnica.ong',foto1)
   
    #label1.place(x = 0, y = 0)  label1 = 
    foto = Image.open("logotecnica1.png")
    resize_image = foto.resize((350,346))
    img = ImageTk.PhotoImage(resize_image)
    label1=Label( Inicio, image = img)
    label1.place(x=0,y=4)

    Label(text="Bienvenido a la herramienta KZAJJPJ",bg="#8B1C0E", fg="white", width="300", height="1", font=("Arial", 15)).pack()
    #Label().pack()

    #Label(bg="white").pack()

    btn1=Button(bg="#8B1C0E", fg="white", text="Iniciar sesión", height="2", width="15", command=Inicio_sesion)
    btn1.place(x=115, y= 150)
    label2=Label(text="o", bg="white", fg="black", font=("Arial"))
    label2.place(x=165, y= 200)
    btn2=Button(bg="#8B1C0E", fg="white", text="Cerrar", height="2", width="15", command=Cerrar_ventana)
    btn2.place(x=115, y=230)
    #place(x=160, y=175)
    #Inicio.wm_attributes("-transparentcolor", 'grey')
    Inicio.mainloop()

def Inicio_sesion():
    Inicio.withdraw()
    
    global InicioS
    InicioS = Toplevel(Inicio)
    InicioS.geometry("350x350")
    InicioS.title("Iniciar sesion")
    InicioS.config(background="white")
    InicioS.iconbitmap("logotecnica.ico")
    InicioS.resizable(0,0)

    Label(InicioS, text="Por favor, ingrese su Usuario y Contraseña a continuación:", bg="white", font=("Arial", 9)).pack()
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