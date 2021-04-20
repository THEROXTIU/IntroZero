#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: DEsarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"

from claseCarrera import *
from claseMateria import *

ing=Carrera("Ingeniería")
algebra=Materia("Álgebra", "Ricardo Quinteros", 2010)
fisica=Materia("Física", "Margarita Gómez", 2006)
quimica=Materia("Química", "Lorenza Ríos", 2003)
ing.agregarMateria(algebra,1234)

print(algebra.fechaInicioDictado)
print(fisica.fechaInicioDictado)
print(quimica.fechaInicioDictado)

