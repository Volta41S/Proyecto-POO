import tkinter as tk
import pymysql
#import cv2
from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image


def Inicio_app():
    global Inicio
    Inicio=Tk()
    Inicio.geometry("350x350")
    Inicio.title("Iniciar sesión")
    #Inicio.config(background="white")
    Inicio.iconbitmap("logotecnica.ico")
    Inicio.resizable(0,0)

    foto = Image.open("logotecnica1.png")
    resize_image = foto.resize((350,346))
    img = ImageTk.PhotoImage(resize_image)
    label1=Label( Inicio, image = img)
    label1.place(x=0,y=4)

    Label(text="Bienvenido a la herramienta KZAJJPJ",bg="#8B1C0E", fg="white", width="300", height="1", font=("Arial", 15)).pack()
    
    btn1=Button(bg="#8B1C0E", fg="white", text="Iniciar sesión", height="2", width="15", command=Inicio_sesion)
    btn1.place(x=115, y= 150)
    label2=Label(text="o", bg="white", fg="black", font=("Arial"))
    label2.place(x=165, y= 200)
    btn2=Button(bg="#8B1C0E", fg="white", text="Cerrar", height="2", width="15", command=Inicio.destroy)
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

    foto = Image.open("logotecnica1.png")
    resize_image = foto.resize((350,346))
    img = ImageTk.PhotoImage(resize_image)
    label1=Label(InicioS, image = img)
    label1.place(x=0,y=4)

    Label(InicioS, text="Por favor, ingrese su Usuario y Contraseña a continuación:", bg="#8B1C0E",fg="white", font=("Arial", 9)).pack()
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
    InicioS.mainloop()
 
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
         InicioS.destroy()
         Menu_Secundario()

    else:
        messagebox.showinfo(title="Inicio de sesion incorrecto", message= "Usuario y contraseña incorrecta")

    bd.close()

def Cerrar_registro():
    Inicio.deiconify()
    InicioS.destroy()

def Menu_Secundario():
    global Menu
    Menu=Toplevel(Inicio)
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

    foto = Image.open("logotecnica1.png")
    resize_image = foto.resize((350,346))
    img = ImageTk.PhotoImage(resize_image)
    label1=Label(settings, image = img)
    label1.place(x=0,y=0)
    
    Label(settings, text="Configuración", bg="white").pack()

    btn1=Button(settings, bg="#8B1C0E", fg="white", text="Cambiar contraseña", width="15")
    btn1.place(x=115, y=150)

    btn2=Button(settings, bg="#8B1C0E", fg="white", text="Reportar errores", width="15")
    btn2.place(x=115, y=200)

    Label(settings, text="Versión 1.0.0", bg="white", fg="gray").place(x=125, y=360)

    settings.mainloop()

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
        
def Eliminar_grupo():
    global Eliminar
    
Inicio_app()