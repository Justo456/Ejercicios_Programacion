import GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_matrices as func
import GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_menu_de_opciones as func1
#1
print("Producto|cantidad|posicion")
lista_de_productos = func.inicilizador_de_matriz(3,5,-1)
lista_de_productos[0][1] = ["Botellas",3,[1,2]]
lista_de_productos[0][3] = ["Frascos",8,[1,4]]
lista_de_productos[1][2] = ["Fideos",4,[2,3]]
lista_de_productos[2][3] = ["Leche",6,[3,4]]

#2
opcion = 0
bandera_opcion_1 = False
while opcion != 6:
    
    opcion = func1.menu_de_opciones_almacen()
    func1.menu_de_opciones_1_almacen(opcion,lista_de_productos) 
    if opcion == 1:
        bandera_opcion_1 = True
    
    func1.menu_de_opciones_2_almacen(bandera_opcion_1,opcion,lista_de_productos)
    func1.menu_de_opciones_3_almacen(bandera_opcion_1,opcion,lista_de_productos)
    func1.menu_de_opciones_4_almacen(opcion,lista_de_productos)
    
    
    



