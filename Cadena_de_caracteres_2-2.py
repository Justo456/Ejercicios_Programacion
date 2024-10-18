'''Crear una función que reciba una cadena y un caracter. La función deberá
devolver el índice en el que se encuentre la primera incidencia de dicho
caracter, o -1 en caso de que no esté.'''


def indice_donde_se_encuentra_x_caracter(cadena:str,caracater:str)->int:
    '''Muestra el numero de indice en el que se encuentra un caracter'''
   
    for i in range(len(cadena)):
        if cadena[i] == caracater:
            mensaje = i
            break
        else:
            mensaje = -1
    
    return mensaje


cadena_de_carac = input("Ingrese una cadena de caracteres: ")
caracter = input("Ingrese el caracater que quiere saber la posicion en la que se encuentra: ")

if indice_donde_se_encuentra_x_caracter(cadena_de_carac,caracter) != -1:
    print(f"La posicion de su caracter es: {indice_donde_se_encuentra_x_caracter(cadena_de_carac,caracter)}")
else:
    print("Su caracter no se encuentra en ninguna posicion")