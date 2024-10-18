'''5) Crear una función que reciba una cadena por parámetro y suprima las
vocales de la misma.'''

def suprime_vocales(cadena:str)-> str:
    '''Suprime vocales dentro de una cadena de carteres'''
    lista_cadena = []
    for i in range(len(cadena)):
        lista_cadena.append(cadena[i])
    
    for j in range(len(lista_cadena)):           
            if lista_cadena[j] == "a" or lista_cadena[j] == "e" or lista_cadena[j] == "i" or lista_cadena[j] == "o" or lista_cadena[j] == "u":
                lista_cadena[j] = ""

    mensaje_total = ""

    for l in range(len(lista_cadena)):
        mensaje = lista_cadena[l]            
        mensaje_total += mensaje

    return mensaje_total

cadena_de_carac = input("Ingrese una cadena de caracteres: ")
print(suprime_vocales(cadena_de_carac))