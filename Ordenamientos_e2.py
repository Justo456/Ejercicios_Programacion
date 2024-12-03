'''Ejercicio 2: Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente.'''

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]


for i in range(len(Nombres)-1):
    for j in range(i+1,len(Nombres)):

        if Nombres[i] > Nombres[j]:
            aux_nom = Nombres[i]
            Nombres[i] = Nombres[j]
            Nombres[j] = aux_nom

            aux_puntos = Puntos[i]
            Puntos[i] = Puntos[j]
            Puntos[j] = aux_puntos


        elif Nombres[i] == Nombres[j]:
                if Puntos[i] < Puntos[j]:
                    aux_puntos = Puntos[i]
                    Puntos[i] = Puntos[j]
                    Puntos[j] = aux_puntos

for i in range (len(Nombres)):
     print(Nombres[i],Puntos[i])