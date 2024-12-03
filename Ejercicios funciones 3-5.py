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