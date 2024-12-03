'''Enunciado/s:
Tabla de Posiciones de Torneo de Ping-Pong
Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
Los datos que se cargarán son:
Nombre del jugador
Edad (validar)
Cantidad de puntos (validar-número entero positivo, hasta 60).
Número de partidos ganados (validar-número entero positivo, hasta 35).
Tipo de saque ("plano", "liftado", "cortado")
Categoría ("elite", "experto", "avanzado")
Se necesita saber
Tema A:
1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive.
2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
3-Porcentaje de jugadores de categoría "experto".
4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.'''

seguir = "si"
cant_jug_eli_plan_18_25 = 0
edad_min = 0
bandera_min = False
cont_experto = 0
cont_elite = 0
cont_avanzado = 0
cont_cortado = 0
cont_plano = 0
cont_liftado = 0
suma_contadores = 0
suma_edades_avanzados = 0
nombre_menos_edad_mas_50 = ""
categoria_menor_edad_mas_50 = ""
nombre_categoria_menos_edad_mas_50_puntos = ""
edad_min_avanzados = 0

while seguir == "si":
    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese su edad (entre 18 y 99 años): "))
    while edad < 18 or edad > 100:
        edad = int(input("Error.Ingrese su edad (entre 18 años y 99 años): "))

    cantidad_puntos = int(input("Ingrese la cantidad de puntos ganados (entre 1 y 60): "))
    while cantidad_puntos <= 0 or cantidad_puntos >= 60:
        cantidad_puntos = int(input("Error.Ingrese la cantidad de puntos ganados (entre 1 y 60): "))
    
    num_partidos_ganados = int(input("Ingrese la cantidad de partidos ganados (entre 1 y 35): "))
    while num_partidos_ganados <= 0 or num_partidos_ganados >= 35:
        num_partidos_ganados = int(input("Error.Ingrese la cantidad de partidos ganados (entre 1 y 35): "))
    
    tipo_saque = input("Ingrese su tipo de saque (plano-liftado-cortado): ").lower()
    while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
        tipo_saque = input("Error.Ingrese su tipo de saque (plano-liftado-cortado): ").lower()

    categoria = input("Ingrese su categoria (elite-experto-avanzado): ").lower()
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Error.Ingrese su categoria (elite-experto-avanzado): ").lower()
    
    seguir = input("Desea seguir: si/no: ").lower()
    while seguir != "si" and seguir != "no":
        seguir = input("Error. Desea seguir: si/no: ").lower()
    
    
    if (edad < edad_min or bandera_min == False) and (cantidad_puntos > 50):
        nombre_menos_edad_mas_50 = nombre
        categoria_menor_edad_mas_50 = categoria
        bandera_min = True
        nombre_categoria_menos_edad_mas_50_puntos = f"{nombre_menos_edad_mas_50} {categoria_menor_edad_mas_50}"
    else:
        nombre_categoria_menos_edad_mas_50_puntos = "No hay jugador con esas caracteristicas"

    if tipo_saque == "cortado":
        cont_cortado += 1
    elif tipo_saque == "liftado":
        cont_liftado += 1
    else:
        cont_plano += 1

    if categoria == "experto":
        cont_experto += 1   
    elif categoria == "elite":
        cont_elite += 1
        if tipo_saque == "plano" and edad > 18 and edad < 26:
            cant_jug_eli_plan_18_25 += 1

    else:
        cont_avanzado += 1
        suma_edades_avanzados += edad
    
       
suma_contadores += cont_experto + cont_avanzado + cont_elite
porcentaje_experto = (cont_experto*100)/suma_contadores

if cont_avanzado > 0:
    promedio_jug_avanzados = suma_edades_avanzados/cont_avanzado
else:
     promedio_jug_avanzados = "No hay jugadores avanzados"
     
if cont_plano > cont_cortado and cont_plano > cont_liftado:
        saque_mas_usado = "Plano"
elif cont_cortado > cont_liftado:
    saque_mas_usado = "Cortado"
else:
    saque_mas_usado = "Liftado"

print(f"Cantidad de jugadores de la categoría elite con tipo de saque plano, cuya edad esté entre 19 y 25 años inclusive: {cant_jug_eli_plan_18_25} ")
print(f"Nombre y Categoría del jugador de menor edad con más de 50 puntos: {nombre_categoria_menos_edad_mas_50_puntos}")
print(f"Porcentaje de jugadores de categoría experto %{porcentaje_experto:.2f}")
print(f"El promedio de edad de los jugadores cuya categoría es “avanzado” es de: {promedio_jug_avanzados}")
print(f"El tipo de saque más usado por los jugadores, cuya categoría sea “elite” es: {saque_mas_usado}")


