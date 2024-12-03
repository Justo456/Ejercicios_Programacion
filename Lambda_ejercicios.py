# '''Ejercicio 1: Crear una función lambda que incremente un 10% en el sueldo recibido.'''

# sueldo = int(input("Ingrese un sueldo: "))

# sueldo_incrementado = (lambda sueldo: sueldo*1.10)(sueldo)

# print(f"Sueldo incrementado: {sueldo_incrementado}")


# '''Ejercicio 2: Crear una función lambda que informe si una persona es mayor (mayor a
# 17 años) o menor.'''

# edad = int(input("Ingrese su edad: "))

# num = (lambda edad: "Es mayor" if edad > 17 else "Es menor")(edad)
# print(num)

# '''Ejercicio 3: Crear una función lambda que indique si el número recibido es par o
# impar'''

# num = int(input("Ingrese un numero: "))

# print((lambda num: "Es par" if num%2 == 0 else "Impar")(num))

# '''Ejercicio 4: Crear una función lambda que indique si el número recibido es positivo o
# negativo'''

# num = int(input("Ingrese un numero: "))

# print((lambda num: "Positivo" if num >= 0 else "Negativo")(num))

# '''Ejercicio 5: Crear una función lambda que realice un 10% de descuento en el
# importe recibido.'''

# importe = int(input("Ingrese un importe: "))

# print((lambda importe: importe*0.90)(importe))

# '''Ejercicio 6: Crear una función lambda devuelva el doble del número recibido.'''

# num = int(input("Ingrese un numero: "))

# print((lambda num: num*2)(num))

# '''Ejercicio 7: Crear una función lambda que devuelva el texto “femenino” si recibe el
# valor “f” y sino “masculino”'''

# genero = input("Ingrese 'f' para femenino y cualquier otra cosa para masculino: ")

# print((lambda genero: "femenino" if genero == "f" else "masculino")(genero))
