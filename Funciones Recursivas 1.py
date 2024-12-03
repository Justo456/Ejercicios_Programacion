'''1. Realizar una función recursiva que calcule la suma de los primeros números naturales:'''

def sumar_naturales(numero:int)->int:
    '''Suma de los primeros numeros naturales'''
    if numero < 0:
        return "invalido"
    if numero > 9:
        return 0
    else:
        return numero + sumar_naturales(numero + 1)
#1er llamada    0   +    1
#2da llamada    1   +    2
#3er llamada    2   +    3
#...

primer_numero_natural = 0
sumar_naturales(primer_numero_natural)
print(f"La suma de los primeros numeros naturales es {sumar_naturales(primer_numero_natural)}")


    
