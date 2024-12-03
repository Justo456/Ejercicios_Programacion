from Funciones_profe_genericas import *
import random

def genera_numero_aleatoriamente_en_un_rango(inicio:int,final:int):
    '''Retorna un numero aleatorio entre "Inicio" y "Final" inclusive'''
    return random.randint(inicio,final)

def agrega_numeros_aleatorios_a_lista(lista:list,cantidad:int):
    '''Recibe una lista y le agrega una cierta cantidad de numeros de forma aleatoria
    cantidad = Cantidad de veces que se le quieren agregar los numeros aleatorios'''
    for i in range(len(lista)):
        for j in range(cantidad):
            lista[i]["piezas"].append(genera_numero_aleatoriamente_en_un_rango(1,3))
    return lista



def verifica_en_vertical(lista:list,fila:int,columna:int,cant_en_ver):
    '''Recibe una matriz y una cantidad de veces que se quiere encontrar un valor dentro de esta matriz de forma vertical,
    el valor es la fila-columna de la matriz
    Lista = Matriz a evaluar
    fila = indice para la fila en la matriz
    columna = indice para la columna en la matriz
    cant_en_ver =  cantidad de veces que deberia aparecer el valor en vertical en la matriz para que retorne Verdadero'''
    retorno = False
    fila -= 1
    columna = columna - 1
    cont_total = 0
    
    for i in range(len(lista) - fila):#recorre hacia abajo
        if lista[fila][columna] == lista[fila + i][columna] and cant_en_ver != cont_total:
            cont_total += 1
        else: 
            break
    if cont_total == cant_en_ver:
        retorno = True
    else:
        for i in range(fila + 1):#recorre hacia arriba
            if lista[fila][columna] == lista[fila - i][columna]:
                cont_total += 1
            else: 
                break
        if cont_total == cant_en_ver:
            retorno = True
        
    return retorno
  

def pide_una_fila()->int:
    '''Pide una fila y verifica si existe dentro de una matriz'''
    fila = 0
    fila = int(input("Ingrese una fila: "))
    fila = verifica_numero_dentro_de_rango(fila,1,4)
    return fila

def pide_una_columna()->int:
    '''Pide una columna y verifica si existe dentro de una matriz'''
    columna = 0
    columna = int(input("Ingrese una columna: "))
    columna = verifica_numero_dentro_de_rango(columna,1,7)
    return columna