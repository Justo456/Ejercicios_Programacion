'''Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).'''

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    mensaje = "Mayor de edad"
elif edad >= 12:
    mensaje = "Adolescente"
else:
    mensaje = "Niño/a"

print(f"La persona es: {mensaje}") 
