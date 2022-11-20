import tkinter as tk
import pymysql
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import scrolledtext as st
from PIL import ImageTk, Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



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

    #nombreusuario_verify=StringVar()
    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(InicioS, text="Folio", bg="white").pack()
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
    try:
        bd=pymysql.connect(
            host="localhost",
            user="kzajjpj",
            passwd="",
            db="secundaria39Demo6"
            )
        fcursor=bd.cursor()
        fcursor.execute("SELECT contraseña_ma FROM maestro WHERE codigo_ma="+nombreusuario_verify.get()+" and contraseña_ma='"+contrasenausuario_verify.get()+"'")

        if fcursor.fetchall():
            messagebox.showinfo(title="Inicio de sesion correcto", message= "Folio y contraseña correcta")
            InicioS.destroy()
            Menu_Secundario()

        else:
            messagebox.showerror(title="Inicio de sesion incorrecto", message= "Folio y/o contraseña incorrecta")

        bd.close()
    except:
        messagebox.showerror(title="Error", message= "No se pudo establecer conexion.")
    
def Cerrar_registro():
    Inicio.deiconify()
    InicioS.destroy()

def Menu_Secundario():
    global Menu
    Menu=Toplevel(Inicio)
    Menu.geometry("1200x700")
    Menu.title("Herramienta KZAJPJ - Menu principal")
    foto = tk.PhotoImage(file="images1.png")
    Menu.iconbitmap("logotecnica.ico")
    Menu.configure(background="white")
    Menu.resizable(0,0)
    global tree
    
    tree = ttk.Treeview(Menu, column=("c1", "c2", "c3","c4","c5"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="Codigo Materia")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="Materia")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="Hora")

    tree.column("#4", anchor=tk.CENTER)

    tree.heading("#4", text="Grupo")

    tree.column("#5", anchor=tk.CENTER)

    tree.heading("#5", text="Clave")
    #tree.bind("<<TreeviewSelect>>", on_tree_select)

    tree.place(x=150, y=130, width=800)
    scroll_databaseH = Scrollbar(Menu, orient="horizontal", command=tree.xview)
    scroll_databaseH.place(x=150, y=350, width=800)
    tree.configure(xscrollcommand=scroll_databaseH.set)
    item = tree.identify_row(0)
    tree.selection_set(item)
    tree.focus(item)
    
    button1 = tk.Button(Menu,text="Cargar", command=view, bg="#8B1C0E", fg="white")
    button1.place(x=100, y=100)
    
    Label(Menu, text="Menu principal", bg="white", fg="black", width="300", height="3", font=("Arial", 15)).pack()
    foto2 = Image.open("logotecnica.png")
    resize_image = foto2.resize((70,70))
    img = ImageTk.PhotoImage(resize_image)
    label1=Label(Menu, image = img)
    label1.place(x=10,y=5)
       
    #btn1=Button(Menu,bg="#8B1C0E", fg="white", text="Seleccionar", height="2", width="15", command=Seleccionar_g)
    #btn1.place(x=1000, y= 600)
    
    #bt2=Button(Menu, bg="#8B1C0E", text="Agregar", fg="white", height="2", width="15", command=Agregar_grupo)
    #bt2.place(x=1000, y=30)
    btn_C=ttk.Button(Menu, image= foto, command=Configuracion)
    btn_C.place(x=15, y=600)

    Menu.mainloop()

def view():
    
    bd=pymysql.connect(
        host="localhost",
        user="kzajjpj",
        passwd="",
        db="secundaria39Demo6"
        )
    fcursor=bd.cursor()

    fcursor.execute("SELECT codigo_mat, nombre_mat, Hora, Grupo, clave_clase FROM clases WHERE codigo_ma="+nombreusuario_verify.get())
    tree.delete(*tree.get_children())
    
    
    for fila in fcursor:
        tree.insert("",END, values=(fila[0],fila[1],fila[2], fila[3], fila[4]))
        tree.bind("<Double-1>", rama_seleccionada)
          
    bd.close() 

def rama_seleccionada(event):
    current_item = tree.focus()
    if not current_item:
        return
    #data = StringVar()
    data = tree.item(current_item)
    global id, codigo_mat, nombre_mat, Hora, Grupo, Clave
    
    codigo_mat, nombre_mat, Hora, Grupo, Clave = data["values"]
    #print(Clave)
    #ident.insert(0,"%i"%id)
    #print(id, nombre, creditos, semestre)
    
    Seleccionar_g()

def Configuracion():
    global settings
    settings=Toplevel(Menu)
    settings.geometry("350x380")
    settings.title("Configuración")
    settings.configure(background="white")
    settings.iconbitmap("logotecnica.ico")
    settings.resizable(0,0) 

    foto = Image.open("logotecnica1.png")
    resize_image = foto.resize((350,346))
    img = ImageTk.PhotoImage(resize_image)
    label1=Label(settings, image = img)
    label1.place(x=0,y=0)
    
    Label(settings, text="Configuración", bg="white").pack()

    btn1=Button(settings, bg="#8B1C0E", fg="white", text="Cambiar contraseña", width="15", command=Ccontraseña)
    btn1.place(x=115, y=150)

    btn2=Button(settings, bg="#8B1C0E", fg="white", text="Reportar errores", width="15", command=RE)
    btn2.place(x=115, y=200)

    btn3=Button(settings, bg="#8B1C0E", fg="white", text="Cerrar sesión", width="15", command=Cerrar_sesion)
    btn3.place(x=115, y=250)

    Label(settings, text="Versión 1.0.0", bg="white", fg="gray").place(x=125, y=360)

    settings.mainloop()

def Ccontraseña():
    global ccontra
    ccontra=Toplevel(settings)
    ccontra.geometry("350x350")
    ccontra.title("Cambiar contraseña")
    ccontra.iconbitmap("logotecnica.ico")
    ccontra.configure(background="white")

    foto = Image.open("logotecnica1.png")
    resize_image = foto.resize((350,346))
    img = ImageTk.PhotoImage(resize_image)
    label1=Label(ccontra, image = img)
    label1.place(x=0,y=0)

    Label(ccontra, text="Cambiar contraseña", bg="white").pack()
    label2 = Label(ccontra, text="Folio : "+nombreusuario_verify.get()+"", bg="white")
    label2.place(x=100, y=60)

    global nuevacontrasena_verify
    global cnuevacontrasena_verify

    nuevacontrasena_verify=StringVar()
    cnuevacontrasena_verify=StringVar()

    global nuevacontrasena_entry
    global cnuevacontrasena_entry

    nuevacontrasena_entry = Entry(ccontra, textvariable= nuevacontrasena_verify, borderwidth=1, relief="solid", show="*")
    nuevacontrasena_entry.place(x=150, y= 100)
    label3 = Label(ccontra, text="Contraseña nueva:", bg="white")
    label3.place(x=35, y=100)
    cnuevacontrasena_entry = Entry(ccontra, textvariable= cnuevacontrasena_verify, borderwidth=1, relief="solid", show="*")
    cnuevacontrasena_entry.place(x=150, y= 140)
    label4 = Label(ccontra, text="Confirmar contraseña:", bg="white")
    label4.place(x=20, y=140)

    btn1 = Button(ccontra, text="Cambiar", width="10", bg="#8B1C0E", fg="white", command=Nueva_contraseña)
    btn1.place(x=115, y=190)

    btn2 = Button(ccontra, text="Cancelar", width="10", bg="#8B1C0E", fg="white", command=ccontra.destroy)
    btn2.place(x=115, y=230)

    ccontra.mainloop()

def Nueva_contraseña():
    if (len(nuevacontrasena_verify.get())>5 and len(nuevacontrasena_verify.get())<9):
        if nuevacontrasena_verify.get() == cnuevacontrasena_verify.get():
            if nuevacontrasena_verify.get() != contrasenausuario_verify.get():
                try:
                    bd=pymysql.connect(
                        host="localhost",
                        user="kzajjpj",
                        passwd="",
                        db="secundaria39Demo6"
                    )
                    fcursor=bd.cursor()
                    fcursor.execute("UPDATE maestro SET contraseña_ma='"+nuevacontrasena_verify.get()+"' WHERE codigo_ma="+nombreusuario_verify.get())
                    bd.commit()
                    messagebox.showinfo(title="Operación exitosa", message= "El cambio de contraseña se realizo exitosamente.")
                    bd.close()
                    contrasenausuario_verify.set(nuevacontrasena_verify.get())
                    nuevacontrasena_verify.set("")
                    cnuevacontrasena_verify.set("")
                except:
                    messagebox.showerror(title="Error", message= "No se pudo establecer conexion.")
            else:
                messagebox.showwarning(title="Advertencia", message= "La nueva contraseña no puede ser igual a la actual.")
        else:
            messagebox.showerror(title="Error", message= "Debe ingresar la misma contraseña en ambos campos.")
    else:
        messagebox.showerror(title="Advertencia", message= "La contraseña debe ser de al menos 6 caracteres y un maximo de 8 caracteres.")

def Cerrar_sesion():
    Inicio.deiconify()
    Menu.destroy()
    
def Seleccionar_g():
    Menu.withdraw()
    global seleccion
    seleccion=Toplevel(Menu)
    seleccion.title("Grupo seleccionado")
    seleccion.iconbitmap("logotecnica.ico")
    seleccion.config(width=550,height=350,padx=10,pady=20)
    seleccion.config(background="white")
    seleccion.resizable(0,0)
    global Trimestre
    #Trimestre = int()
    Tit1=Label(seleccion,text=nombre_mat,font=("Arial",20), bg="white")
    Tit1.grid(column=0,row=0,columnspan=5,padx=30,pady=10)
    CodGru_label=Label(seleccion,text="Calificaciones Grupo %s"%Grupo,font=("Arial",15), bg="white")
    CodGru_label.grid(column=0,row=1,columnspan=5,padx=32,pady=10)

    PriTri_boton=Button(seleccion,text="1er trimestre", bg="#8B1C0E",fg="white", command=Tri_1)
    PriTri_boton.grid(column=0,row=2,padx=0,pady=10)

    SegTri_boton=Button(seleccion,text="2do trimestre",bg="#8B1C0E",fg="white", command=Tri_2)
    SegTri_boton.grid(column=1,row=2,padx=0,pady=10)

    TerTri_boton=Button(seleccion,text="3er trimestre",bg="#8B1C0E",fg="white", command=Tri_3)
    TerTri_boton.grid(column=2,row=2,padx=10,pady=10)

    Prom_boton=Button(seleccion,text="Promedio del ciclo escolar",bg="#8B1C0E",fg="white", command=FinalC)
    Prom_boton.grid(column=0,row=3,columnspan=5, padx=50,pady=10)

    Reg_boton=Button(seleccion,text="Regresar",bg="#8B1C0E",fg="white", command=Rmenu)
    Reg_boton.grid(column=0,row=4,padx=20,pady=10)

    seleccion.mainloop()
def Rmenu():
    seleccion.destroy()
    Menu.deiconify()

def Tri_1():
    global Trimestre
    Trimestre = 1
    seleccion.withdraw()
    C_Trimestre()
    
def Tri_2():
    global Trimestre
    Trimestre = 2
    seleccion.withdraw()
    C_Trimestre()
    
def Tri_3():
    global Trimestre
    Trimestre = 3
    seleccion.withdraw()
    C_Trimestre()
    
def FinalC():
    seleccion.withdraw()
    VerCFinal()


def C_Trimestre():
    global Cali
    Cali=Toplevel(Menu)
    Cali.title("Calificaciones del Trimestre %i"%Trimestre)
    Cali.geometry("1500x800")
    Cali.iconbitmap("logotecnica.ico")
    Cali.config(background="white")
    Cali.resizable(0,0)
    global tree2
    global Folio_entry
    global valor_entry, combo
    Label(Cali, text="Calificaciones del trimestre %i del grupo %s en la materia %s"%(Trimestre, Grupo, nombre_mat), bg="white", font=(("Arial"),20)).pack()
    tree2 = ttk.Treeview(Cali, column=("c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14","c15"), show='headings')
    tree2.column("#1", anchor=tk.CENTER)

    tree2.heading("#1", text="Folio_alu")

    tree2.column("#2", anchor=tk.CENTER)

    tree2.heading("#2", text="N.L.")

    tree2.column("#3", anchor=tk.CENTER)

    tree2.heading("#3", text="Nombre del alumno")

    tree2.column("#4", anchor=tk.CENTER)

    tree2.heading("#4", text="Act_1")

    tree2.column("#5", anchor=tk.CENTER)

    tree2.heading("#5", text="Act_2")

    tree2.column("#6", anchor=tk.CENTER)

    tree2.heading("#6", text="Act_3")

    tree2.column("#7", anchor=tk.CENTER)

    tree2.heading("#7", text="Act_4")

    tree2.column("#8", anchor=tk.CENTER)

    tree2.heading("#8", text="Act_5")

    tree2.column("#9", anchor=tk.CENTER)

    tree2.heading("#9", text="Act_6")

    tree2.column("#10", anchor=tk.CENTER)

    tree2.heading("#10", text="Act_7")

    tree2.column("#11", anchor=tk.CENTER)

    tree2.heading("#11", text="Act_8")

    tree2.column("#12", anchor=tk.CENTER)

    tree2.heading("#12", text="Act_9")

    tree2.column("#13", anchor=tk.CENTER)

    tree2.heading("#13", text="Act_10")

    tree2.column("#14", anchor=tk.CENTER)

    tree2.heading("#14", text="Examen")

    tree2.column("#15", anchor=tk.CENTER)

    tree2.heading("#15", text="Promedio de trimestre")
    
    tree2.place(x=100, y=100, width= 1300)
    Obtener_c()

    scroll_databaseH = Scrollbar(Cali, orient="horizontal", command=tree2.xview)
    scroll_databaseH.place(x=100, y=320, width=1300)
    tree2.configure(xscrollcommand=scroll_databaseH.set)
    item = tree2.identify_row(0)
    tree2.selection_set(item)
    tree2.focus(item)

    combo = ttk.Combobox(Cali,state="readonly",
    values = ["act_1","act_2","act_3","act_4","act_5","act_6","act_7","act_8","act_9","act_10","Examen"])
    combo.bind("<<ComboboxSelected>>", Obtener_co)
    combo.place(x=700, y=440)
    Button(Cali, bg="#8B1C0E", fg="white", text="Cerrar",width="10", command=Cerrar_T).place(x=30, y=700)
    Label(Cali, text="Folio del Alumno:", bg="white").place(x=590, y=400)
    Folio_entry=Entry(Cali, textvariable = "", borderwidth=1, relief="solid")
    Folio_entry.place(x=700, y=400)
    Label(Cali, text="Actividad:", bg="white").place(x=590, y=440)
    Label(Cali, text="Puntuación", bg="white").place(x=590, y=470)
    valor_entry=Entry(Cali, textvariable = "", borderwidth=1, relief="solid")
    valor_entry.place(x=700, y=470)
    btn1=Button(Cali, text="Guardar calificación", bg="#8B1C0E", fg="white", command=Guardar_C)
    btn1.place(x=620, y=500)


    Cali.mainloop()

def Obtener_co(event):
    global act
    act = combo.get()

def Obtener_c():
    try:
        bd=pymysql.connect(
            host="localhost",
            user="kzajjpj",
            passwd="",
            db="secundaria39Demo6"
            )
        fcursor=bd.cursor()

        fcursor.execute("SELECT folio_alu, no_lista, nombre_alumno, act_1, act_2,act_3,act_4,act_5,act_6,act_7,act_8,act_9,act_10, Examen, round(avg(act_1+act_2+act_3+act_4+act_5+act_6+act_7+act_8+act_9+act_10+Examen)/11, 0) FROM trimestre%i where clave_clase like '%s' group by clave_clase, folio_alu, no_lista, nombre_alumno;"%(Trimestre, Clave))
        tree2.delete(*tree2.get_children())
        
        
        for fila in fcursor:
            tree2.insert("",END, values=(fila[0],fila[1],fila[2], fila[3], fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12],fila[13],fila[14]))
            tree2.bind("<<TreeviewSelect>>", rama_seleccionada2)
            
        bd.close() 
    except:
        messagebox.showerror(title="Error", message= "No se pudo establecer conexion.")

def rama_seleccionada2(event):
    Folio_entry.delete(0,"end")
    current_item = tree2.focus()
    if not current_item:
        return
    #data = StringVar()
    data = tree2.item(current_item)
    global folio_alu, no_lista, nombre_alumno, act_1, act_2,act_3,act_4,act_5,act_6,act_7,act_8,act_9,act_10, Examen, Promedio
    
    folio_alu, no_lista, nombre_alumno, act_1, act_2,act_3,act_4, act_5, act_6,act_7, act_8, act_9, act_10, Examen, Promedio = data["values"]
    
    Folio_entry.insert(0,"%s"%folio_alu)
    #print("UPDATE trimestre%i SET %s= %s WHERE folio_alumno=%s and clave_clase like '%s'"%(Trimestre, combo.get(),valor_entry.get(), Folio_entry.get(), Clave))

def Guardar_C():
    try:
        value = float(valor_entry.get())
        if (Folio_entry.get().isdigit() and (not combo.get().isspace()) and (value>=0 and value<=100)):
            try:
                bd=pymysql.connect(
                    host="localhost",
                    user="kzajjpj",
                    passwd="",
                    db="secundaria39Demo6"
                )
                fcursor=bd.cursor()
                fcursor.execute("UPDATE trimestre%i SET %s= %s WHERE folio_alu=%s and clave_clase like '%s';"%(Trimestre, combo.get(),valor_entry.get(), Folio_entry.get(), Clave))
                bd.commit()
                messagebox.showinfo(title="Operación exitosa", message= "El cambio de calificación se realizo exitosamente.")
                Obtener_c()
                
                fcursor.execute("UPDATE trimestre%i SET Promedio= (Select round(avg(act_1+act_2+act_3+act_4+act_5+act_6+act_7+act_8+act_9+act_10+Examen)/11, 0)) WHERE folio_alu=%s and clave_clase like '%s';"%(Trimestre, Folio_entry.get(), Clave))
                bd.commit()
                bd.close()
                
            except:
                messagebox.showerror(title="Error", message= "No se pudo establecer conexion.")
        else:
            messagebox.showwarning(title="Advertencia", message= "Debe llenar bien los campos, el campo de calificación debe tener valores positivos y menores o iguales a 100.")
    except:
        messagebox.showwarning(title="Advertencia", message= "Debe llenar bien los campos, el campo de calificación debe tener valores positivos y menores o iguales a 100.")

def VerCFinal():
    global Final
    Final=Toplevel(Menu)
    Final.title("Calificaciones finales")
    Final.geometry("1200x600")
    Final.iconbitmap("logotecnica.ico")
    Final.config(background="white")
    Final.resizable(0,0)

    Label(Final,text="Calificaciones finales del grupo %s en la materia %s"%(Grupo, nombre_mat), font=(("Arial"), 20), bg="white").pack()
    global tree3

    tree3 = ttk.Treeview(Final, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings')

    tree3.column("#1", anchor=tk.CENTER)

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

    button1 = tk.Button(Final,text="Regresar",bg="#8B1C0E", fg="white", command=Cerrar_F)
    button1.place(x=80, y=550)
    CCF()

    Final.mainloop()

def Cerrar_T():
    seleccion.deiconify()
    Cali.destroy()
def Cerrar_F():
    seleccion.deiconify()
    Final.destroy()


def CCF():
    try:
        bd=pymysql.connect(
            host="localhost",
            user="kzajjpj",
            passwd="",
            db="secundaria39Demo6"
            )
        fcursor=bd.cursor()

        fcursor.execute("select b.folio_alu, b.no_lista,b.nombre_alumno,b.Promedio Trimestre_1, c.Promedio Trimestre_2, d.Promedio Trimestre_3, round(avg(b.Promedio+c.Promedio+d.Promedio)/3,0) Final from Trimestre1 as b, Trimestre2 as c, Trimestre3 as d where (((b.folio_alu = c.folio_alu) and (c.folio_alu = d.folio_alu)))and (b.clave_clase like '%s'and ((b.clave_clase=c.clave_clase)and(c.clave_clase=d.clave_clase))) group by b.folio_alu, b.clave_clase;"%(Clave))
        tree3.delete(*tree3.get_children())
        
        
        for fila in fcursor:
            tree3.insert("",END, values=(fila[0],fila[1],fila[2], fila[3],fila[4],fila[5],fila[6]))
                        
        bd.close() 
    except:
        messagebox.showerror(title="Error", message= "No se pudo establecer conexion.")

def RE():
    Reporte=Toplevel(Menu)
    Reporte.title("Reporte de errores")
    Reporte.config(background="white")
    Reporte.iconbitmap("logotecnica.ico")
    Reporte.geometry("500x300")
    Reporte.resizable(0,0)
    
    global scrolledtext1
    Label(Reporte,text="Reporte de errores", bg="White", font=("Arial",15)).grid(column=0, row=0, padx=170, pady=0)
    Label(Reporte,text="Ingrese aqui los problemas que haya tenido", bg="White", font=("Arial",10)).grid(column=0, row=1, padx=100, pady=0)
    scrolledtext1=st.ScrolledText(Reporte, width=50, height=10, relief=SOLID)
    scrolledtext1.grid(column=0,row=2, padx=40, pady=0)
    Button(Reporte, text="Enviar", command=imprimir, bg="#8B1C0E", fg="white", width="10").grid(column=0, row=3, padx=200, pady=5)
    Button(Reporte, text="Regresar", command=Reporte.destroy, bg="#8B1C0E", fg="white", width="10").grid(column=0, row=4, padx=140, pady=5)
    
    Reporte.mainloop()

def imprimir():
    datos=StringVar()
    datos=scrolledtext1.get("0.0", tk.END)
    #print(datos)
    
    if not (datos.isspace()):
        try:
            msg = MIMEMultipart()
        
        
            message = datos
            
            # setup the parameters of the message
            password = "nwqfwdgfucljameu"
            msg['From'] = "herramientakzajjpj@gmail.com"
            msg['To'] = "angel.torresprd@uanl.edu.mx"
            msg['Subject'] = "Reporte de errores"
            
            # add in the message body
            msg.attach(MIMEText(message, 'plain'))
            
            #create server
            server = smtplib.SMTP('smtp.gmail.com: 587')
            
            server.starttls()
            
            # Login Credentials for sending the mail
            server.login(msg['From'], password)
            
            
            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            
            server.quit()
            messagebox.showinfo(title="Operacion exitosa", message= "El reporte se envio con exito")
            #print ("successfully sent email to %s:" % (msg['To']))
            #print(datos)
            scrolledtext1.delete("0.0", tk.END)
        except:
            messagebox.showerror(title="Error de conexion", message= "No se pudo contactar con el servidor")
        
        
    else:
        messagebox.showwarning(title="Mensaje no valido", message= "Debe ingresar texto")

Inicio_app()