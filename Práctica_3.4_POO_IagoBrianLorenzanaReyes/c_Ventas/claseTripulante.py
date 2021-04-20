#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: Desarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"
from claseEmpleado import *
from claseAgenteVentas import *
from claseGerente import *

class Tripulante(Empleado):
    def mostrarRenovacionLicencia(self):
        if self.edad<50:
            print("Renueva su licencia cada 1 año")
        else:
            print("Renueva su licencia cada 6 meses")
