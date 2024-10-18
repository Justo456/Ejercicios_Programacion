from GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_menu_de_opciones import *
from GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_matrices import *
opcion_2 = False
opcion_4 = False
opcion_7 = False
opcion = menu_de_opciones_1()
seguir = "s"
seguir = input("¿Desea continuar? s/n: ").lower()
while seguir != "s" and seguir!= "n":
    seguir = input("¿Error.Desea continuar? s/n: ").lower()

while seguir == "s":
    opcion = int(input("2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\n9-Listar los datos de los usuarios de México ordenados por nombre\nIngrese una opción: "))
    while opcion > 11 or opcion < 2:    
        opcion = int(input("ERROR.\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\n9-Listar los datos de los usuarios de México ordenados por nombre\nIngrese una opción: "))
    if opcion == 2:
        opcion_2= True  
        lista_noms_Mex = menu_de_opciones_2(opcion)
    if opcion == 4:
        opcion_4 = True  
        lista_jovenes = menu_de_opciones_4(opcion)
    if opcion == 7:
        opcion_7 = True  
        lista_mx_br_codpos_mas_8000 = menu_de_opciones_7(opcion)
    
    menu_de_opciones_3(opcion)
    menu_de_opciones_5(opcion)
    menu_de_opciones_6(opcion)
    menu_de_opciones_8(opcion) 

    if opcion_2 == True and opcion == 9:
        menu_de_opciones_9(lista_noms_Mex,opcion)
    elif opcion_2 == False and opcion == 9:
        print("Error.Primero debe listar los datos de los usuarios de mexico")
    
    if opcion_4 == True and opcion == 10:
        menu_de_opciones_10(lista_jovenes,opcion)
    elif opcion_4 == False and opcion == 10:
        print("Error.Primero debe listar los datos de los usuarios mas jovenes")

    if opcion_7 == True and opcion == 11:
        menu_de_opciones_11(lista_mx_br_codpos_mas_8000,opcion)
    elif opcion_7 == False and opcion == 11:
        print("Error.Primero debe listar los datos de los usuarios de mexico")
       
    
    seguir = input("¿Desea continuar? s/n: ").lower()
    while seguir != "s" and seguir != "n":
        seguir = input("¿Error.Desea continuar? s/n: ").lower()