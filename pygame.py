from funciones_pygame import *

lista = [
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]}
 ]

ganador = "s"

lista_numeros_aleatorios = crear_lista_valores(agrega_numeros_aleatorios_a_lista(lista,7),"piezas")

while ganador == "s":

    for e_lista_nums in lista_numeros_aleatorios:
        print(e_lista_nums)

    if verifica_en_vertical(lista_numeros_aleatorios,pide_una_fila(),pide_una_columna(),3):
        print("HA GANADO 10 PUNTOS")
        
    else:
        print("SEGUI PARTICIPANDO")

    ganador = input("¿Desea seguir probando? (s/n): ").lower()
    while ganador != "s" and ganador != "n":
        ganador = input("Error.¿Desea seguir probando? (s/n): ").lower()

#Fusionar las funcioner arriba y abajo ✅
#Agregar cantidad de veces que deberia aparecer el valor en vertical en la matriz ✅
#Validar si en el primer recorrido ya conto la cantidad necesaria ✅
#Hacer el archivo ❌
#Hacer el pygame ❌