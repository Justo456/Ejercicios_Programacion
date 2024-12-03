'''Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
<número de caracteres> - 1.'''

def char_at(cadena:str,numero:int)->any:
    if numero < len(cadena):
        mensaje = cadena[numero]
    else:
        mensaje = f"Posicion indicada invalida"
    return mensaje

cadena_de_carac = input("Ingrese una cadena de caracteres: ")
posicion = int(input("Ingrese el indice de la cadena de caracteres que quiere mostrar: "))

print(char_at(cadena_de_carac,posicion + 1))