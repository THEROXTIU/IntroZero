#PARTE2
#Nombre: Iago brian Lorenzana Reyes
#Carrera: Informática
#Materia: Desarrollo de aplicaciones web con python
#Ejercicio o práctica: 2.1 - votos

import random
print ("Programa para contabilizar 2,000,000 de votos y elegir un ganador entre ellos")
lista = []
for i in range (2000000):
    lista.append(i)
    print(i)
voto = random.choice(lista)
print("El voto ganador es: ", voto)

