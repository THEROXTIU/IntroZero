#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: Desarrollo de Aplicaciones Web
#Ejercicio o práctica: 2.3 - practicando Funciones python
from random import randint


precio = 150
capacidad = 10000
monto = capacidad * precio
sumaRealDesc= 0
sumaPercibida= 0

clasificacion = {"Primera":0, "Segunda":0, "Tercera":0, "Cuarta":0, "Quinta":0}
descuentos = {
    "1":(precio*0.30),
    "2":(precio*0.10),
    "3":(precio*0.15),
    "4":(precio*0.25),
    "5":(precio*0.35)
    }
suma_descuentos = [0, 0, 0, 0, 0]
suma_entradas = {"1":0, "2":0, "3":0, "4":0, "5":0}

for i in range(10000):
    edad = randint(5,120)
    if edad > 5 and edad <14:
        clasificacion["Primera"] +=1
        suma_descuentos[0] += descuentos["1"]
        suma_entradas["1"] += precio - descuentos["1"]
    elif edad > 15 and edad <19:
        clasificacion["Segunda"] +=1
        suma_descuentos[1] += descuentos["2"]
        suma_entradas["2"] += precio - descuentos["2"]
    elif edad > 20 and edad < 45:
        clasificacion["Tercera"] +=1
        suma_descuentos[2] += descuentos["3"]
        suma_entradas["3"] += precio - descuentos["3"]
    elif edad > 46 and edad <65:
        clasificacion["Cuarta"] +=1
        suma_descuentos[3] += descuentos["4"]
        suma_entradas["4"] += precio - descuentos["4"]
    else:
        clasificacion["Quinta"] +=1
        suma_descuentos[4] += descuentos["5"]
        suma_entradas["5"] += precio - descuentos["5"]
sumaTotal=(suma_entradas["1"]+suma_entradas["2"]+suma_entradas["3"]+suma_entradas["4"]+suma_entradas["5"])
sumaTotalDesc=(suma_descuentos[0]+suma_descuentos[1]+suma_descuentos[2]+suma_descuentos[3]+suma_descuentos[4])

print("La suma total percibida es : $", sumaTotal)
print("El monto total que dejaría de cobrar por el evento : $",suma_descuentos[0]+suma_descuentos[1]+suma_descuentos[2]+suma_descuentos[3]+suma_descuentos[4])
print("El monto total que dejaría de cobrar por el evento en porcentaje sería : ", (sumaTotalDesc/monto)*100,"%")
print("Se pudo haber obtenido csi se hubiera cobrado el descuento un total de: ",sumaTotal+sumaTotalDesc)
                 
porcentaje1 = ((clasificacion["Primera"] / capacidad)*100)
porcentaje2 = ((clasificacion["Segunda"] / capacidad)*100)
porcentaje3 = ((clasificacion["Tercera"] / capacidad)*100)
porcentaje4 = ((clasificacion["Cuarta"] / capacidad)*100)
porcentaje5 = ((clasificacion["Quinta"] / capacidad)*100)

if porcentaje1 >0 and porcentaje1 <10 :
    bar1=("**")
elif porcentaje1 >10 and porcentaje1 <15 :
    bar1=("****")
elif porcentaje1 >15 and porcentaje1 <30 :
    bar1=("******")
elif porcentaje1 >30 and porcentaje1 <50 :
    bar1=("********")
elif porcentaje1 >50 and porcentaje1 <100 :
    bar1=("**********")
if porcentaje2 >0 and porcentaje2 <10 :
    bar2=("**")
elif porcentaje2 >10 and porcentaje2 <15 :
    bar2=("****")
elif porcentaje2 >15 and porcentaje2 <30 :
    bar2=("******")
elif porcentaje2 >30 and porcentaje2 <50 :
    bar2=("********")
elif porcentaje1 >50 and porcentaje2 <100 :
    bar2=("**********")
if porcentaje3 >0 and porcentaje3 <10 :
    bar3=("**")
elif porcentaje3 >10 and porcentaje3 <15 :
    bar3=("****")
elif porcentaje3 >15 and porcentaje3 <30 :
    bar3=("******")
elif porcentaje3 >30 and porcentaje <50 :
    bar3=("********")
elif porcentaje3 >50 and porcentaje3 <100 :
    bar3=("**********")
if porcentaje4 >0 and porcentaje4 <10 :
    bar4=("**")
elif porcentaje4 >10 and porcentaje4 <15 :
    bar4=("****")
elif porcentaje4 >15 and porcentaje4 <30 :
    bar4=("******")
elif porcentaje4 >30 and porcentaje4 <50 :
    bar4=("********")
elif porcentaje4 >50 and porcentaje4 <100 :
    bar4=("**********")
if porcentaje5 >0 and porcentaje1 <10 :
    bar5=("**")
elif porcentaje5 >10 and porcentaje5 <15 :
    bar5=("****")
elif porcentaje5 >15 and porcentaje5 <30 :
    bar5=("******")
elif porcentaje5 >30 and porcentaje5 <50 :
    bar5=("********")
if porcentaje5 >50 and porcentaje5 <100 :
    bar5=("**********")
    
    
    
print("Rango de edad de las personas que entraron:")
print("5-14 :", clasificacion['Primera'], porcentaje1, "%", "=",bar1)
print("15-19 :", clasificacion['Segunda'], porcentaje2, "%", "=",bar2)
print("20-45 :", clasificacion['Tercera'], porcentaje3, "%", "=",bar3)
print("46-65 :", clasificacion['Cuarta'], porcentaje4, "%", "=",bar4)
print("66-> :", clasificacion['Quinta'], porcentaje5, "%", "=",bar5)
