import random
'''Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida posición y número a guardar al usuario, lo 
guarde en una lista en la posición solicitada aleatoriamente y la retorne. 
El programa principal debe invocar a la función y mostrar por pantalla el retorno.'''


def pide_pos_y_num()->list:

    lista_numeros = [0] * 10
    numero = int(input("Ingrese un numero: "))

    posicion_aleatoria = random.randint(0,9)
    
    lista_numeros[posicion_aleatoria] = numero

    return lista_numeros

ret = pide_pos_y_num()
# mensaje_total = ""
# for i in range(len(ret)):
#     mensaje = ret[i]
#     mensaje_total += f"'{mensaje}' "
   
# print(f"La posicion aleatoria en la que se encuentra su numero es: {i} ({mensaje_total})")

print(ret)