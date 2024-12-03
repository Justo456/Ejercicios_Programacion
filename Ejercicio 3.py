'''Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.'''

pares = 0
pares_max = 0
impares = 0
numero_min = 0
suma_positivos = 0
producto_negativos = 1
bandera_min = False
bandera_par = False
for numeros in range(5):

    numeros = int(input("Ingrese un número entero: "))

    while numeros == 0:
        numeros = int(input("Error. Ingrese un número entero: "))

    if numeros > 0:
        numeros_positivos = numeros
        suma_positivos += numeros_positivos
    else:
        numeros_negativos = numeros
        producto_negativos *= numeros_negativos

    resto_numeros = numeros % 2

    if resto_numeros == 0:
        pares += 1 
        par = numeros
    else:
        impares += 1

    if numeros < numero_min or bandera_min == False:
        numero_min = numeros
        bandera_min = True

    if par > pares_max or bandera_par == False:
        pares_max = par
    
print("Cantidad de pares ("+ str(pares) +")\nCantidad de impares ("+ str(impares) +")\nMenor número ingresado :("+ str(numero_min) +")\nMayor par ingresado("+ str(pares_max) +")\nSuma de los positivos("+ str(suma_positivos) + ")\nProducto de los negativos ("+ str(producto_negativos) +")")


