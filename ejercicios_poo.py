# '''Ejemplo: Clase simple
# Crear una clase Persona que tenga las características nombre y edad. La persona debe poder
# mostrar un mensaje saludando presentándose con su nombre y edad. Se debe crear la clase e
# implementarla.'''

# class Persona:
#     def __init__(self,nombre:str,edad:int) -> None:
#         self.nombre:str = nombre
#         self.edad:int = edad
        
    
#     def MostarPersona(self):
#         print(f"Nombre: {self.nombre}")
#         print(f"Edad: {self.edad}")

# persona_1 = Persona("Justo","21")
# persona_1.MostarPersona()




# '''Ejemplo: Clase para representar un Libro
# Crear una clase Libro que tenga las características títuto, autor y año de publicación. Del libro se 
# debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase 
# e implementarla.'''

# class Libro:
#     def __init__(self,titulo:str,autor:str,año_de_publicacion:int) -> None:
#         self.__titulo:str = titulo
#         self.__autor:int = autor
#         self.__año:int = año_de_publicacion
        
#     def mostrar_informacion(self):
#         print("Titulos del libro: ", self.__titulo)
#         print("Autor del libro: ", self.__autor)
#         print("Años de pulbicacion del libro: ", self.__año)

# libro = Libro("Deadpool","Stan Lee",1990)

# libro.mostrar_informacion()


# '''Ejemplo: Clase para representar un Rectángulo
# Crear una clase rectángulo que tenga las características base y altura. Del rectángulo se debe
# poder calcular el área y el perímetro. Se debe crear la clase e implementarla.'''

# class Rectangulo:
#     def __init__(self,base:int,altura:int) -> None:
#         self.__base:int = base
#         self.__altura:int = altura

#     def calcular_area_y_perimetro(self):
#         print(f"Perimetro: {self.__base*self.__altura}")
#         print(f"Área: {2*(self.__base+self.__altura)}")

# base = int(input("Ingrese una base: "))
# altura = int(input("Ingrese una altura: "))

# rectangulo = Rectangulo(base,altura)
# rectangulo.calcular_area_y_perimetro()


# '''Ejemplo: Herencia de clases
# Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de Animal
# las características y realice el sonido “guau guau”. La clase Gato que herede de Animal las
# características y realice el sonido “Miau”. Del gato y el perro se debe poder mostrar el sonido que
# realizan. Se debe crear la clase e implementarla.'''


# class Animal:
#     def __init__(self,nombre:str) -> None:
#         self.nombre = nombre
    
#     def mostrar_animal(self):
#         print(f"{self.nombre} hace {self._sonido}")

# class Perro(Animal):
#     def __init__(self, nombre: str) -> None:
#         super().__init__(nombre)
#         self._sonido = "guau guau"
#         self.mostrar_animal()

# class Gato(Animal):
#     def __init__(self, nombre: str) -> None:
#         super().__init__(nombre)
#         self._sonido = "Miau"
#         self.mostrar_animal()

# perro = Perro("Moro")
# gato = Gato("Michi")


# '''Ejemplo: Encapsulamiento
# Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado. De la
# cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue
# exitoso). Se debe crear la clase e implementarla.'''

# class CuentaBancaria:
#     def __init__(self,titular:str,saldo_encapsulado:int) -> None:
#         self._titular = titular
#         self._saldo_encapsulado = saldo_encapsulado
    
#     def mostrar_depositar_retirar_saldo(self):
#         opcion = ""
#         while opcion != "s":

#             opcion = input('''¿Que desea hacer con su saldo?: 
#                             M-Mostrar
#                             R-Retirar
#                             D-Deposita
#                             S-Salir

#                         ''').lower()
#             while opcion != "m" and opcion != "r" and opcion != "d" and opcion != "s":
#                 opcion = input('''*Opcion invalida*
#                             ¿Que desea hacer con su saldo?: 
#                             M-Mostrar
#                             R-Retirar
#                             D-Depositar
#                             S-Salir
                            
#                         ''').lower()
#             if opcion == "m":
#                 print(f"'{self._titular}', su saldo es {self._saldo_encapsulado}")
#                 print("*Opcion realizada de forma exitosa*")

#             elif opcion == "r":
#                 retiro = int(input("¿Cuanto desear retirar?: "))
#                 if retiro > self._saldo_encapsulado:
#                     print("No se puede retirar ese monto porque no hay suficiente dinero en la cuenta")
#                 else:
#                     nuevo_saldo = (self._saldo_encapsulado - retiro)
#                     self._saldo_encapsulado = nuevo_saldo
#                     print("*Opcion realizada de forma exitosa*")
            
#             elif opcion == "d":

#                 deposito = int(input("¿Cuanto desear depositar?: "))
#                 nuevo_saldo = (self._saldo_encapsulado + deposito)
#                 self._saldo_encapsulado = nuevo_saldo
#                 print("*Opcion realizada de forma exitosa*")


# banco = CuentaBancaria("Justo",100000)
# banco.mostrar_depositar_retirar_saldo()





