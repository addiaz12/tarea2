from pyswip import Functor, Variable, Query, call

def animal(raza,nombre,genero,edad,ecosistema,comida):
	assertz = Functor("assertz", 1)
	raz = Functor(raza, 5)

	call(assertz(raz(nombre,genero,edad,ecosistema,comida)))

	A = Variable()
	B = Variable()
	C = Variable()
	D = Variable()
	
	q = Query(raz(nombre,A,B,C,D))
	while q.nextSolution():
		print "Hola", nombre,A.value, B.value, C.value, D.value
	q.closeQuery()
animal("perro","firulais","M","5","bosque","ascan")
