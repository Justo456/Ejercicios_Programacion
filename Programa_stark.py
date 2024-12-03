from copy import deepcopy
from data_stark import lista_personajes
lista_personajes_copia = deepcopy(lista_personajes) 
from menu_opciones_stark import *

menu_de_opciones_stark(lista_personajes_copia)