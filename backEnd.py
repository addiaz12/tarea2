from pyswip import Functor, Variable, Query, call

#Para definir las afirmaciones y su aridad
assertz = Functor("assertz", 1)
Animal = Functor("Animal", 6)

#Funcion para insertar los datos en la base de conocimiento
def insertar(raza,nombre,genero,edad,ecosistema,comida):
	call(assertz(Animal(raza,nombre,genero,edad,ecosistema,comida)))
	print "inserto",raza,nombre,genero,edad,ecosistema,comida
	
	
#esta funcion retorna una lista con los valores que se optuvieron de la consulta
def consulta(raza,nombre,genero,edad,ecosistema,comida):
	#Se definen las variables
	A = Variable()
	B = Variable()
	C = Variable()
	D = Variable()
	E = Variable()
	F = Variable()
	a=A;
	b=B;
	c=C;
	d=D;
	e=E;
	f=F;
	
	#Condiciones para encontar las variables unificadoras
	if raza != "vacio":
		a=raza;
	if nombre != "vacio":
		b=nombre;
	if genero != "vacio":
		c=genero;
	if edad != "vacio":
		d=edad;
	if ecosistema != "vacio":
		e=ecosistema;
	if comida != "vacio":
		f=comida;
	#esta lista almacena todas las consultas	
	lista=[]
	#apertura del query para iniciar consulta en prolog
	q=Query(Animal(a,b,c,d,e,f))
	while q.nextSolution():
		if raza == "vacio":
			a=A.value;
		if nombre == "vacio":
			b=B.value;
		if genero == "vacio":
			c=C.value;
		if edad == "vacio":
			d=D.value;
		if ecosistema == "vacio":
			e=E.value;
		if comida == "vacio":
			f=F.value;
		lista2=[a,b,c,d,e,f]
		print "consulto",a,b,c,d,e,f
		lista.insert(len(lista),lista2)
	#cierre del query
	q.closeQuery()
	return lista


