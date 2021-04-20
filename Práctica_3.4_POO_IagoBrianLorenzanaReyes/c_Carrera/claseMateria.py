#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: DEsarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"
from claseCarrera import *

class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre=nombre
        self.profesor=profesor
        self.fechaInicioDictado=fecha

    @property
    def fechaInicioDictado(self):
        return self._fechaInicioDictado

    @fechaInicioDictado.setter
    def fechaInicioDictado(self, fecha):
        if fecha<2006:
            self._fechaInicioDictado=2006
        else:
            self._fechaInicioDictado=fecha






 
