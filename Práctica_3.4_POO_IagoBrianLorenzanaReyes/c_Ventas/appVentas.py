#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: DEsarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"
from claseEmpleado import *
from claseAgenteVentas import *
from claseTripulante import *
from claseGerente import *


jorge = Empleado("Jorge", 35, "B110", 2000)
print(jorge.nombre)
print(jorge.calcularSueldo(1000,500))

carlos = Tripulante("Carlos", 25, "A110", 1000)
print(carlos.mostrarRenovacionLicencia())

helena = Gerente("Helena", 45, "Z210", 200000)
print(helena.calcularSueldo(100,6000))

