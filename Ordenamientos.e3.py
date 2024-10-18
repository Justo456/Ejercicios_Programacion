'''Ejercicio 3: Dadas las siguientes listas:
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera ascendente, si el nombre también es el mismo, debe ordenar por nota de manera descendente.
Ejercicio'''

Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ['Sosa','Gutierrez','Alsina','Martinez','Sosa','Ramirez','Perez','Lopez','Arregui','Mitre','Andrade','Loza','Antares','Roca','Perez']
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]


for i in range(len(Estudiantes)-1):
    for j in range(i+1,len(Estudiantes)):
        if Apellidos[i] > Apellidos[j]:
            aux_apellidos = Apellidos[i]
            Apellidos[i] = Apellidos[j]
            Apellidos[j] = aux_apellidos

            aux_Estudiantes = Estudiantes[i]
            Estudiantes[i] = Estudiantes[j]
            Estudiantes[j] = aux_Estudiantes

            aux_nota = Nota[i]
            Nota[i] = Nota[j]
            Nota[j] = aux_nota

        elif Apellidos[i] == Apellidos[j]:
            if Estudiantes[i] > Estudiantes[j]:
                aux_Estudiantes = Estudiantes[i]
                Estudiantes[i] = Estudiantes[j]
                Estudiantes[j] = aux_Estudiantes
            
            elif Estudiantes[i] == Estudiantes[j]:
                if Nota[i] < Nota[j]:
                    aux_nota = Nota[i]
                    Nota[i] = Nota[j]
                    Nota[j] = aux_nota

for i in range(len(Estudiantes)):
    print(Apellidos[i],"-",Estudiantes[i],"-",Nota[i])



        
