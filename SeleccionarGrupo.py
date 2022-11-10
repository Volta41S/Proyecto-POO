from tkinter import*
from tkinter import ttk

raiz=Tk()

AgreGrupo=Frame(raiz)
AgreGrupo.pack()
AgreGrupo.config(width=550,height=350,padx=10,pady=20)

Tit1=Label(AgreGrupo,text="Nombre de grupo",font=("Arial",20))
Tit1.grid(column=0,row=0,columnspan=5,padx=(40,0),pady=10)
CodGru_label=Label(AgreGrupo,text="Calificaciones",font=("Arial",15))
CodGru_label.grid(column=0,row=1,columnspan=5,padx=(40,0),pady=(10,20))

PriTri_boton=ttk.Button(AgreGrupo,text="1er trimestre")
PriTri_boton.grid(column=1,row=2,padx=10,pady=10)

SegTri_boton=ttk.Button(AgreGrupo,text="2do trimestre")
SegTri_boton.grid(column=2,row=2,padx=10,pady=10)

TerTri_boton=ttk.Button(AgreGrupo,text="3er trimestre")
TerTri_boton.grid(column=3,row=2,padx=10,pady=10)

Prom_boton=ttk.Button(AgreGrupo,text="Promedio del ciclo escolar")
Prom_boton.grid(column=0,row=3,columnspan=5, padx=(50,10),pady=10)

Reg_boton=ttk.Button(AgreGrupo,text="Regresar")
Reg_boton.grid(column=0,row=4,padx=20,pady=10)

espacioder_label = Label(AgreGrupo,width=5)
espacioder_label.grid(column=5,row=0,rowspan=10,padx=2,)

espacioizq_label = Label(AgreGrupo,width=5)
espacioizq_label.grid(column=0,row=0,rowspan=10,padx=2)

raiz=mainloop()