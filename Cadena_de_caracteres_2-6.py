'''6) Crear una función para contar cuántas veces aparece una subcadena dentro
de una cadena.'''

def cuenta_subcadenas(cadena:str, sub_cadena:str) -> int:
    '''Cuenta cuntas veces aparece una subcadena dentro de una cadena.'''
    
    contador = 0
    longitud_subcadena = len(sub_cadena)
    
    for i in range(len(cadena) - longitud_subcadena + 1):
        if cadena[i:i + longitud_subcadena] == sub_cadena:
            contador += 1
            
    return contador

cadena_de_carac = input("Ingrese una cadena de caracteres: ")
sub_cadena = input("Ingrese la subcadena para saber la cantidad de veces que aparece en la cadena: ")
print(f"La cantidad de veces que aparece \"{sub_cadena}\" en \"{cadena_de_carac}\" es: {cuenta_subcadenas(cadena_de_carac,sub_cadena)}")