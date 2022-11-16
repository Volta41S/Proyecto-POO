from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st

def ventana_p():
    ventana1=tk.Tk()
    ventana1.geometry("500x500")
    global scrolledtext1
    scrolledtext1=st.ScrolledText(ventana1, width=50, height=10)
    scrolledtext1.grid(column=0,row=2, padx=40, pady=60)
    Button(text="imprimir", command=imprimir).grid(column=0, row=15, padx=200, pady=160)
    
    
    ventana1.mainloop()


def imprimir():
    datos=StringVar()
    datos=scrolledtext1.get("0.0", tk.END)
    print("/%s/"%(datos))
    if not(datos.isspace()):
        print(datos)
    else:
        print("Error")
        

ventana_p()
