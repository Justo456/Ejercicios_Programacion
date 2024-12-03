'''Ejercicio 1: Dadas las siguientes listas:
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.'''
import GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_matrices as func
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

for i in range(len(Nombres) - 1):

    for j in range(i + 1,len(Nombres)):
        
        if Nombres[i] > Nombres[j]:

            aux_i = Nombres[i]

            Nombres[i] = Nombres[j] 

            Nombres[j] = aux_i

func.printear_listas(Nombres)
