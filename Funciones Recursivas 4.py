'''4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:
Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
'''
def calcula_numero_Fibonacci(numero,f_0:int,f_1:int)->int|None:
    resultado = 0
    if numero >= 0:
        
        suma_f = f_0 + f_1
        anterior = f_1
        subsecuente = suma_f + anterior
        resultado = subsecuente + anterior
        if numero == 0:
            return 

        else:
            calcula_numero_Fibonacci(numero - 1,f_0 = suma_f,f_1 = anterior)            
    else:
        return None            
        
numero_ingresado = int(input("Ingrese un numero mayor o igual a 0: "))
fibonacci_0 = 0
fibonacci_1 = 1
calcula_numero_Fibonacci(numero_ingresado,fibonacci_0,fibonacci_1)


