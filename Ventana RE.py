from tkinter import *
from tkinter import messagebox
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from tkinter import scrolledtext as st

def RE():
    Reporte=tk.Tk()
    Reporte.config(background="white")
    Reporte.geometry("500x300")
    
    global scrolledtext1
    Label(Reporte,text="Reporte de errores", bg="White", font=("Arial",15)).grid(column=0, row=0, padx=170, pady=0)
    Label(Reporte,text="Ingrese aqui los problemas que haya tenido", bg="White", font=("Arial",10)).grid(column=0, row=1, padx=100, pady=0)
    scrolledtext1=st.ScrolledText(Reporte, width=50, height=10, relief=SOLID)
    scrolledtext1.grid(column=0,row=2, padx=40, pady=0)
    Button(Reporte, text="Enviar", command=imprimir, bg="#8B1C0E", fg="white").grid(column=0, row=3, padx=200, pady=5)
    
    
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
RE()