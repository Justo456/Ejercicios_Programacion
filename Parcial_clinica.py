import GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_matrices as func
from Ejercicos.Todos_los_ejercicios.GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_ejemplo_parcial_Clinica import *

opcion = menu_de_opciones()
while opcion != 9:
    opcion = int(input('''     
                        1-Cargar pacientes
                        2-Mostrar la lista de pacientes
                        3-Buscar pacientes por numero de Historia Clinica
                        4-Ordenar pacientes por numero de Historia Clinica
                        5-Mostrar paciente cin mas dias de internacion
                        6-Mostrar paciene con menos dias de internacion
                        7-Cantidad de pacientes con ams de 5 dias de internacion
                        8-Promedio de dias de internacion de todos los pacientes
                        9-Salir
                        Ingrese un opcion: 
                            '''))
    if opcion == 2:
        matriz = menu_de_opciones_clinica_1()

    print(matriz)
    menu_de_opciones_clinica_2(opcion,matriz)


            
                 

