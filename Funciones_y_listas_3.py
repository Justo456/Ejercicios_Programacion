'''Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango especificado, validar los números solicitados dentro de ese 
rango, guardar en una lista y retornarla. El programa principal debe invocar a la función y mostrar por pantalla el retorno.'''

def pedir_numero()->list:
    cont_numeros = 1
    lista_numeros = []
    while cont_numeros < 11:
        numeros = int(input(f"Ingrese 10 numeros entre el (15) y el (55) inclusives, N°{cont_numeros}: "))        
        while numeros < 15 or numeros > 55:
            numeros = int(input("Error.Ingrese 10 numeros entre el (15) y el (55) inculsives: "))
        cont_numeros += 1
        
        lista_numeros.append(numeros)
        print(lista_numeros)
    
    return lista_numeros

ret = pedir_numero()
mensaje_total = ""
for i in range(len(ret)):
    mensaje = ret[i]
    mensaje_total += f"'{mensaje}' "

print(f"Su lista es: {mensaje_total}")