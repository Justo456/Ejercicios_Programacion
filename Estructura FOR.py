# 1. Mostrar los números ascendentes desde el 1 al 10
for i in range (1,11):
   print(i)

#2. Mostrar los números descendentes desde el 10 al 1
numero = 11
for i in range (10):
   print(i-1)
#3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
numero = int(input("Ingrese un numero: "))
for i in range (-1,numero):
   print(i+1)
#4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
#5 x 0 = 0
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15 …
numero = int(input("Ingrese un numero: "))
for i in range (11):
   print(numero*i)
#5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
#número 0. Mostrar la suma y el promedio de todos los números.
suma = 0
for i in range (10):
   numero = int(input("Ingrese 10 numeros, o termine el programa ingresando el 0: "))
   if numero == 0 or i > 10:
       break
   suma += numero
if i > 0:
   promedio = suma/i
else:
   promedio = "No hay"
print(f"La suma es {suma} y el promedio {promedio}")

#6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

for i in range (1,11):
    if i%3 == 0:
        multiplos_3 = i
        print("Multiplos de 3: ", multiplos_3)

#7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
for i in range (1,51):
    if i%2 == 0:
        print(i)
#8. Realizar un programa que permita mostrar una pirámide de números. Por
#ejemplo: si se ingresa el numero 5, la salida del programa será la
#siguiente:

veces = int(input("Ingrese un numero entero: "))

for i in range (1,veces+1):
    linea_numeros = ""
    for j in range (1,i+1):
        linea_numeros += str(j)

    print(linea_numeros)

#9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
#el número ingresado. Mostrar la cantidad de divisores encontrados.
cont_divisores = 0
numero = int(input("Ingrese un número: "))
for i in range (1,numero+1):
    if numero%i == 0:
        divisores = i
        cont_divisores += 1
        print(f"Los divisores de su numero son: {divisores}")
    
print(f"La cantidad de divisores: {cont_divisores}")
#10.Ingresar un número. Determinar si el número es primo o no.

cont_divisores = 0
numero = int(input("Ingrese un numero: "))
for i in range (1,numero + 1):
    if numero%i == 0:
        cont_divisores += 1
if cont_divisores == 2:
    print("Su numero es primo")
else:
    print("Su numero no es primo")


#11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
#número ingresado. Informar cuántos números primos se encontraron.

cont_divisores = 0
primos = 0
cont_primos = 0
hay_primos = False
mensaje = ""

numero = int(input("Ingrese un numero: "))

for i in range (1,numero + 1):
    cont_divisores = 0
    for j in range (1,i + 1):
        if i%j == 0:
            cont_divisores += 1
            
    if cont_divisores == 2:
        cont_primos += 1
        primos = i
        mensaje += f"({str(primos)})"
        hay_primos = True
if hay_primos == False:
    mensaje = "no hay"    

print(f"El/los numero/s primo/s entre el 1 y el {numero} es/son: {mensaje}")
print(f"Y hay: {cont_primos} numero/s primo/s")

