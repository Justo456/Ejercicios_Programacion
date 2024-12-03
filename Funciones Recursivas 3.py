'''3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:'''

def sumar_digitos(numero:int)->int:
    if numero == 0:
        return 0
    
    else:
        return (numero % 10) + sumar_digitos(numero // 10)
    #1ra llamada      0      +   sumar_digitos(100)
    #2da llamada      0      +   sumar_digitos(10)
    #3ra llamada      0      +   sumar_digitos(1)
    #4ta llamada      1      +   sumar_digitos(0)

numero = 1000
resultado = sumar_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}")