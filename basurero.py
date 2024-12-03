def recorre_abajo_vertical(lista:list,fila:int,columna:int):
    cont = 0
    for i in range(1,len(lista) - fila):
        if lista[fila][columna] == lista[fila + i][columna]:
            cont += 1
        else: 
            break
    return cont    


def recorre_arriba_vertical(lista:list,fila:int,columna:int):
    cont = 0
    for i in range(1,fila + 1):
        if lista[fila][columna] == lista[fila - i][columna]:
            cont += 1
        else: 
            break
    return cont  

def verifica_en_vertical(lista:list,fila:int,columna:int,cant_en_ver):
    '''Recibe una matriz y una cantidad de veces que se quiere encontrar un valor dentro de esta matriz de forma vertical,
    el valor es la fila-columna de la matriz
    Lista = Matriz a evaluar
    fila = indice para la fila en la matriz
    columna = indice para la columna en la matriz
    cant_en_ver =  cantidad de veces que deberia aparecer el valor en vertical en la matriz para que retorne Verdadero'''
    retorno = False
    fila -= 1
    columna -= 1
    cont_total = 1
      
    cont_total +=  recorre_abajo_vertical(lista,fila,columna)
    if cont_total >= cant_en_ver:
        retorno = True
    else:
        cont_total += recorre_arriba_vertical(lista,fila,columna)
    #Hacer un fusion de funciones arriba abajo, verificar (cont) para no recorrer innecesariamente
    if cont_total >= cant_en_ver:
        retorno = True
    
    
    return retorno
