import pygame
from colores import * 

from funciones_pygame import * 
lista = [
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]},
 {"piezas":[]}
 ]
pygame.init()
segundos = "11"
fin_tiempo = False
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)


poner_musica("Bakermat - Baianá (Official Video).mp3")
cabecera = ["Nombre","Puntos"]
escala_pantalla = [700,500]
escala_caramelos = [50,50]
posicion_del_timer = [350,400]
posicion_imagen = [0,0] 
posicion_scoreboard = [230,100]
lista_numeros_aleatorios = crear_lista_valores(agrega_numeros_aleatorios_a_lista(lista,7),"piezas")
pantalla = pygame.display.set_mode(escala_pantalla)
ancho_botones = [200,100]
puntaje = []
lista_puntajes = []

pygame.display.set_caption("Candy Crush UTN")

imagen = cargar_imagen_a_escala("Fondo_Candy.jpg",escala_pantalla)
fondo_transparente = cargar_imagen_a_escala("fondo_transparente.jpg",[500,400])
imagen_caramelo_1 = cargar_imagen_a_escala("Flynn_paaff.png",escala_caramelos)
imagen_caramelo_2 =cargar_imagen_a_escala("Felford.png",escala_caramelos)
imagen_caramelo_3 =cargar_imagen_a_escala("sugus.webp",escala_caramelos)
imagen_inicio = cargar_imagen_a_escala("Inicio_Candy.png",escala_pantalla)
imagen_jugar = cargar_imagen_a_escala("Jugar.png",ancho_botones)
imagen_ver_score = cargar_imagen_a_escala("Ver_score.png",ancho_botones)
imagen_nombre = cargar_imagen_a_escala("nombre.png",[200,50])
imagen_listo = cargar_imagen_a_escala("listo.png",[200,50])
imagen_scoreboard = cargar_imagen_a_escala("Scoreboard.png",[300,380])
puntos = 0
iniciado = True
ingresar_nombre = True
jugando = False
inicio_mostrado = False
mostrar_inicio = False
game_over = False
ver_score = False


#Rect nombre de usuario y fuente
fuente_scoreboard = pygame.font.SysFont("Arial", 30)
fuente_nombre = pygame.font.SysFont("Arial", 30)
fuente = pygame.font.SysFont("Arial", 80)
##########
nombre = ""
###########
rect_nombre = imagen_nombre.get_rect()
rect_nombre.x = 250
rect_nombre.y = 320
#Rect de Listo
rect_listo = imagen_listo.get_rect()
rect_listo.x = 480
rect_listo.y = 320
#Indico donde va a estar mi Rect en base al tamaño de mi imagen y le doy las coordenadas
rect_jugar = imagen_jugar.get_rect()
rect_jugar.x = 1000
rect_jugar.y = 1000

rect_ver_score = imagen_ver_score.get_rect()          
rect_ver_score.x = 1000
rect_ver_score.y = 1000



caramelos_rects = []

while iniciado:
    for evento in pygame.event.get():
         
        if evento.type == pygame.QUIT:
            iniciado = False
        if game_over == True:
            iniciado = False
        if ingresar_nombre:
            
            pantalla.blit(imagen_inicio,(posicion_imagen))
            pantalla.blit(imagen_nombre,(rect_nombre.x,rect_nombre.y))
            pantalla.blit(imagen_listo,(rect_listo.x,rect_listo.y))
       
            if evento.type == pygame.KEYDOWN:
                
                    if evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[0:-1]
                    elif len(nombre) <= 12:                   
                            nombre += evento.unicode
                        
            fuente_nombre_surface = fuente_nombre.render(nombre, True, BLACK) 
            pantalla.blit(fuente_nombre_surface, (rect_nombre.x+10, rect_nombre.y+10))
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
                
                if rect_listo.collidepoint(evento.pos):           
                    ingresar_nombre = False
                    mostrar_inicio = True
                    
                    
        if mostrar_inicio: 
            pantalla.blit(imagen_inicio,(posicion_imagen))
            pantalla.blit(imagen_jugar,(250,270))
            pantalla.blit(imagen_ver_score,(250,380))
            puntaje = generar_csv_cabecera("scoreboard.csv",cabecera)
                       
            rect_jugar.x = 250
            rect_jugar.y = 270                   
            rect_ver_score.x = 250
            rect_ver_score.y = 380
            inicio_mostrado = True
        tabla_de_jugadores = [nombre,puntos] 
        if evento.type == pygame.MOUSEBUTTONDOWN and inicio_mostrado:
            if rect_jugar.collidepoint(evento.pos) and inicio_mostrado:               
                segundos = "10"
                jugando = True
                mostrar_inicio = False
                rect_jugar.x = 1000
                rect_jugar.y = 1000 
                pantalla.blit(imagen,(posicion_imagen))
                pantalla.blit(fondo_transparente,(posicion_imagen))
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
                
            
            elif rect_ver_score.collidepoint(evento.pos) and inicio_mostrado:
                
                ver_score = True
                mostrar_inicio = False
                pantalla.blit(imagen,(posicion_imagen))
                pantalla.blit(imagen_scoreboard,(posicion_scoreboard))
                agregar = True
            

        if evento.type == timer_segundos and jugando:
                segundos_texto = fuente.render(str(segundos), True, COLOR_BLANCO )
                pantalla.fill(BLACK, (posicion_del_timer[0], posicion_del_timer[1], 400, 80))
                pantalla.blit(segundos_texto, posicion_del_timer) 
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    if int(segundos) <= 0:
                        fin_tiempo = True
                        segundos = "Game Over"
                        game_over = True
                                               
                

        if evento.type == pygame.MOUSEBUTTONDOWN:              
            for e_caramelos in caramelos_rects:

                rect = e_caramelos[0]
                
                if rect.collidepoint(evento.pos):                                             
                    indices_de_matriz = coordenada_a_indices(rect,15,25,70,100)
                    if verifica_en_vertical(lista_numeros_aleatorios,indices_de_matriz[0],indices_de_matriz[1],3):
                        print("HA GANADO 10 PUNTOS")
                        puntos += 10

                    else:
                        if segundos != "Game Over" and int(segundos) > 1:
                            segundos = int(segundos) - 1
                        puntos -= 1
                        print("SEGUI PARTICIPANDO")
                        lista_caramelos_y_nums = actualizar_caramelos(pantalla,imagen_caramelo_1,imagen_caramelo_2,imagen_caramelo_3)
                        caramelos_rects = lista_caramelos_y_nums[0]
                        lista_numeros_aleatorios = lista_caramelos_y_nums[1]
                        
        
                
        espacio_y = 30
        espacio_x = 110
        if ver_score:
            
            lista_puntajes = crear_lista_puntajes("scoreboard.csv")
                       
            for e_puntaje in lista_puntajes:
                for i in range(len(e_puntaje)):
                    print(e_puntaje)
                    nombre_puntos = e_puntaje[i].split(",")
                    pantalla.blit(fuente_scoreboard.render(f"{nombre_puntos[0]}", True, BLACK),(posicion_scoreboard[0],posicion_scoreboard[1] + espacio_y) )
                    
                    pantalla.blit(fuente_scoreboard.render(f"{nombre_puntos[1]}", True, BLACK),(posicion_scoreboard[0]+espacio_x,posicion_scoreboard[1] + espacio_y) )           
                    espacio_y += 30
                    
            ver_score = False

    pygame.display.flip()

pygame.quit() 

agregar_informacion_a_csv("scoreboard.csv",tabla_de_jugadores)   