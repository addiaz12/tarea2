#!/usr/local/bin/python
# -*- coding: latin-1 -*-

#funciones del archivo backEnd
from backEnd import insertar
from backEnd import consulta

#librerias Importadas
import Tkinter
from Tkinter import *  
import ttk
import tkMessageBox

#se define la ventana principal
ventana =Tk()
ventana.title("Zoo")

#pestañas de la ventana principal
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='Inserccion')
notebook.add(frame2, text='Consultas')

#funcion de ingreso enviar e insertar datos en el backend
def Ingreso():
	raza=eraza.get()
	nombre=enombre.get()
	genero=egenero.get()
	edad=eedad.get()
	ecosistema=eecosistema.get()
	comida=ecomida.get()
	if (eraza.get()=="" or enombre.get()=="" or eedad.get()=="" or eecosistema.get()=="" or egenero.get()=="" or ecomida.get()==""):
		Error()
	else:
		insertar(raza,nombre,genero,edad,ecosistema,comida)
		Aviso()

#funcion de consulta para enviar y recibir una respuesta del backend
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
	#llama a la funcion consulta del backend	
	lista=consulta(raza,nombre,genero,edad,ecosistema,comida)
	Ventana(lista)

#funcion de salida del programa
def Salida():
    ventana.destroy()
 
 #mensaje de error al intentar insertar datos vacios
def Error():
	tkMessageBox.showinfo(title="Error", \
    message="Tiene que llenar todos los atributos del animal")

#funcion de aviso al insertar los datos
def Aviso():
	tkMessageBox.showinfo(title="Aviso", \
    message="Insercción Exitosa")
    
#ventana emergente con los resultados de las consultas
def Ventana(lista):
	ventana2 = Tk()
	ventana2.title("Consulta:")
	plano_3 = Label(ventana2)
	plano_3.pack()
	
	label_15 = Label(plano_3,text="Resultado: ", font = ("Helvetica", 16), fg = "black")
	label_15.place(x = 10, y = 2)
	label_15.pack()
	
	for i in range(len(lista)):
			label_15 = Label(plano_3,text= ("--Raza:",lista[i][0],"--Nombre:",lista[i][1],"--Genero:",lista[i][2]
			,"--Edad:",lista[i][3],"--Ecosistema:",lista[i][4],"--Comida:",lista[i][5]), font = ("Helvetica", 14), fg = "black")
			label_15.place(x = 0, y = 50)
			label_15.pack()
	
	ventana2.geometry('800x300')
	ventana2.mainloop()

#botones
plano_1 = Button(frame1, text = "Agregar Animales", font = ("Helvetica", 10), command=Ingreso)
plano_1.place(x = 10, y = 220)

plano_2 = Button(frame2, text = "Hacer Consultas", font = ("Helvetica", 10), command=Consulta)
plano_2.place(x = 10, y = 220)

boton_1 = Button(frame1, text = "Salir",font = ("Helvetica", 10), command = Salida)
boton_1.place(x = 150, y = 220)

boton_1 = Button(frame2, text = "Salir",font = ("Helvetica", 10), command = Salida)
boton_1.place(x = 150, y = 220)

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

ventana.geometry('350x300')
ventana.mainloop()
