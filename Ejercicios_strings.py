'''Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una
cadena.
Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.
Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra
en una cadena.'''

# cadena = "hola mundo"

# def invierte_caracteres_de_cadena(cadena:str):
    
#     print(cadena[::-1])

# invierte_caracteres_de_cadena(cadena)


#2

# def cuantas_palabras_en_cadena(cadena:str):
    
#     cadena = cadena.split(' ')
#     if cadena[-1] == "":
#         print(len(cadena)-1)
#     elif cadena[0] == "":
#         print(len(cadena)-1)
#     else:
#         print(len(cadena))

# cuantas_palabras_en_cadena(cadena)

#3
# def reemplaza_palabra_especifica(cadena:str):

#     print(cadena.replace("mundo", "universo")) 

# reemplaza_palabra_especifica(cadena)

#4

# lista_peli = [
# ["Matrix", "El Padrino", "Titanic"],
# ["Forrest Gump", "Pulp Fiction", "Gladiador"],
# ["Blade Runner", "El Rey León", "Volver al Futuro"],
# ["La La Land", "El Gran Lebowski", "Blade Runner"],
# ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
# ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
# ["Titanic", "Star Wars", "El Señor de los Anillos"],
# ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
# ["Forrest Gump", "The Godfather", "Goodfellas"],
# ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
# ]

# def convierte_elementos_de_lista_en_cadena(lista:list):
    
#     for i in range(len(lista)):   
#             mensaje = ""       
#             for j in range(len(lista[i])):

#                 pelicula = lista[i][j]           
#                 mensaje += f"{pelicula},"
                
                
#             print(f"Se recomienda ver {mensaje}")
    
# convierte_elementos_de_lista_en_cadena(lista_peli)

#5

# cadena = "hola mundo"

# def capitaliza_palabras(cadena:str):

#     return cadena.capitalize()

# print(capitaliza_palabras(cadena))

#6


# def es_palindromo(cadena:str)->bool:
#     '''Retorna si la cadena de caracteres es un palindromo o no'''
    
#     cadena = cadena.lower()

#     palindromo = False

#     if cadena == cadena[::-1]:
#         palindromo = True
       
#     return palindromo

# cadena_de_carac = input("Ingrese una cadena de caracteres: ")

# if es_palindromo(cadena_de_carac):
#     print("Es un palíndromo")
# else:
#     print("No es un palíndromo")

#7

# def ordenar(lista:list, clave:str, orden:int):
#     '''Ordenar una lista de diccionaro por la clave solicitada con el criterio de ordenamiento pasado por parametro
#     Lista: es la lista a ordenar
#     Clave: key del diccionario por la cual voy a ordenar
#     Orden: 1 = ascendente   -1 = descendente
#     '''

#     for i in range(len(lista)-1):
#         for j in range(i+1,len(lista)):
#             if orden == 1:
#                 if lista[i][clave] > lista[j][clave]:
#                     intercambiar(lista, i, j)
            
#             if orden == -1:
#                 if lista[i][clave] < lista[j][clave]:
#                     intercambiar(lista, i, j)
            

# def intercambiar(lista:list,posicion1:int,posicion2:int):
#     '''Intercambiar posciones'''
#     aux = lista[posicion1]
#     lista[posicion1] = lista[posicion2]
#     lista[posicion2] = aux
