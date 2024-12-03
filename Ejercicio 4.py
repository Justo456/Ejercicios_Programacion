'''Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero", 
mostrar el siguiente mensaje: 'Es muy pequeño para NO ser soltero.'''


edad = int(input("Ingrese su edad: "))
estado_civil = input("Ingrese su estado civil: Casado/a - Soltero/a - Divorciado/a - Viudo/a : ").lower()

while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "divorciado" and estado_civil != "viudo" and estado_civil != "soltera" and estado_civil != "casada" and estado_civil != "divorciada" and estado_civil != "viuda":
        estado_civil = input("Error. Ingrese su estado civil de nuevo: ")

if edad < 18 and estado_civil != "soltero":
    print("Es muy pequeño/a par No ser soltero.")

