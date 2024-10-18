import GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_matrices as func
from listas_personas import mis_listas
def menu_de_opciones_1():
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

def pregunta_si_desea_seguir():
    seguir = input("¿Desea continuar? s/n: ").lower()
    while seguir != "s" and seguir!= "n":
        seguir = input("¿Error.Desea continuar? s/n: ").lower()

def menu_de_opciones_2(opcion:int)->list:
    
    if opcion == 2:
            lista = []
            print("----------------DATOS DE LOS USUARIOS DE MÉXICO--------------------")
            for i in range(len(mis_listas)):
                for j in range(len(mis_listas[i])):
                    if mis_listas[i][j] == "Mexico":

                        lista.append(mis_listas[0][j])  
                        
                        for k in range(len(mis_listas)):                           
                            print(mis_listas[k][j])
                        print("-------------------------------------------------------------------")
    
            return lista   

def menu_de_opciones_3(opcion:int):
        if opcion == 3:
            print("---------------------NOMBRE,TELEFONO,MAIL,USUARIOS DE BRASIL---------------------")
            for i in range(len(mis_listas)):
                for j in range(len(mis_listas[i])):
                    if mis_listas[i][j] == "Brazil":
                        for k in range(len(mis_listas)):               
                            if mis_listas[k] == mis_listas[0] or mis_listas[k] == mis_listas[1] or mis_listas[k] == mis_listas[2]:
                                print(mis_listas[k][j])  
                        print("--------------------------------------------------------------------------------")


def menu_de_opciones_4(opcion:int):
    if opcion == 4:
            lista_jovenes_1 = []
            lista_jovenes_2 = []
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
                    lista_jovenes_1.append(edad_menor)
                    lista_jovenes_2.append(nombre_menor)
                    mensaje_total += mensaje
            print("----------------------USUARIOS MAS JOVENES----------------------")
            print(mensaje_total)
            print("----------------------------------------------------------------")
            lista_total_joven = [lista_jovenes_1,lista_jovenes_2]
            return lista_total_joven

def menu_de_opciones_5(opcion:int):
     if opcion == 5:
            edad_promedio = 0
            suma_edades = 0
            for i in range(len(mis_listas[7])):
                suma_edades += mis_listas[7][i]
                if i == len(mis_listas[7]) - 1:       
                    edad_promedio = suma_edades/len(mis_listas[7])
            print(f"El promedio de edades es de {edad_promedio:.0f} años")            

def menu_de_opciones_6(opcion:int):
     if opcion == 6:
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

def menu_de_opciones_7(opcion:int):
     if opcion == 7:
                lista_br_mx_8000_1 = []
                lista_br_mx_8000_2 = []
                print("------------------------DATOS DEL USUARIOS MÉXICO Y BRAZIL CON CODIGO POSTAL MAYOR A 8000------------------------")
                for i in range(len(mis_listas)):                                            
                        for j in range(len(mis_listas[i])):
                            
                            if mis_listas[i][j] == "Mexico" or mis_listas[i][j] == "Brazil":
                                if mis_listas[4][j] > 8000:
                                    
                                    for k in range(len(mis_listas)):
                                        edad = mis_listas[7][i]
                                        nombre = mis_listas[0][i]
                                        lista_br_mx_8000_1.append(edad)
                                        lista_br_mx_8000_2.append(nombre)
                                        print(mis_listas[k][j])
                                    print("-----------------------------------------------------------")
                lista_br_mx_8000 = [lista_br_mx_8000_1,lista_br_mx_8000_2]
                return lista_br_mx_8000

def menu_de_opciones_8(opcion:int):
     if opcion == 8:
            print("---------------------NOMBRE,TELEFONO,MAIL,USUARIOS DE ITALIA MAYORES DE 40 AÑOS---------------------")
            for i in range(len(mis_listas)):
                for j in range(len(mis_listas[i])):
                    if mis_listas[i][j] == "Italy" and mis_listas[7][j] > 40:
                        for k in range(len(mis_listas)):           
                                if mis_listas[k] == mis_listas[0] or mis_listas[k] == mis_listas[1] or mis_listas[k] == mis_listas[2]:
                                    print(mis_listas[k][j])  
                        print("--------------------------------------------------------------------------------")  

def menu_de_opciones_9(lista_nombres_mex:list,opcion:int):
    
    if opcion == 9 :
            
            for i in range(len(lista_nombres_mex) - 1):
                
                for j in range(i+1,len(lista_nombres_mex)):
                    
                    if lista_nombres_mex[i] > lista_nombres_mex[j]:
                        aux_nom_mex = lista_nombres_mex[i]
                        lista_nombres_mex[i] = lista_nombres_mex[j]
                        lista_nombres_mex[j] = aux_nom_mex

            for k in range(len(lista_nombres_mex)):
                 print(lista_nombres_mex[k])
                 
                
def menu_de_opciones_10(lista_jovenes:list,opcion:int):
    if opcion == 10 :
                                    
                    for j in range(len(lista_jovenes[0]) - 1):
                        
                        for k in range(j+1,len(lista_jovenes[0])):
                            
                            if lista_jovenes[0][j] > lista_jovenes[0][k]:
                                aux_jov_1 = lista_jovenes[0][j]
                                lista_jovenes[0][j] = lista_jovenes[0][k]
                                lista_jovenes[0][k] = aux_jov_1

                                aux_jov_2 = lista_jovenes[1][j]
                                lista_jovenes[1][j] = lista_jovenes[1][k]
                                lista_jovenes[1][k] = aux_jov_2

                            elif lista_jovenes[0][j] == lista_jovenes[0][k]:
                                 if lista_jovenes[1][j] > lista_jovenes[1][k]:
                                    aux_jov_2 = lista_jovenes[1][j]
                                    lista_jovenes[1][j] = lista_jovenes[1][k]
                                    lista_jovenes[1][k] = aux_jov_2

                            

                    for l in range(len(lista_jovenes) - 1):
                        for m in range(len(lista_jovenes[l]) - 1):
                            print(lista_jovenes[l][m],lista_jovenes[1][m])
                
def menu_de_opciones_11(lista_mx_br_cp_mas_8000:list,opcion:int):
      
    if opcion == 11:
                    for j in range(len(lista_mx_br_cp_mas_8000[0]) - 1):
                        
                            for k in range(j+1,len(lista_mx_br_cp_mas_8000[0])):
                                
                                if lista_mx_br_cp_mas_8000[0][j] > lista_mx_br_cp_mas_8000[0][k]:
                                    aux_jov_1 = lista_mx_br_cp_mas_8000[0][j]
                                    lista_mx_br_cp_mas_8000[0][j] = lista_mx_br_cp_mas_8000[0][k]
                                    lista_mx_br_cp_mas_8000[0][k] = aux_jov_1

                                    aux_jov_8000 = lista_mx_br_cp_mas_8000[1][j]
                                    lista_mx_br_cp_mas_8000[1][j] = lista_mx_br_cp_mas_8000[1][k]
                                    lista_mx_br_cp_mas_8000[1][k] = aux_jov_8000

                                elif lista_mx_br_cp_mas_8000[0][j] == lista_mx_br_cp_mas_8000[0][k]:
                                    if lista_mx_br_cp_mas_8000[1][j] > lista_mx_br_cp_mas_8000[1][k]:
                                        aux_jov_8000 = lista_mx_br_cp_mas_8000[1][j]
                                        lista_mx_br_cp_mas_8000[1][j] = lista_mx_br_cp_mas_8000[1][k]
                                        lista_mx_br_cp_mas_8000[1][k] = aux_jov_8000

                    for i in range(len(mis_listas)):                                            
                        for j in range(len(mis_listas[i])):
                            
                            if mis_listas[i][j] == "Mexico" or mis_listas[i][j] == "Brazil":
                                if mis_listas[4][j] > 8000:
                                    
                                    for k in range(len(mis_listas)):                                   
                                        print(mis_listas[k][j])
                                    print("-----------------------------------------------------------")
    

def menu_de_opciones_almacen()->int:
    opcion = int(input("""
                       1-Alta de productos (producto nuevo)\n
                       2-Baja de productos (producto existente)\n
                       3-Modificar productos (cantidad, ubicación)\n
                       4-Listar productos\n
                       5-Lista de productos ordenado por nombre\n
                       6-Salir\n                       
                       Ingrese una opción: """))
    
    opcion = func.verifica_dentro_de_rango(opcion,1,6)

    return opcion

def menu_de_opciones_1_almacen(opcion:int,lista_de_productos:list)->list:
    if opcion == 1:
        producto_nuevo = input("Producto nuevo: ")

        cantidad_producto_nuevo =  int(input("Cantidad producto nuevo: "))
        cantidad_producto_nuevo = func.verifica_dentro_de_rango(cantidad_producto_nuevo,0,80)

        posicion_fila_producto_nuevo = int(input("Posicion de la fila del producto nuevo: "))
        posicion_fila_producto_nuevo = func.verifica_dentro_de_rango(posicion_fila_producto_nuevo,1,3)

        posicion_columna_producto_nuevo = int(input("Posicion de la columna del producto nuevo: "))
        posicion_columna_producto_nuevo = func.verifica_dentro_de_rango(posicion_columna_producto_nuevo,1,5)

        lista_de_productos[posicion_fila_producto_nuevo - 1][posicion_columna_producto_nuevo - 1] = [producto_nuevo,cantidad_producto_nuevo,[posicion_fila_producto_nuevo,posicion_columna_producto_nuevo]]
          
    return lista_de_productos

def menu_de_opciones_2_almacen(opcion_1:bool,opcion:int,lista_de_productos:list):
    if opcion == 2:
        if opcion_1 == True and opcion == 2:
            fila = int(input("Ingrese N° de fila del producto a eliminar: "))
            fila = func.verifica_dentro_de_rango(fila,1,3)
            columna = int(input("Ingrese N° de columna del producto a eliminar: "))
            columna = func.verifica_dentro_de_rango(columna,1,5)
            lista_de_productos[fila - 1][columna - 1] = -1
            
        else:        
            print("Error. Primero debe hacer el alta de productos")


def menu_de_opciones_3_almacen(opcion_1,opcion:int,lista_de_productos:list):
        
    if opcion == 3:  
     
        if opcion_1 == True :

            posicion_fila_producto = int(input("Posicion de la fila del producto a actual: "))
            posicion_fila_producto = func.verifica_dentro_de_rango(posicion_fila_producto,1,3)

            posicion_columna_producto = int(input("Posicion de la columna del producto a actual: "))
            posicion_columna_producto = func.verifica_dentro_de_rango(posicion_columna_producto,1,5)
            
            posicion_fila_producto_modificar = int(input("Posicion de la fila del producto a modificar: "))
            posicion_fila_producto_modificar = func.verifica_dentro_de_rango(posicion_fila_producto_modificar,1,3)

            posicion_columna_producto_modificar = int(input("Posicion de la columna del producto a modificar: "))
            posicion_columna_producto_modificar = func.verifica_dentro_de_rango(posicion_columna_producto_modificar,1,5)

            cantidad_producto_modificar =  int(input("Cantidad producto a modificar: "))
            cantidad_producto_modificar = func.verifica_dentro_de_rango(cantidad_producto_modificar,0,80)

            nombre_del_producto_modificar = input("Ingrese el nombre del producto a modificar: ")
            
            lista_de_productos[posicion_fila_producto - 1][posicion_columna_producto - 1] = lista_de_productos[posicion_fila_producto_modificar - 1][posicion_columna_producto_modificar - 1]

            lista_de_productos[posicion_fila_producto - 1][posicion_columna_producto - 1] = -1

            lista_de_productos[posicion_fila_producto_modificar][posicion_columna_producto_modificar] = [nombre_del_producto_modificar,cantidad_producto_modificar,[posicion_fila_producto_modificar,posicion_columna_producto_modificar]]
            

        else:        
            print("Error. Primero debe hacer el alta de productos")


def menu_de_opciones_4_almacen(opcion:int,lista_productos:list):
     if opcion == 4:
          func.printear_listas(lista_productos)


def menu_de_opciones_ferreteria()->int:
    opcion = int(input("""
                        1- Reponer mercadería (productos existentes)\n
                        2- Vender mercadería (producto existente, solo si alcanza el stock)\n
                        3- Listar inventario\n
                        4- Salir\n                      
                        Ingrese una opción: """))
    
    opcion = func.verifica_dentro_de_rango(opcion,1,4)

    return opcion

def menu_de_opciones_ferreteria_1(opcion:int,lista:list):
    if opcion == 1:
        producto_a_reponer = input("¿Que producto desea reponer?: ").lower()
        producto_a_reponer = func.verifica_nombre_dentro_de_lista(producto_a_reponer,lista)
        cantidad_a_reponer = int(input("¿Cuantos productos quiere reponer?: "))
        for i in range(len(lista)):            
            if lista[i][0] == producto_a_reponer:
                lista[i][1] += cantidad_a_reponer  

def menu_de_opciones_ferreteria_2(opcion:int,lista:list):
    if opcion == 1:
        producto_a_vender = input("¿Que producto desea vender?: ").lower()
        producto_a_vender = func.verifica_nombre_dentro_de_lista(producto_a_vender,lista)
        cantidad_a_vender = int(input("¿Cuantos productos quiere vender?: "))

        for i in range(len(lista)):            
            if lista[i][0] == producto_a_vender:

                while lista[i][1] < cantidad_a_vender:
                     cantidad_a_vender = int(input("Error, no hay esa cantidad para vender ¿Cuantos productos quiere vender?: "))

                lista[i][1] -= cantidad_a_vender 

def menu_de_opciones_ferreteria_3(opcion:int,lista:list):
    if opcion == 3:
        func.printear_listas(lista)
    