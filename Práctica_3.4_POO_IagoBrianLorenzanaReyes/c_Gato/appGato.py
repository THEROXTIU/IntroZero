#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: Desarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"
from claseGato import *

a = Gato("Carlos V", 3)
b = Gato("Peluquín", 1)

a.alimentos=["leche", "galletas", "pescado"]
b.alimentos=["leche", "croquetas", "pescado"]


print("El nombre del primer gato: ", a.nombre)
print("El nombre del segundo gato: ", b.nombre)
print("Edad del primer gato: ", a.edad)
a.verEtapaDeVida()
print("Edad del segundo gato: ", b.edad)
b.verEtapaDeVida()

print(a.esAlimentoFavorito("leche"))
print(b.esAlimentoFavorito("galletas"))

