from pyswip import Functor, Variable, Query, call

assertz = Functor("assertz", 1)
Animal = Functor("Animal", 6)

def insertar(raza,nombre,genero,edad,ecosistema,comida):
	#print(raza,nombre,genero,edad,ecosistema,comida)
	call(assertz(Animal(raza,nombre,genero,edad,ecosistema,comida)))
	
def consulta(raza,nombre,genero,edad,ecosistema,comida):
	
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
		print "Hola", a, b , c , d , e , f
	q.closeQuery()
	
insertar("perro","firulais","M","5","casa","ascan")
insertar("gato","silvestre","M","10","casa","wiskas")
insertar("gato","gsg","M","10","casa","wiskas")
insertar("elefante","dumbo","M","20","selva","mani")
insertar("gallo","claudio","M","2","granja","maiz")

#consulta("gallo","vacio","vacio","vacio","vacio","maiz")

