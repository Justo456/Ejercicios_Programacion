'''Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
como parámetro.'''

def muestra(numero1:int)->int:
    '''Muestra el numero que recibe como parametro'''
    print("Su numero es: ", numero1)


num1 = int(input("Ingrese un numero: "))
muestra(num1)

'''Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.'''
def muestra()->int:
    '''Muestra un numero ingresado'''
    retorno = int(input("Ingrese un numero: "))
    print(retorno)
    return retorno

numero = muestra()
print("Su numero es: ", numero)

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

'''Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en sus 4 combinaciones.
 Restar1(int, int)->int:
 Restar2()->int:
 Restar3(int, int):
 Restar4():'''

def restar1(par1:int,par2:int)->int:

    retorno = par1 - par2
    return retorno

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

ret = restar1(num1,num2)
print(f"El resultado de la resta es: {ret}")

def restar2()->int:
    num1 = int(input(f"Ingrese un numero: "))
    num2 = int(input(f"Ingrese otro numero: "))
    resultado = num1 - num2
    return resultado

result = restar2()
print(f"El resultado de la resta es: {result}")

def restar3(par1:int,par2:int):
    resultado = par1 - par2
    print(f"El resultado de la resta es {resultado}")

restar3(10,20)

def restar4():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

restar4()

'''Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario, valide el mismo entre 10 y 100, 
realice un descuento del 5% a dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado por pantalla. 
Atención: pueden reutilizarse funciones ya creadas.'''


def realizarDescuento(par1:int)-> int:
    descuento = 0.95
    valor_con_descuento = par1 * descuento
    print(f"El el valor con el %5 de descuento es de: {valor_con_descuento}")





numero1 = int(input("Ingrese un valor entre 10 y 100: "))
while numero1 < 10 or numero1 > 100:
    numero1 = int(input("Error.Ingrese un  entre 10 y 100: "))

realizarDescuento (numero1)

'''Ejercicio 3-7: Realizar un programa que: 
asigne a las variables numero1 y numero2 los valores solicitados al usuario, 
valide los mismos entre 10 y 100, 
asigne a la variable operacion el valor solicitado al usuario: 
's'-sumar, 'r'-restar (validar), 
realice la operación de dichos valores a través de una función. Mostrar el resultado por pantalla.'''

def restar_o_sumar(valor1:int,valor2:int,suma_o_resta:str):
    if suma_o_resta == "s" or suma_o_resta == "sumar":
        resultado_suma = valor1 + valor2
        resultado = resultado_suma
    else:
        resultado_resta = valor1 - valor2
        resultado = resultado_resta
    
    print(f"El resultado de la operacion es: {resultado}")



numero1 = int(input("Ingrese un valor entre el 10 y el 100: "))
while numero1 < 10 or numero1 > 100:
    numero1 = int(input("Error.Ingrese un valor entre el 10 y el 100: "))

numero2 = int(input("Ingrese un valor entre el 10 y el 100: "))
while numero2 < 10 or numero2 > 100:
    numero2 = int(input("Error.Ingrese un valor entre el 10 y el 100: "))

operacion = input("Que quiere hacer: Sumar(s) o Restar(r)").lower()
while operacion != "s" and operacion != "sumar" and operacion != "r" and operacion != "restar":
    operacion = input("Error.Que quiere hacer: Sumar(s) o Restar(r)").lower()

restar_o_sumar(numero1,numero2,operacion)


