import json
from data_stark import *

def leer_json(archivo_cargado:str,nombre_lista):
    retorno = False
    try:
        with open(archivo_cargado, "r") as archivo:
            datos = json.load(archivo)            
            retorno = datos[nombre_lista]
    
    except FileNotFoundError:        
        print("*El archivo no existe*")
       
    return retorno

def generar_csv(nombre:str,lista:list):
    info = ""
    if lista:
        with open(nombre,"w+") as archivo:
            for e_lista in lista:
                for i in range(len(e_lista)):     
                    info += f"{e_lista[i]},\n"
            
            archivo.write(info)
    else:
        return False
    
generar_csv("data_stark.csv",lista_personajes)







