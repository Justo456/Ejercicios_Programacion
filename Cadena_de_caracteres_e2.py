'''Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar.'''

def imprime_o_no_de_un_indice_hasta_otro(cadena:str,indice1:int,indice2:int):
        
        if len(cadena) > indice1 and len(cadena) > indice2:
            mensaje = cadena[indice1:indice2]
        else:
            mensaje = f"Los indices no son validos para '{cadena}'"
        return mensaje

cadena_de_carac = input("Ingrese una cadena de caracteres: ")
indice_1 = int(input(f"Ingrese la posicion de donde quiere empezar a imprimir {cadena_de_carac}: "))
indice_2 = int(input(f"Ingrese la posicion de donde quiere terminar de imprimir {cadena_de_carac}: "))

print(imprime_o_no_de_un_indice_hasta_otro(cadena_de_carac,indice_1,indice_2))
