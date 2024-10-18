import GitHub_Programacion.Paquetes.Paquete_funciones.Funciones_menu_de_opciones as func1

estanteria = [["to12",65],["to16",86],["to20",65],["to25",45],
              ["to30",68],["to35",73],["to40",85],["to45",89],
              ["ta4",58],["ta5",48],["ta6",64],["ta7",96],
              ["ta8",36],["ta10",72],["ta12",78],["ta14",71]]
opcion = 0
while opcion != 4:
    
    opcion = func1.menu_de_opciones_ferreteria()
    func1.menu_de_opciones_ferreteria_1(opcion,estanteria)
    func1.menu_de_opciones_ferreteria_2(opcion,estanteria)
    func1.menu_de_opciones_ferreteria_3(opcion,estanteria)