#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: DEsarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"
from claseEmpleado import *
from claseAgenteVentas import *


class Gerente(Empleado):
    def calcularSueldo(self, descuentos, bonificaciones):
        return self.sueldoBase-descuentos+bonificaciones
