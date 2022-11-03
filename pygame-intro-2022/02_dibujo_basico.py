'''Iniciación a pygame.Enero 2021.
IFC Castelar TestLab'''

#Para que el siguiente import funcione debemos instalar la biblioteca pygame
import pygame, sys, random

# Este es el modelo más sencillo de una aplicación pygame
pygame.init()
screen = pygame.display.set_mode( (800,600) ) #Tamaño de pantalla, expresado com una tupla
pygame.display.set_caption("Pygame !!") #Título de la ventana
fspclock = pygame.time.Clock() #Reloj de la aplicación

while True: #Bucle infito del juego

    # Dibujamos círculos con un color RGB aleatorio y con una posicion aleatoria
    #Un círculo en cada paso por el bucle, esto es 30 círculos por segundo
    color = ( random.randint(0,255),random.randint(0,255),random.randint(0,255) ) #tupla de 3 valores (R,G,B)
    pos = (random.randint(0,800),random.randint(0,600)) #tupla de dos valores (x,y)
    pygame.draw.circle(screen, color, pos, 30)

    #Dentro del bucle infinito controlamos los eventos para que el programa pueda salir
    for event in pygame.event.get(): #Salir del programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fspclock.tick(30) #Indicamos que la pantalla se va a refrescar 30 veces por segundo
    pygame.display.update() #Refrescar la pantalla
