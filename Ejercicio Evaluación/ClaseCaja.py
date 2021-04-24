#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: DEsarrollo de Aplicaciones Web
#Ejercicio o Práctica "Ejercicio de Evaluación"

#Se crea la clase caja
class Caja:
#se crea el metodo constructor
    def __init__(self, ancho, largo, alto):
        self.ancho=ancho
        self.largo=largo
        self.alto=alto
#se crea el método mostrar para mostrar los valores de la clase caja    
    def mostrar(self):
        return"Alto: ",self.alto," Ancho: ", self.ancho," Largo: ", self.largo
#se crea el metodo para calcular el volumen  
    def calcularVolumen(self):
        Vol = (self.alto * self.ancho * self.largo)
        return("El volumen es: ",Vol)
#se crea el metodo para calcular el area lateral   
    def areaLateral(self):
        return self.largo * self.alto
#se crea el metodo para calcular el area frontal       
    def areaFrontal(self):
        return self.alto * self.ancho
#se crea el metodo para calcular el areasuperior      
    def areaSuperior(self):
        return self.largo * self.ancho
#se crea el metodo para calcular el area total    
    def calcularAreaTotal(self):
        Total = (2 * self.areaFrontal() + 2 * self.areaSuperior() + 2 * self.areaLateral())
        return Total
#se crea el metodo para crear un clon de nuestra clase
    def clon(self):
        cl= Caja(self.ancho, self.largo, self.alto)
        return cl
#se crea un método con valores con un 25% más grande
    def crearCajaGrande(self):
        nuevoAlto = self.alto * 1.25
        nuevoAncho = self.ancho * 1.25
        nuevoLargo  = self.largo * 1.25

        cajaNueva = Caja(nuevoAncho, nuevoLargo, nuevoAlto)
        return cajaNueva
#se crea un metodo para comparar el clon con la caja más grande, se comparan los valores para saber si cabe la caja clon con la caja más grande  
    def cabe1DentroDe2(self, cl,cajaNueva):
        if cl.ancho < cajaNueva.ancho and cl.alto < cajaNueva.alto and cl.largo < cajaNueva.largo:
            return "Si lo es"
        else:
            return "No lo es"
