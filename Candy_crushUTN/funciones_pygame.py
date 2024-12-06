from Funciones_profe_genericas import *
import random
import pygame

def genera_numero_aleatoriamente_en_un_rango(inicio:int,final:int):
    '''Retorna un numero aleatorio entre "Inicio" y "Final" inclusive'''
    return random.randint(inicio,final)

def agrega_numeros_aleatorios_a_lista(lista:list,cantidad:int):
    '''Recibe una lista y le agrega una cierta cantidad de numeros de forma aleatoria
    cantidad = Cantidad de veces que se le quieren agregar los numeros aleatorios'''
    for i in range(len(lista)):
        for j in range(cantidad):
            lista[i]["piezas"].append(genera_numero_aleatoriamente_en_un_rango(1,3))
    return lista



def verifica_en_vertical(lista:list,fila:int,columna:int,cant_en_ver):
    '''Recibe una matriz y una cantidad de veces que se quiere encontrar un valor dentro de esta matriz de forma vertical,
    el valor es la fila-columna de la matriz
    Lista = Matriz a evaluar
    fila = indice para la fila en la matriz
    columna = indice para la columna en la matriz
    cant_en_ver =  cantidad de veces que deberia aparecer el valor en vertical en la matriz para que retorne Verdadero'''
    retorno = False
    
    cont_total = 1 #Inicializo el contador en 1 para que cuando compare la fila con la siguiente o la anterior 
                    #fila no me cuente la posicion que ingreso el usuario
    
    for i in range(1,len(lista) - fila):#Cantidad de veces que tiene que recorrer hacia abajo
        if lista[fila][columna] == lista[fila + i][columna] and cant_en_ver != cont_total:#recorre hacia abajo
            cont_total += 1
        else: 
            break
    if cont_total == cant_en_ver:#Si el contador ya llego a la cantidad indicada corta
        retorno = True
    else:
        for i in range(1,fila + 1):#Cantidad de veces que tiene que recorrer hacia arriba
            if lista[fila][columna] == lista[fila - i][columna] and cant_en_ver != cont_total:#recorre hacia arriba
                cont_total += 1
                
            else: 
                break
        if cont_total == cant_en_ver:
            retorno = True
        
    return retorno
  

def pide_una_fila()->int:
    '''Pide una fila y verifica si existe dentro de una matriz'''
    fila = 0
    fila = input("Ingrese una fila: ")
    fila = verifica_si_es_numero(fila)
    fila = verifica_numero_dentro_de_rango(fila,1,4)
    return fila

def pide_una_columna()->int:
    '''Pide una columna y verifica si existe dentro de una matriz'''
    columna = 0
    columna = input("Ingrese una columna: ")
    columna = verifica_si_es_numero(columna)
    columna = verifica_numero_dentro_de_rango(columna,1,7)
    return columna

def generar_csv_cabecera(nombre_archivo:str,cabecera:list):
        ''''''
        try:                  
            with open(nombre_archivo, "r") as archivo:  #Si no hay error y puede leer el archivo no hace pasa                
                pass
        
        except FileNotFoundError:
            with open(nombre_archivo, "w") as archivo: #Si el archivo no se encuentra, lo crea
                archivo.write(",".join(cabecera))#Se le agrega al archivo la cabecera
                
        
def agregar_informacion_a_csv(nombre_archivo,lista:list):
    
        with open(nombre_archivo,"a") as archivo: 
            for i in range(len(lista)-1):
                archivo.write(f"\n{lista[i]},{lista[i+1]}")
            

def crear_lista_puntajes(nombre_archivo):
    puntaje = []
    with open(nombre_archivo,"r+") as archivo:
        puntaje.append(archivo.readlines())
    
    return puntaje   
            


def cargar_imagen_a_escala(nombre:str,escala:list):
    imagen = pygame.image.load(nombre)
    imagen = pygame.transform.scale(imagen,(escala))
    return imagen

def coordenada_a_indices(rect,x_inicio, y_inicio, ancho, alto):
    columna = (rect.x - x_inicio) // ancho
    fila = (rect.y - y_inicio) // alto
    return [fila, columna]

def poner_musica(nombre):
    pygame.mixer.init()
    pygame.mixer.music.load(nombre)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def actualizar_caramelos(pantalla,imagen_caramelo_1,imagen_caramelo_2,imagen_caramelo_3):
    caramelos_rects = []
    
    lista = [{"piezas": []}, {"piezas": []}, {"piezas": []}, {"piezas": []}]
    lista_numeros_aleatorios = crear_lista_valores(agrega_numeros_aleatorios_a_lista(lista, 7), "piezas")
    pos_fila = 25
    for i in range(len(lista_numeros_aleatorios)):
        pos_columna = 15
        for j in range(len(lista_numeros_aleatorios[i])):
                
                if lista_numeros_aleatorios[i][j] == 1:  

                    pantalla.blit(imagen_caramelo_1,(pos_columna,pos_fila))                      
                    rect = imagen_caramelo_1.get_rect()
                    rect.x = pos_columna
                    rect.y = pos_fila                                        
                    caramelos_rects.append([rect,1])      
                    
                elif lista_numeros_aleatorios[i][j] == 2:

                    pantalla.blit(imagen_caramelo_2,(pos_columna,pos_fila))                                                                            
                    rect = imagen_caramelo_2.get_rect()
                    rect.x = pos_columna
                    rect.y = pos_fila 
                    caramelos_rects.append([rect,2]) 

                elif lista_numeros_aleatorios[i][j] == 3:

                    pantalla.blit(imagen_caramelo_3,(pos_columna,pos_fila))                                                                             
                    rect = imagen_caramelo_3.get_rect()
                    rect.x = pos_columna
                    rect.y = pos_fila 
                    caramelos_rects.append([rect,3]) 

                pos_columna += 70                    
    
        pos_fila += 100

    return [caramelos_rects,lista_numeros_aleatorios]

