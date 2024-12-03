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


