import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ancho = 1498
altura = 1024
 
# Crear la ventana
pantalla = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Juego de totito de Alan")

# Cargar imágenes
tablero_img = pygame.image.load("totito/tablero.jpg")
pato_img = pygame.image.load("totito/pato.png")
pinguino_img = pygame.image.load("totito/pinguino.png")
instrucciones_img = pygame.image.load("totito/instrucciones.png")

# Cambiar tamaño de imagenes
UpView1 = pygame.transform.scale_by(pinguino_img,0.43)
UpView2 = pygame.transform.scale_by(pato_img,1.1)

# Posición de la ficha 1🦆
pato_1izquierdo_x = 30
pato_1izquierdo_y = 55

pato_2izquierdo_x = 30
pato_2izquierdo_y = 380

pato_3izquierdo_x = 30
pato_3izquierdo_y = 725

#🦆🦆🦆🦆🦆🦆🦆🦆🦆

pato_1central_x = 360
pato_1central_y = 55

pato_2central_x = 360
pato_2central_y = 380

pato_3central_x = 360
pato_3central_y = 725

#🦆🦆🦆🦆🦆🦆🦆🦆🦆

pato_1derecho_x = 720
pato_1derecho_y = 55

pato_2derecho_x = 720
pato_2derecho_y = 380

pato_3derecho_x = 720
pato_3derecho_y = 725

# Posición del pinguino
pinguino_x = 345
pinguino_y = 345

# Velocidad del pinguino
pinguino_speed = 3

#Musica
Musica = pygame.mixer.music.load("totito/putin.mp3")
pygame.mixer.music.play(-1)

#Variables de false y true para colocar los muñecos en sus cuadros con el teclado
p_izquierdo1=False
p_izquierdo2=False
p_izquierdo3=False

p_central1=False
p_central2=False
p_central3=False

p_derecho1=False
p_derecho2=False
p_derecho3=False

# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Colocar imagenes de fondo
    pantalla.blit(tablero_img, (0, 0)) #tablero de totito
    pantalla.blit(instrucciones_img, (1022, 5)) #letrero de instrucciones

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
      
    # poner muñecos en la pantalla    

    pantalla.blit(UpView1, (pinguino_x, pinguino_y))

    #poner pato en lugar izquierdo 1
    if keys[pygame.K_q]:
        p_izquierdo1=True
    if p_izquierdo1:
        pantalla.blit(UpView2, (pato_1izquierdo_x, pato_1izquierdo_y))

    #poner pato en lugar izquierdo 2
    if keys[pygame.K_a]:
        p_izquierdo2=True
    if p_izquierdo2:
        pantalla.blit(UpView2, (pato_2izquierdo_x, pato_2izquierdo_y))

    #poner pato en lugar izquierdo 3
    if keys[pygame.K_z]:
        p_izquierdo3=True
    if p_izquierdo3:
        pantalla.blit(UpView2, (pato_3izquierdo_x, pato_3izquierdo_y))

#🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆

    #poner pato en lugar central 1
    if keys[pygame.K_w]:
        p_central1=True
    if p_central1:
        pantalla.blit(UpView2, (pato_1central_x, pato_1central_y))

    #poner pato en lugar central 2
    if keys[pygame.K_s]:
        p_central2=True
    if p_central2:
        pantalla.blit(UpView2, (pato_2central_x, pato_2central_y))

    #poner pato en lugar central 3
    if keys[pygame.K_x]:
        p_central3=True
    if p_central3:
        pantalla.blit(UpView2, (pato_3central_x, pato_3central_y))

#🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆🦆

    #poner pato en lugar derecho 1
    if keys[pygame.K_e]:
        p_derecho1=True
    if p_derecho1:
        pantalla.blit(UpView2, (pato_1derecho_x, pato_1derecho_y))

    #poner pato en lugar derecho 2
    if keys[pygame.K_d]:
        p_derecho2=True
    if p_derecho2:
        pantalla.blit(UpView2, (pato_2derecho_x, pato_2derecho_y))

    #poner pato en lugar derecho 3
    if keys[pygame.K_c]:
        p_derecho3=True
    if p_derecho3:
        pantalla.blit(UpView2, (pato_3derecho_x, pato_3derecho_y))

        # Actualizar la ventana
    pygame.display.update() 