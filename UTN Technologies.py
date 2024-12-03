'''UTN Technologies, una reconocida software factory se encuentra en la búsqueda
de ideas para su próximo desarrollo en Python, que promete revolucionar el
mercado.
Las posibles aplicaciones son las siguientes:
● Inteligencia artificial (IA),
● Realidad virtual/aumentada (RV/RA),
● Internet de las cosas (IOT)
Para ello, la empresa realiza entre sus empleados una encuesta, con el
propósito de conocer ciertas métricas.
A) Los datos a ingresar por cada empleado encuestado son:
● nombre del empleado
● edad (no menor a 18)
● género (Masculino - Femenino - Otro)
● tecnologia (IA, RV/RA, IOT)
B) Cargar por terminal 10 encuestas.
C) Determinar:
1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive.
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40.
3. Nombre y tecnología que votó, de los empleados de género masculino con
mayor edad de ese género.'''

seguir = "si"
cont_encuesta = 1
cont_empleados = 0
cont_emp_masc_ia_iot_25_50 = 0
cont_emp_no_ia_no_femenino_33_40 = 0
edad_mayor = 0
while seguir == "si":
    print("Encuesta N° ", cont_encuesta)
    nombre = input("Ingrese su nombre: ").lower()

    edad = int(input("Ingrese su edad (no menor a 18): "))
    while edad < 18 or edad > 90:
        edad = int(input("Error.Ingrese su edad (no menor a 18): "))

    genero = input("Ingrese su genero (Masculino - Femenino - Otro): ").lower()
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("Error.Ingrese su genero (Masculino - Femenino - Otro): ").lower()

    tecnologia = input("Ingrese la tecnologia que utiliza (IA, RV/RA, IOT): ").lower()
    while tecnologia != "ia" and tecnologia != "rv" and tecnologia != "ra" and tecnologia != "iot":
        tecnologia = input("Error.Ingrese la tecnologia que utiliza (IA, RV/RA, IOT): ").lower()

    cont_encuesta += 1
    cont_empleados += 1

    seguir = input("¿Desea seguir? si/no: ").lower()
    while seguir != "si" and seguir != "no":
        seguir = input("Error.¿Desea seguir? si/no: ").lower()
    
    if cont_encuesta == 11:
        seguir = ""
    #1. Cantidad de empleados de género masculino que votaron por IOT o IA,
    #cuya edad esté entre 25 y 50 años inclusive.
    if genero == "masculino" and (tecnologia == "iot" or tecnologia == "ia") and  edad >= 25 and edad <= 50:
        cont_emp_masc_ia_iot_25_50 += 1
    #2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
    #género no sea Femenino o su edad se encuentre entre los 33 y 40.
    if tecnologia != "ia" and  (genero != "femenino" or (edad >= 33 and edad <= 40)):
        cont_emp_no_ia_no_femenino_33_40 += 1
    #3. Nombre y tecnología que votó, de los empleados de género masculino con
    #mayor edad de ese género.
    if genero == "masculino" and edad > edad_mayor:
        nombre_mayor = nombre
        edad_mayor = edad
        tecnologia_mayor = tecnologia
porcentaje = (cont_emp_no_ia_no_femenino_33_40*100)/cont_empleados
print(f"La cantidad de empleados de género masculino que votaron por IOT o IA,cuya edad esté entre 25 y 50 años inclusive: {cont_emp_masc_ia_iot_25_50}")
print(f"El Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: %{porcentaje:.2f}")   
print(f"Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género: {nombre_mayor},{tecnologia_mayor}")   


