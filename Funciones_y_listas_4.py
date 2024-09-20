'''Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números y un número especificado. 
La misma debe buscar el número especificado en la lista y retornar “True” si existe.'''

def busca_numero_en_lista(lista_numeros:list,numero_espec:int):

    resultado = False
    for i in range(len(lista_numeros)):
        if lista_numeros[i] == numero_espec:
            resultado = True
            mensaje = "Existe ese numero en la lista"
             
    if resultado == False:
        mensaje = "No existe ese numero en la lista"

    return mensaje


lista_de_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numero_especifico = int(input("Ingrese el numero que desear buscar en  la lista: "))
ret = busca_numero_en_lista(lista_de_numeros,numero_especifico)
print(ret)