'''Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de compras on-line recientemente lanzado al mercado para 
ello necesita un programa que le permita acceder a los datos relevados.
Realizar una función con el siguiente Menú de Opciones:
1-Importar listas
2-Listar los datos de los usuarios de México
3-Listar los nombre, mail y teléfono de los usuarios de Brasil
4-Listar los datos del/los usuario/s más joven/es
5-Obtener un promedio de edad de los usuarios
6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.'''

def menu_de_opciones():
    
    opcion = int(input("1-Importar listas\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\nIngrese una opción: "))
    
    while opcion != 1:
        print("------------------------------------------")
        print("|*ERROR.Primero debe importar las listas*|")
        print("------------------------------------------")
        opcion = int(input("1-Importar listas\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\nIngrese una opción: "))
    if opcion == 1:
        from listas_personas import mis_listas
        print("")
        print("*Las listas han sido importadas*")
        print("")
    
    seguir = input("¿Desea continuar? s/n: ").lower()
    while seguir != "s" and seguir!= "n":
        seguir = input("¿Error.Desea continuar? s/n: ").lower()
    
    while seguir == "s":
        
        opcion = int(input("2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\nIngrese una opción: "))
        while opcion > 8 or opcion < 2:    
            opcion = int(input("ERROR.\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\nIngrese una opción: "))
        if opcion == 2:
            print("----------------DATOS DE LOS USUARIOS DE MÉXICO--------------------")
            for i in range(len(mis_listas)):
                for j in range(len(mis_listas[i])):
                    if mis_listas[i][j] == "Mexico":
                                                                           
                        for k in range(len(mis_listas)):
                            print(mis_listas[k][j])
                        print("-------------------------------------------------------------------")    
            

        elif opcion == 3:
            print("---------------------NOMBRE,TELEFONO,MAIL,USUARIOS DE BRASIL---------------------")
            for i in range(len(mis_listas)):
                for j in range(len(mis_listas[i])):
                    if mis_listas[i][j] == "Brazil":
                        for k in range(len(mis_listas)):               
                            if mis_listas[k] == mis_listas[0] or mis_listas[k] == mis_listas[1] or mis_listas[k] == mis_listas[2]:
                                print(mis_listas[k][j])  
                        print("--------------------------------------------------------------------------------")
                                    

        elif opcion == 4:
            
            edad_menor = 0   
            mensaje = ""
            mensaje_total = ""
            edad_promedio = 0
            suma_edades = 0
            for i in range(len(mis_listas[7])):
                suma_edades += mis_listas[7][i]
                if i == len(mis_listas[7]) - 1:       
                    edad_promedio = suma_edades/len(mis_listas[7])
                    
            
            for i in range(len(mis_listas[7])):
                
                if mis_listas[7][i] <= edad_promedio:
                    edad_menor = mis_listas[7][i]
                    nombre_menor = mis_listas[0][i]
                    mensaje = f"{nombre_menor} y su edad es {edad_menor}, "
                    mensaje_total += mensaje
            print("----------------------USUARIOS MAS JOVENES----------------------")
            print(mensaje_total)
            print("----------------------------------------------------------------")

        elif opcion == 5:
            edad_promedio = 0
            suma_edades = 0
            for i in range(len(mis_listas[7])):
                suma_edades += mis_listas[7][i]
                if i == len(mis_listas[7]) - 1:       
                    edad_promedio = suma_edades/len(mis_listas[7])
            print(f"El promedio de edades es de {edad_promedio:.0f} años")
        
        elif opcion == 6:
            edad_mayor = 0
            print("------------------------DATOS DEL USUARIO DE BRAZIL CON MAYOR EDAD------------------------")
            for i in range(len(mis_listas)):
                for j in range(len(mis_listas[i])):
                    if mis_listas[i][j] == "Brazil":
                        if mis_listas[7][j] > edad_mayor:
                            edad_mayor = mis_listas[7][j]
                            pos_edad_mayor = j
                            

            for k in range(len(mis_listas)):
                print(mis_listas[k][pos_edad_mayor])
            print("------------------------------------------------------------------------------------------")    

        elif opcion == 7:
                print("------------------------DATOS DEL USUARIOS MÉXICO Y BRAZIL CON CODIGO POSTAL MAYOR A 8000------------------------")
                for i in range(len(mis_listas)):                                            
                        for j in range(len(mis_listas[i])):
                            
                            if mis_listas[i][j] == "Mexico" or mis_listas[i][j] == "Brazil": 
                                if mis_listas[4][j] > 8000:                                                                               
                                    for k in range(len(mis_listas)):
                                        print(mis_listas[k][j])
                                    print("-----------------------------------------------------------")

        elif opcion == 8:
            print("---------------------NOMBRE,TELEFONO,MAIL,USUARIOS DE ITALIA MAYORES DE 40 AÑOS---------------------")
            for i in range(len(mis_listas)):
                for j in range(len(mis_listas[i])):
                    if mis_listas[i][j] == "Italy" and mis_listas[7][j] > 40:
                        for k in range(len(mis_listas)):           
                                if mis_listas[k] == mis_listas[0] or mis_listas[k] == mis_listas[1] or mis_listas[k] == mis_listas[2]:
                                    print(mis_listas[k][j])  
                        print("--------------------------------------------------------------------------------")                                    
                
        seguir = input("¿Desea continuar? s/n: ").lower()
        while seguir != "s" and seguir!= "n":
            seguir = input("¿Error.Desea continuar? s/n: ").lower()

        

menu_de_opciones()