'''Desafío:
Realizar una función con el siguiente Menú de Opciones:
A. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por
Nombre de manera ascendente.
B. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de
género M.
C. Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de
ojos.
D. Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo.
E. Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
E. Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género
femenino
F. Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un
nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el
IMC calculado.
Nota:
Crear una función para cada opción de menú.
Desarrollar las funciones en una biblioteca.
Utilizar todo lo visto en clases, métodos, funciones lambda, operadores ternarios, etc.'''
from copy import deepcopy
from data_stark import lista_personajes
from Funciones_profe_genericas import *
lista_personajes_copia = deepcopy(lista_personajes) 

def menu_de_opciones_stark(lista:list)->int:
    opcion = int(input("""
                       1-Lista ordenado por nombre
                       2-Listar Masculinos debiles
                       3-Cantidad de color de ojos
                       4-Listar por color de Pelo
                       5-Listar Inteligencia
                       6-Listar Promedio
                       7-Asignar IMC
                       Ingrese una opcion:"""))
    
    verifica_numero_dentro_de_rango(opcion,1,7)

    if opcion == 1:
        ordenar(lista,"nombre",1)
        invocar_tabla(lista[0])
        mostrar_todos(lista)

    elif opcion == 2: 

        invocar_tabla(lista[0])
        for i in range(len(lista)):
            if int(lista[i]["fuerza"]) == min_max(crear_lista_valores(compara_clave_igual_xvalor(lista,"genero","M"),"fuerza"),1) and lista[i]["genero"] == "M":
                mostrar_informacion_en_tabla(lista[i])
                

                
    
    elif opcion == 3:

        lista_color_de_ojos = crear_lista_valores(lista,"color_ojos")
        lista_color_de_ojos_copia = lista_color_de_ojos.copy()
        lista_colores_r_eliminados = elimina_elementos_repetidos(lista_color_de_ojos_copia)
        
        for i in range(len(lista_colores_r_eliminados)):       
            contador = cuenta_elementos_iguales(lista_color_de_ojos,lista_colores_r_eliminados[i])
            print(f"La cantidad de ojos color {elimina_elementos_repetidos(lista_color_de_ojos_copia)[i]} es {contador}")
           

    elif opcion == 4:
        
        
        for e_lista in elimina_elementos_repetidos(crear_lista_valores(lista,"color_pelo")):  
            print(f"\nHeroes con pelo color {e_lista} \n")   
            invocar_tabla(lista[0])     
            mostrar_todos(compara_clave_igual_xvalor(lista,"color_pelo",e_lista))

    elif opcion == 5:

            for e_lista in elimina_elementos_repetidos(crear_lista_valores(lista,"inteligencia")):  
                print(f"\nHeroes con inteligencia {e_lista} \n")   
                invocar_tabla(lista[0])     
                mostrar_todos(compara_clave_igual_xvalor(lista,"inteligencia",e_lista))
    
    elif opcion == 6:
        
        for i in range(len(lista)):
            if int(crear_lista_valores(lista,"fuerza")[i]) > promediar_valores_dic(crear_lista_valores(compara_clave_igual_xvalor(lista,"genero","F"),"fuerza")):
                print(lista[i]["nombre"])
                print(lista[i]["peso"])
                print("---------------------------------------------")

    elif opcion == 7:

        for e_lista in lista:
            e_lista["IMC"] = (lambda peso,altura: str(float(peso)/((float(altura)/100) ** 2)))(e_lista["peso"],e_lista["altura"])
        invocar_tabla(lista[0])
        mostrar_todos(lista)