'''Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.'''
def muestra()->int:
    '''Muestra un numero ingresado'''
    retorno = int(input("Ingrese un numero: "))
    print(retorno)
    return retorno

numero = muestra()
print("Su numero es: ", numero)