#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: DEsarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"
class Carrera:
    def __init__(self, nombre):
        self.nombre=nombre
        self.materias={}

    def agregarMateria(self, materia, codigo):
        self.materias[codigo]=materia


