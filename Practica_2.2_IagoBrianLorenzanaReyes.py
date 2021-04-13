#Nombre: Iago Brian Lorenzana Reyes
#Carrera: Informática
#Materia: Desarrollo de Aplicaciones Web
#Ejercicio o práctica: 2.2 - practicando condicionales complejas python
fecha=input("Fecha (formato'dia, DD/MM') :") #Declaramos variables con sus diferentes propiedades y formatos como en el caso de diasemana, dianro, mesnro
fecha=fecha.lower()
diasemana=fecha[0:fecha.find(',')]
dianro=int(fecha[fecha.find(' ')+1:fecha.find('/')])
mesnro=int(fecha[fecha.find('/')+1:])
if dianro>31 or mesnro>12:
    print("Fecha incorrecta")

else:
    if diasemana in "lunes,martes,miércoles":#Empiezan las condiciones y apartir de cada respuesta obtendremos un diferente resultado de promedio
        respuesta=input("¿Se tomaron exámenes? S/N: ")#En caso de que sea una entrada de texto que no esté en la condición sólo mostrará un error
        if respuesta.lower()=="s":
            aprobados=int(input("Cantidad de aprobados: "))
            reprobados=int(input("Cantidad de reprobados: "))
            print("Porcentaje de aprobados: ", (aprobados*100)/(aprobados+reprobados) ,"%")

    elif diasemana == "jueves":
        asistencia=int(input("Porcentaje de asistencia: "))#En caso de que sea jueves o viernes se verificará la asistencia si es mayor a 50 mandará un mensaje de asistirá la mayoría
        if asistencia>50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")

    elif diasemana == "viernes": #En este elif si la condición es viernes y si el día es el primero o el mes primero o septimo dará el mensaje de Comienzo de nuevo ciclo
        if dianro==1 and (mesnro==1 or mesnro==7):
            print("Comienzo de nuevo ciclo")
            alumnos=int(input("Cantidad de alumnos: "))#Asignamos la cantidad de alumnso cómo el arancel por alumno y así calcularemos el ingreso total multiplicando la cantidad de alumnos por el arancel y se mostrará al final el ingreso total
            arancel=float(input("Arancel: $"))
            print("Ingreso total: $", alumnos*arancel)
    
    else:
        print("Fecha incorrecta")

print("Fin del programa")