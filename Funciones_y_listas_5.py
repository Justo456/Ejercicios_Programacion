'''Ejercicio 5: Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las personas de menor edad (puede ser más de una) y las retorne. 
El programa principal deberá mostrar nombre y edad de los menores.'''

def muestra_las_edades_menores(nombre:list,edad:list)->str:
    edad_menor = 0
    
    mensaje = ""
    mensaje_total = ""
    edad_promedio = 0
    suma_edades = 0
    for i in range(len(edad)):
        suma_edades += edad[i]
        if i == len(edad) - 1:       
            edad_promedio = suma_edades/len(edad)
            
    
    for i in range(len(edad)):
        
        if edad[i] <= edad_promedio:
            edad_menor = edad[i]
            nombre_menor = nombre[i]
            mensaje = f"{nombre_menor} y su edad es {edad_menor}, "
            mensaje_total += mensaje

    return mensaje_total
        

Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

ret = muestra_las_edades_menores(Nombres,edades)
print(f"Los nombres con menor edad son : ",ret)

