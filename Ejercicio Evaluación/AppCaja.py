
#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: DEsarrollo de Aplicaciones Web
#Ejercicio o Práctica "Ejercicio de Evaluación"

#Importamos de nuestra clase que está en la misma ubicación que nuestra app

from ClaseCaja import *
#construimos el objeto de la claseCaja
cajas = Caja(20,20,30)
#Usamos el método mostrar
print (cajas.mostrar())
#Ahora muestro el volumen
print (cajas.calcularVolumen())
#Muestro ahora el area total
print("Area total: ",cajas.calcularAreaTotal())
#Ahora se crea el clon
miClon= cajas.clon()
#Mostramos información del clon
print("Las cantidades de nuestro clon exactas de la primera caja: ", miClon.mostrar())
#creamos una caja mas grande a partir del clon con ayuda de "cajas"
cajas25MasGrande = cajas.crearCajaGrande()
print(cajas25MasGrande.mostrar())
#Verificamos si la primer caja cabe en la segunda
verificacion = miClon.cabe1DentroDe2(miClon,cajas25MasGrande)
print("La caja es más grande: ", verificacion)
