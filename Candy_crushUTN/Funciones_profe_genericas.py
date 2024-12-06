def ordenar(lista:list, clave:str, orden:int):
    '''Ordenar una lista de diccionaro por la clave solicitada con el criterio de ordenamiento pasado por parametro
    Lista: es la lista a ordenar
    Clave: key del diccionario por la cual voy a ordenar
    Orden: 1 = ascendente   -1 = descendente
    '''

    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if orden == 1:
                if lista[i][clave] > lista[j][clave]:
                    intercambiar(lista, i, j)
            
            if orden == -1:
                if lista[i][clave] < lista[j][clave]:
                    intercambiar(lista, i, j)
            

def intercambiar(lista:list,posicion1:int,posicion2:int):
    '''Intercambiar posciones'''
    aux = lista[posicion1]
    lista[posicion1] = lista[posicion2]
    lista[posicion2] = aux

def verifica_numero_dentro_de_rango(valor:int,desde:int,hasta:int)->int:
    '''Verifica si el valor ingresado esta dentro del rango establecido, si no, dara error hasta que se encuetre en el rango'''
    
    
    while valor < desde or valor > hasta:
        valor = int(input(f"Error.Valor fuera de rango, ingrese un valor entre {desde} y {hasta} inclusives: "))

    return valor

def verifica_si_es_numero(numero)->int:
    numero = str(numero)
    while not numero.isdigit():
        numero = input("Error.*No es un digito* Ingrese una numero: ")
    numero = int(numero)  
    return numero

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

def min_max(lista:list,comparador:int):
    '''Lista: ingresar la lista a recorrer para hallar el menor o mayor
        Comparador: -1 = mayor  1 = menor'''
    for j in range(len(lista)):
        lista[j] = int(lista[j])

    retorno = None
    mayor = lista[0]
    menor = lista[0]
    for i in range(len(lista)):

        if comparador == -1 and mayor <= lista[i]:
            mayor = lista[i]
            retorno = mayor
    
        if comparador == 1 and menor >= lista[i]:
            menor = lista[i]
            retorno = menor
            
                               
                                                                              
    return retorno 

def crear_lista_valores(lista:list,clave:str):
    '''Crea una lista con los valores de las claves de un diccionario
    Lista = lista que contiene los diccionarios
    Clave = Clave que queremos guadar en una lista nueva'''
    nueva_lista = []
    for i in range(len(lista)):
        nueva_lista.append(lista[i][clave])
    
    return nueva_lista

def compara_clave_igual_xvalor(lista:list,clave:str,valor:str):#no es tan generica, porq en la misma funcion se le aplica un filtro, ademas si el valor no es str no se puede usar
    '''Recorre una lista con diccionarios y si la clave ingresada por parametro tiene un valor igual al valor ingresado por parametro
    entonces guarda ese diccionario en una nueva lista
    Lista = lista que contiene los diccionarios
    Clave = Clave que contiene el valor que queremos comparar
    Valor = Valor por el cual queremos filtrar para crear una nueva lista
    '''
    lista_claves = [] 
    
    for i in range(len(lista)):
           
        if lista[i][clave] == valor:
            lista_claves.append(lista[i])
            
    
    return lista_claves


def mostrar_uno(lista:list,p_1:str|None,p_2:str|None,p_3:str|None,p_4:str|None,p_5:int|None,p_6:str|None,p_7:str|None,p_8:str|None,posicion:int):
    '''Muestra los indices de un lista.
    ''' 

    if p_1 != None:
        print({lista[posicion][p_1]})
    if p_2 != None:
        print({lista[posicion][p_2]})
    if p_3 != None:
        print({lista[posicion][p_3]})
    if p_4 != None:
        print({lista[posicion][p_4]})
    if p_5 != None:
        print({lista[posicion][p_5]})
    if p_6 != None:
        print({lista[posicion][p_6]})
    if p_7!= None:
        print({lista[posicion][p_7]})
    if p_8 != None:
        print({lista[posicion][p_8]})



def cuenta_elementos_iguales(lista:list,elemento):
    '''Cuenta cuantos elementos iguales hay en una lista y retorna la cantidad que contó'''
    cont = 0
    for i in range(len(lista)):
        if elemento == lista[i]:
                cont += 1

    return cont


def elimina_elementos_repetidos(lista:list):
    '''Elimina elementos repetidos, y retorna la lista limpia'''
    lista_nueva = []
    for i in range(len(lista)-1):
        
        for j in range(i+1,len(lista)):
            if lista[i] == lista[j]:
                            
                lista[j] = ""
    
    for k in range(len(lista)):
        if lista[k] != "":
            lista_nueva.append(lista[k])
                
    
    return lista_nueva

def invocar_tabla(diccionario:dict):
    '''Invoca un tabla con todas las claves que poseea un diccionario'''
    lista = "  |  ".join(list(diccionario.keys()))  
    print(lista)
    

def mostrar_informacion_en_tabla(diccionario:dict):
    '''Muestra los valores que posee un diccionario en forma de tabla'''
    lista = "|".join(list(diccionario.values()))
    print(lista)

def mostrar_todos(lista:list):
    '''Muestra todos los elementos de una lista separados'''   
    for i in range(len(lista)):
        mostrar_informacion_en_tabla(lista[i])
             
        
def mostrar_uno(lista:list,posicion:int):
    '''Muestra un elemento de una lista'''
    mostrar_informacion_en_tabla(lista[posicion])


def promediar_valores_dic(lista:list)->int:
    '''Promedia todos los valores dentro de una lista'''
    acumulador = 0

    for i in range(len(lista)):
        if str(lista[i]).isdigit():
            acumulador += int(lista[i])
        
    promedio = (acumulador/len(lista))

    return promedio