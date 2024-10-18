def inicilizador_de_matriz(cantidad_de_filas:int,cantidad_de_columnas:int,valor_inicial:any)->list:
    matriz = []

    for i in range(cantidad_de_filas):

        filas = [valor_inicial] * cantidad_de_columnas

        matriz += [filas]

    return matriz

def cargar_matriz_secuencial(matriz:list):

    for i in range(len(matriz)):
        
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Ingrese un numero en la fila {i} columna {j}: "))
            
    return matriz

def cargar_matriz_aleatoriamente(matriz:list,filas:int,columnas:int):
    seguir = "s"
    while seguir == "s":

        fila = int(input("Indice de fila: "))
        while fila > filas or fila < 0:
            fila = int(input("*Fila fuera de rango. Indice de fila: "))

        columna = int(input("Indice de columna: "))
        while columna > columnas or columna < 0:
            columna = int(input("*Columna fuera de rango. Indice de columna: "))

        dato = input("Ingrese el dato a cargar: ")

        cantidad_dato = input("Ingrese la cantidad del dato: ")

        matriz[fila][columna] = f"|{dato} ({cantidad_dato})|"

        seguir = input("¿Desea seguir cargando datos? (s/n): ").lower()
        while seguir != "s" and seguir != "n":
            seguir = input("Error.¿Desea seguir cargando datos? (s/n): ").lower()


def alinea_filas(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")


def muestra_lista(lista:list)->str:
    mensaje_total = ""
    for i in range(len(lista)):
        mensaje = lista[i]
        mensaje_total += f"'{mensaje}' "

def continuar():
    seguir = input("¿Desea continuar? s/n: ").lower()
    while seguir != "s" and seguir!= "n":
        seguir = input("¿Error.Desea continuar? s/n: ").lower()
    return seguir

def printear_listas(lista:list):
    print("{:<15} {:<15} {:<15}".format("Productos","Cantidad","Posicion"))

    bandera_mensaje = 1
    for i in range(len(lista)):
        
        for j in range(len(lista[i])):
            
            if lista[i][j] != -1 :
                
                for k in range(len(lista[i][j])):

                    mensaje = lista[i][j][k]
                    mensaje = str(mensaje)
                    
                    if bandera_mensaje == 1:
                        producto = mensaje
                        bandera_mensaje += 1
                    elif bandera_mensaje == 2:
                        cantidad = mensaje
                        bandera_mensaje += 1
                    else:
                        posicion = mensaje
                        bandera_mensaje = 1
                    
    
                print("{:<20}{:<13}{:<10}" .format(producto,cantidad,posicion))

def verifica_dentro_de_rango(valor:int,desde:int,hasta:int)->int:
    '''Verifica si el valor ingresado esta dentro del rango establecido, si no, dara error hasta que se encuetre en el rango'''
    while valor < desde or valor > hasta:
        valor = int(input(f"Error.Valor fuera de rango, ingrese un valor entre {desde} y {hasta} inclusives: "))

    return valor
    

def verifica_nombre_dentro_de_lista(nombre:str,lista:list)->str:
    '''Verifica si el nombre introducido esta dentro de la lista'''
    bandera_nombre = False
    while bandera_nombre == False:
        for i in range(len(lista)):
            for j in range(len(lista[i])):    
                if nombre == lista[i][j]: 
                    bandera_nombre = True
        if bandera_nombre == False:
            nombre = input(f'''Error.Nombre ivalido, el nombre debe estar en {lista}\n 
                            Ingrese el nombre de nuevo: ''')
    
    return nombre

def printear_listas(lista:list):
    mensaje_total = ""
    for i in range(len(lista)):
        for j in range(len(lista)):
            mensaje = lista[i][j]
            mensaje = str(mensaje)
            mensaje_total += f"{mensaje}"
        print(mensaje_total)
        mensaje_total = ""
        
        
