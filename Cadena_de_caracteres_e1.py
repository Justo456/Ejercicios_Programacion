'''Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto.'''


def cuenta_cantidad_letra_en_palabra(letra:str,cadena:str)->int:
    cantidad = 0
    for e_cadena in cadena:
        if e_cadena == letra:
            cantidad += 1

    return cantidad

cadena_de_carac = input("Ingrese una cadena de caracteres: ")
letra = input(f"Ingrese la letra que quiere saber cuantas veces aparece en {cadena_de_carac}: ")

print(f"La cantidad veces que aparece \"{letra}\" en \"{cadena_de_carac}\", es: {cuenta_cantidad_letra_en_palabra(letra,cadena_de_carac)}")