'''Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en un rango determinado pasado por parámetro “desde”-“hasta”.'''

def muestra_3_1(numero1:int,desde:int,hasta:int)->int:
    '''Muestra si el numero es valido dentro de un rango'''
    if numero1 > desde or numero1 < hasta:
        print(f"Numero dentro del rango")
    else:
        print(f"Numero fuera del rango")
        


def muestra_3_2(desde:int,hasta:int)->int:
    '''Muestra si el numero es valido dentro de un rango'''
    numero = int(input("Ingrese un numero: "))
    while numero < desde or numero > hasta:
        numero = int(input("Error.*Numero fuera de rango*Ingrese un numero: "))
    retorno = ("Numero dentro de el rango")

    return retorno

muestra_3_1(15,20,100)

resultado = muestra_3_2(100,200)
print(resultado)