#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: Desarrollo de Aplicaciones Web
#Ejercicio o Práctica "practica_3.4_practicando Clases y Objetos"
class Gato:
    especie="mamífero"

    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=[]

    def verEtapaDeVida(self):
        if self.edad>1:
            print(self.nombre, "es adulto")
        else:
            print(self.nombre, "es cachorro")

    def esAlimentoFavorito(self,alimento):
        return alimento in self.alimentos
         
