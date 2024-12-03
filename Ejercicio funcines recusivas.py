'''Ejercicio:
● Numero primos son:
● Número entero positivo mayor que el número uno y que
● solo puede ser divisible sin resto por el número uno y por el mismo.
● Los primeros números primos son:
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47, ...
● Realizar un programa que solicite un número y a través de una función
recursiva determine si el número es primo.'''


def es_primo(primo:int,cont_div:int,i:int)->bool:
    
    if i > primo:
        return cont_div == 2
    if primo%i == 0:
        cont_div += 1

    return es_primo(primo,cont_div, i + 1)
    



numero = int(input("Ingrese un numero: "))
resultado = es_primo(numero,0,1)
if resultado:
    print("Es primo")
else:
    print("No es primo")
