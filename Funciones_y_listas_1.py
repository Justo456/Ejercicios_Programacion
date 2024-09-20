'''Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.'''

def pide_nombres(lista:list)->list:
    'Pide nombres y te los muestra de manera secuencial'
    cont_nombres = 0
    while cont_nombres < 10:
        cont_nombres += 1
        nombres = input(f"Ingrese 10 nombres (Nombre N° {cont_nombres}): ")  
        
        lista.append(nombres)

    return lista
        
        
mensaje_total = ""       
lista_nombre = []
ret = pide_nombres(lista_nombre)
for i in range(len(ret)):
    mensaje = lista_nombre[i]
    mensaje_total += f"'{mensaje}' "

print(f"Los nombres de la lista son: {mensaje_total}")




        

        
        