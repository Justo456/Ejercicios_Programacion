'''Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
programa principal realizando la invocación o llamada.'''

def es_par(par1:int)->bool:
    if par1 % 2 == 0:
        resultado = True
    else:
        resultado = False
    
    return resultado

numero = int(input("Ingrese un numero: "))
ret = es_par(numero)
print("¿Es par tu numero?: ",ret)