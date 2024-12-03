'''Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
como parámetro.'''

def muestra(numero1:int)->int:
    '''Muestra el numero que recibe como parametro'''
    print("Su numero es: ", numero1)


num1 = int(input("Ingrese un numero: "))
muestra(num1)