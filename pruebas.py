# matriz = [[2,4,5,8],[6,3,1,9]]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end=" ")
#     print("")

# print(matriz[0][2])

# matriz[0][2] = 15

# print(matriz[0][2])

# def inicilizador_de_matriz(cantidad_de_filas:int,cantidad_de_columnas:int,valor_inicial:any)->list:
#     matriz = []

#     for i in range(cantidad_de_filas):

#         filas = [valor_inicial] * cantidad_de_columnas

#         matriz += [filas]

#     return matriz

# ret = inicilizador_de_matriz(3,3,0)
# print(ret)

# def cargar_matriz_secuencial(matriz:list):

#     for i in range(len(matriz)):
        
#         for j in range(len(matriz[i])):
#             matriz[i][j] = int(input(f"Ingrese un numero en la fila {i} columna {j}: "))
            
#     return matriz

# ret_llena = cargar_matriz_secuencial(ret)
# print(ret_llena)

from listas_personas import mis_listas
from GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_menu_de_opciones import *
from GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_matrices import *
# for i in range(len(mis_listas)):
#     for j in range(len(mis_listas[i])):
#         if mis_listas[i][j] == "Brazil":
#             pos_j_Brazil = j
#             break

# for k in range(len(mis_listas)):
#     print(mis_listas[k][pos_j_Brazil])

# for i in range(len(mis_listas)):
#     for j in range(len(mis_listas[i])):
#         if mis_listas[i][j] == "Brazil":
#             pos_j_Brazil = j
#             break


# for k in range(len(mis_listas)):
#     if mis_listas[k] == mis_listas[0] or mis_listas[k] == mis_listas[1] or mis_listas[k] == mis_listas[2]:
#         print(mis_listas[k][pos_j_Brazil])   


# for i in range(len(mis_listas)):
#                 for j in range(len(mis_listas[i])):
#                     if mis_listas[i][j] == "Brazil":
#                         pos_j_Brazil = j
#                         break

# for k in range(len(mis_listas)):
#     if mis_listas[k] == mis_listas[0] or mis_listas[k] == mis_listas[1] or mis_listas[k] == mis_listas[2]:
#         print(mis_listas[k][pos_j_Brazil])
    

# for i in range(len(mis_listas)):
#                 for j in range(len(mis_listas[i])):
#                     if mis_listas[i][j] == "Mexico":
                                                                           
#                         for k in range(len(mis_listas)):
#                             print(mis_listas[k][j])

# lista = [["Juan"],["Roman",2,[1,2]],["Pedro"]]

# for e_lista in lista:
#     print(e_lista)
# seguir = "s"


# while seguir == "s":
#     opcion = int(input("2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\n9-Listar los datos de los usuarios de México ordenados por nombre\nIngrese una opción: "))
#     while opcion > 9 or opcion < 2:    
#         opcion = int(input("ERROR.\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años\n9-Listar los datos de los usuarios de México ordenados por nombre\nIngrese una opción: "))
#     if opcion == 2:
#         opcion_2 = True 
        
#     lista_noms_Mex = menu_de_opciones_2(opcion)

#     menu_de_opciones_9(lista_noms_Mex,opcion,opcion_2)

# nombre = "Hola"
# print(nombre + ".txt")

# variable = "nombre_archivo"
# extensión= "csv"
# variable = ".".join([variable, extensión])
# print(variable)
# variable = 1
# for i in range(1,variable + 1):
#     print(variable)

