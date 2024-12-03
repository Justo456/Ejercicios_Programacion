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