from tkinter import*
from tkinter import ttk

raiz=Tk()

AgreGrupo=Frame(raiz)
AgreGrupo.pack()
AgreGrupo.config(width=550,height=350,padx=10,pady=20)

Tit1=Label(AgreGrupo,text="Eliminar Grupo",font=("Arial",20))
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

Can_boton=ttk.Button(AgreGrupo,text="Cancelar")
Can_boton.grid(column=1,row=3,padx=10)

Ace_boton=ttk.Button(AgreGrupo,text="Aceptar")
Ace_boton.grid(column=2,row=3,padx=10,columnspan=2)

espacioder_label = Label(AgreGrupo,width=5)
espacioder_label.grid(column=5,row=0,rowspan=10,padx=2,columnspan=2)

espacioizq_label = Label(AgreGrupo,width=5)
espacioizq_label.grid(column=0,row=0,rowspan=10,padx=2)

raiz=mainloop()