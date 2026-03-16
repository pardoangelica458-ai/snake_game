from gettext import install
import pip
import pygame # type: ignore
import random
# Inicializar pygame
pygame.init()
# Tamaño de la ventana
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente")
# Colores
negro = (0,0,0)
verde = (0,255,0)
rojo = (255,0,0)
# Tamaño de bloque
bloque = 10
# Velocidad del juego
reloj = pygame.time.Clock()
# Posición inicial
x = ancho / 2
y = alto / 2
x_cambio = 0
y_cambio = 0
comida_x = random.randrange(0, ancho, bloque)
comida_y = random.randrange(0, alto, bloque)
correr = True
while correr:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x_cambio = -bloque
                y_cambio = 0
            elif evento.key == pygame.K_RIGHT:
                x_cambio = bloque
                y_cambio = 0
            elif evento.key == pygame.K_UP:
                y_cambio = -bloque
                x_cambio = 0
            elif evento.key == pygame.K_DOWN:
                y_cambio = bloque
                x_cambio = 0
    x += x_cambio
    y += y_cambio
    pantalla.fill(negro)
    pygame.draw.rect(pantalla, rojo, [comida_x, comida_y, bloque, bloque])
    pygame.draw.rect(pantalla, verde, [x, y, bloque, bloque])
    pygame.display.update()
    reloj.tick(15)
pygame.quit()