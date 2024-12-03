'''3) Crear una función que reciba como parámetro una cadena y determine si la
misma es o no un palíndromo. Deberá retornar un valor booleano indicando
lo sucedido.'''

def es_palindromo(cadena:str)->bool:
    '''Retorna si la cadena de caracteres es un palindromo o no'''
    
    cadena = cadena.lower()

    palindromo = False

    if cadena == cadena[::-1]:
        palindromo = True
    
        
    
    return palindromo

cadena_de_carac = input("Ingrese una cadena de caracteres: ")

if es_palindromo(cadena_de_carac):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")