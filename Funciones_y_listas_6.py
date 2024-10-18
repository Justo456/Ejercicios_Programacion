'''Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo listas_personas.py. Importar los nombres a una lista. 
Realizar una función que muestre los mismos.'''
from listas_personas import nombres

lista_nombres = nombres
def muestra_lista(lista:list)->str:
    mensaje_total = ""
    for i in range(len(lista)):
        mensaje = lista[i]
        mensaje_total += f"'{mensaje}' "
    return mensaje_total

ret = muestra_lista(lista_nombres)
print(ret)
