'''Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base, se pide el ingreso de una 
estación del año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) para vacacionar para poder 
calcular el precio final: -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un descuento del 10% Mar del Plata 
tiene un descuento del 20% -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene un aumento del 10% Mar del Plata 
tiene un aumento del 20% -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un aumento del 10% Mar del Plata 
tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
Validar el ingreso de datos.'''


base = 15000

estacion = input("Ingrese en la estacion del año que viajará (Verano-Otoño-Invierno-Primavera): ").lower()
while estacion != "verano" and estacion != "otoño" and estacion != "invierno" and estacion != "primavera":
    estacion = input("Error. Ingrese en la estacion del año que viajará (Verano-Otoño-Invierno-Primavera): ").lower()

localidad = input("Ingrese su destino (Bariloche-Cataratas-Mar del Plata-Córdoba): ").lower()
while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "córdoba":
    localidad = input("Error.Ingrese su destino (Bariloche-Cataratas-Mar del Plata-Córdoba): ").lower()


match estacion:
    case "invierno":
        if localidad == "bariloche":
            aumento_descuento = 1.2
        elif localidad == "mar del plata":
            aumento_descuento = 0.8
        else:
            aumento_descuento = 0.9
    case "verano":
        if localidad == "bariloche":
            aumento_descuento = 0.8
        elif localidad == "mar del plata":
            aumento_descuento = 1.2
        else:
            aumento_descuento = 1.1
    case "otoño" | "primavera":
        if localidad == "córdoba":
            aumento_descuento = 1
        else:
            aumento_descuento = 1.1
        
coste_total = base*aumento_descuento

print("El coste total es de: $"+str(coste_total))


