#!/usr/local/bin/python
# -*- coding: latin-1 -*-
                 # Permite abrir archivos dentro de la carpeta del programa
from backEnd import insertar
from backEnd import consulta
from Tkinter import *     # Importación del módulo tkinter

ventana = Tk()            # Creación de la ventana principal
ventana.minsize(500,300)  #Asigna un tamaño minimo al frame
ventana.maxsize(700,500)  #Asigna un tamañan máximo al frame
ventana.title("Zoológico El Animalito Feliz")      # Nombre de la ventana

fondo = Frame(ventana)
fondo.pack()

def Ingreso():
	raza=eraza.get()
	nombre=enombre.get()
	genero=egenero.get()
	edad=eedad.get()
	ecosistema=eecosistema.get()
	comida=ecomida.get()
	insertar(raza,nombre,genero,edad,ecosistema,comida)

def Consulta():
	raza=eraza.get()
	nombre=enombre.get()
	genero=egenero.get()
	edad=eedad.get()
	ecosistema=eecosistema.get()
	comida=ecomida.get()
	if eraza.get()=="":
		raza="vacio"
	if enombre.get()=="":
		nombre="vacio"
	if egenero.get()=="":
		genero="vacio"
	if eedad.get()=="":
		edad="vacio"
	if eecosistema.get()=="":
		ecosistema="vacio"
	if ecomida.get()=="":
		comida="vacio"
		
	#print(raza,nombre,genero,edad,ecosistema,comida)
	consulta(raza,nombre,genero,edad,ecosistema,comida)

barra = Frame(ventana)
plano_1 = Button(barra, text = "Agregar Animales", font = ("Helvetica", 10), command=Ingreso)
plano_1.pack(side=LEFT, padx = 2, pady = 2)

plano_2 = Button(barra, text = "Hacer Consultas", font = ("Helvetica", 10), command=Consulta)
plano_2.pack(side = LEFT, padx = 2, pady = 2)

barra.pack(side=TOP, fill=X)
#----------------------------------------------------------------------------------------------------------
photo = PhotoImage(file = "selva.GIF")      # Se ubica el frame en la ventana
plano = Label(ventana, image = photo)
plano.photo = photo
plano.pack()


def Salida():#FUNCION DE SALIDA DEL PROGRAMA    
    ventana.destroy()
    

	
	
#-----------------------------------------------------------------------------------------------------------
#En este bloque se encuentran los labels de la página principal

label_1 = Label(plano,text="Ingrese los datos del animal: ", font = ("Helvetica", 16), fg = "black")
label_1.place(x = 10, y = 2)

label_2 = Label (plano,text="Nombre: ", font = ("Helvetica", 12), fg = "black")
label_2.place(x = 10, y = 40)

label_3 = Label (plano,text="Raza: ", font = ("Helvetica", 12), fg = "black")
label_3.place(x = 10, y = 70)

label_4 = Label (plano,text="Género: ", font = ("Helvetica", 12), fg = "black")
label_4.place(x = 10, y = 100)

label_5 = Label (plano,text="Edad: ", font = ("Helvetica", 12), fg = "black")
label_5.place(x = 10, y = 130)

label_6 = Label (plano,text="Ecosistema: ", font = ("Helvetica", 12), fg = "black")
label_6.place(x = 10, y = 160)

label_7 = Label (plano,text="Comida Favorita: ", font = ("Helvetica", 12), fg = "black")
label_7.place(x = 10, y = 190)

#---------------------------------------------------------------------------------------------------------
nombre = StringVar()
enombre = Entry(plano, textvariable = nombre)
enombre.place(x = 145, y = 40)

raza = StringVar()
eraza = Entry(plano, textvariable = raza)
eraza.place(x = 145, y = 70)

genero = StringVar()
egenero = Entry(plano, textvariable = genero)
egenero.place(x = 145, y = 100)

edad = StringVar()
eedad = Entry(plano, textvariable = edad)
eedad.place(x = 145, y = 130)

ecosistema = StringVar()
eecosistema = Entry(plano, textvariable = ecosistema)
eecosistema.place(x = 145, y = 160)

comida = StringVar()
ecomida = Entry(plano, textvariable = comida)
ecomida.place(x = 145, y = 190)

#----------------------------------------------------------------------------------------------------------
boton_1 = Button(plano, text = "Salir", command = Salida, bd = 10)
boton_1.place(x= 250, y = 350)

ventana.mainloop()
