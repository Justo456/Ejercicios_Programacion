'''Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona.'''

nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))
aumento = sueldo + sueldo*0.10
print(f"Su sueldo con aumento es de: {aumento}")