#!/usr/local/bin/python
# -*- coding: latin-1 -*-
                 # Permite abrir archivos dentro de la carpeta del programa
from backEnd import insertar
from backEnd import consulta
import Tkinter
from Tkinter import *  
import ttk

ventana =Tk()
ventana.title("Zoo")

notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='Inserccion')
notebook.add(frame2, text='Consultas')

def Ingreso():
	raza=eraza.get()
	nombre=enombre.get()
	genero=egenero.get()
	edad=eedad.get()
	ecosistema=eecosistema.get()
	comida=ecomida.get()
	insertar(raza,nombre,genero,edad,ecosistema,comida)

def Consulta():
	raza=craza.get()
	nombre=cnombre.get()
	genero=cgenero.get()
	edad=cedad.get()
	ecosistema=cecosistema.get()
	comida=ccomida.get()
	if craza.get()=="":
		raza="vacio"
	if cnombre.get()=="":
		nombre="vacio"
	if cgenero.get()=="":
		genero="vacio"
	if cedad.get()=="":
		edad="vacio"
	if cecosistema.get()=="":
		ecosistema="vacio"
	if ccomida.get()=="":
		comida="vacio"
		
	#print(raza,nombre,genero,edad,ecosistema,comida)
	consulta(raza,nombre,genero,edad,ecosistema,comida)
	
def Salida():#FUNCION DE SALIDA DEL PROGRAMA    
    ventana.destroy()

#botones
plano_1 = Button(frame1, text = "Agregar Animales", font = ("Helvetica", 10), command=Ingreso)
plano_1.place(x = 10, y = 220)

plano_2 = Button(frame2, text = "Hacer Consultas", font = ("Helvetica", 10), command=Consulta)
plano_2.place(x = 10, y = 220)

boton_1 = Button(frame1, text = "Salir",font = ("Helvetica", 10), command = Salida)
boton_1.place(x = 150, y = 220)

boton_1 = Button(frame2, text = "Salir",font = ("Helvetica", 10), command = Salida)
boton_1.place(x = 150, y = 220)

#-----------------------------------------------------------------------------------------------------------
#En este bloque se encuentran los labels de la parte de Ingreso

label_1 = Label(frame1,text="Ingrese los datos del animal: ", font = ("Helvetica", 16), fg = "black")
label_1.place(x = 10, y = 2)

label_2 = Label (frame1,text="Nombre: ", font = ("Helvetica", 12), fg = "black")
label_2.place(x = 10, y = 40)

label_3 = Label (frame1,text="Raza: ", font = ("Helvetica", 12), fg = "black")
label_3.place(x = 10, y = 70)

label_4 = Label (frame1,text="Género: ", font = ("Helvetica", 12), fg = "black")
label_4.place(x = 10, y = 100)

label_5 = Label (frame1,text="Edad: ", font = ("Helvetica", 12), fg = "black")
label_5.place(x = 10, y = 130)

label_6 = Label (frame1,text="Ecosistema: ", font = ("Helvetica", 12), fg = "black")
label_6.place(x = 10, y = 160)

label_7 = Label (frame1,text="Comida Favorita: ", font = ("Helvetica", 12), fg = "black")
label_7.place(x = 10, y = 190)

#---------------------------------------------------------------------------------------------------------
nombre = StringVar()
enombre = Entry(frame1, textvariable = nombre)
enombre.place(x = 145, y = 40)

raza = StringVar()
eraza = Entry(frame1, textvariable = raza)
eraza.place(x = 145, y = 70)

genero = StringVar()
egenero = Entry(frame1, textvariable = genero)
egenero.place(x = 145, y = 100)

edad = StringVar()
eedad = Entry(frame1, textvariable = edad)
eedad.place(x = 145, y = 130)

ecosistema = StringVar()
eecosistema = Entry(frame1, textvariable = ecosistema)
eecosistema.place(x = 145, y = 160)

comida = StringVar()
ecomida = Entry(frame1, textvariable = comida)
ecomida.place(x = 145, y = 190)

#-----------------------------------------------------------------------------------------------------------
#En este bloque se encuentran los labels de la parte de Consulta

label_8 = Label(frame2,text="Ingrese los datos del animal: ", font = ("Helvetica", 16), fg = "black")
label_8.place(x = 10, y = 2)

label_9 = Label (frame2,text="Nombre: ", font = ("Helvetica", 12), fg = "black")
label_9.place(x = 10, y = 40)

label_10 = Label (frame2,text="Raza: ", font = ("Helvetica", 12), fg = "black")
label_10.place(x = 10, y = 70)

label_11 = Label (frame2,text="Género: ", font = ("Helvetica", 12), fg = "black")
label_11.place(x = 10, y = 100)

label_12 = Label (frame2,text="Edad: ", font = ("Helvetica", 12), fg = "black")
label_12.place(x = 10, y = 130)

label_13 = Label (frame2,text="Ecosistema: ", font = ("Helvetica", 12), fg = "black")
label_13.place(x = 10, y = 160)

label_14 = Label (frame2,text="Comida Favorita: ", font = ("Helvetica", 12), fg = "black")
label_14.place(x = 10, y = 190)

#---------------------------------------------------------------------------------------------------------
nombre = StringVar()
cnombre = Entry(frame2, textvariable = nombre)
cnombre.place(x = 145, y = 40)

raza = StringVar()
craza = Entry(frame2, textvariable = raza)
craza.place(x = 145, y = 70)

genero = StringVar()
cgenero = Entry(frame2, textvariable = genero)
cgenero.place(x = 145, y = 100)

edad = StringVar()
cedad = Entry(frame2, textvariable = edad)
cedad.place(x = 145, y = 130)

ecosistema = StringVar()
cecosistema = Entry(frame2, textvariable = ecosistema)
cecosistema.place(x = 145, y = 160)

comida = StringVar()
ccomida = Entry(frame2, textvariable = comida)
ccomida.place(x = 145, y = 190)

#barra.pack(side=TOP, fill=X)

ventana.geometry('350x300')
ventana.mainloop()
