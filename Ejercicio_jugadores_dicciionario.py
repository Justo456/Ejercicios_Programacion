# jugadores = [
#          {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
#          {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
#          {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
#          {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
# ]

# #Si puntos es menor a 10 guardar nombres

# #ordenar de manera descendente los nombres

# for i in range(len(jugadores)-1):

#     for j in range(i+1,len(jugadores)):

#         if jugadores[i]["nombre"] < jugadores[j]["nombre"]:

#             aux_i = jugadores[i]    
#             jugadores[i] = jugadores[j]
#             jugadores[j] = aux_i


# for k in range(len(jugadores)):
#     print(jugadores[k])

#buscar el de menor edad y mostrar su nombre
# jugadores = [
#          {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
#          {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
#          {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
#          {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
# ]

# edad_menor = jugadores[0]["edad"]

# for i in range(len(jugadores)):

#     if jugadores[i]["edad"] < edad_menor:
#         edad_menor = jugadores[i]["edad"]
#         nombre_menor = jugadores[i]["nombre"]

# print(nombre_menor)

#acumular los puntos de cada jugador

jugadores = [
         {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
         {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
         {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
         {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
]

for i in range(len(jugadores)):
    acumulador = 0
    for j in range(len(jugadores[i]["puntos"])):

        acumulador += jugadores[i]["puntos"][j]
    
    print(f"{jugadores[i]["nombre"]},{acumulador} puntos acumulados")

