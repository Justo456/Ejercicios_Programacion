'''4) Crear una función que reciba como parámetro una cadena y suprima los
caracteres repetidos.'''


def suprime_caracteres_repetidos(cadena:str)-> str:
    '''Suprime caracteres repetidos dentro de una cadena de carteres'''
    lista_cadena = []
    for i in range(len(cadena)):
        lista_cadena.append(cadena[i])
    
    for j in range(len(lista_cadena)-1):
        for k in range(j+1,len(lista_cadena)):            
            if lista_cadena[j] == lista_cadena[k]:
                lista_cadena[k] = ""
    mensaje_total = ""
    for l in range(len(lista_cadena)):
        mensaje = lista_cadena[l]            
        mensaje_total += mensaje

    return mensaje_total

cadena_de_carac = input("Ingrese una cadena de caracteres: ")
print(suprime_caracteres_repetidos(cadena_de_carac))
