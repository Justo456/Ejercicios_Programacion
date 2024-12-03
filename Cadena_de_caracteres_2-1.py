'''Crear una función que reciba como parámetro una cadena y determine la
cantidad de vocales que hay de cada una (individualmente). La función
retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
la cantidad.'''

def cuenta_vocales(cadena:str)-> list:
    '''Cuenta las vocales de una cadena de caracateres'''
    lista_de_vocales = [["a",0],["e",0],["i",0],["o",0],["u",0]]

    for e_cadena in cadena:
        if e_cadena == "a":
            lista_de_vocales[0][1] += 1
        elif e_cadena == "e":
            lista_de_vocales[1][1] += 1
        elif e_cadena == "i":
            lista_de_vocales[2][1] += 1
        elif e_cadena == "o":
            lista_de_vocales[3][1] += 1
        elif e_cadena == "u":
            lista_de_vocales[4][1] += 1


          
    return lista_de_vocales


cadena_de_carac = input("Ingrese una cadena de caracteres: ")
mensaje_total = ""
ret = cuenta_vocales(cadena_de_carac)
for i in range(len(ret)):
    print(ret[i])