'''Iniciación a pygame.Enero 2021.
IFC Castelar TestLab'''

import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode( (800,600) )
pygame.display.set_caption("Pygame !!")
fspclock = pygame.time.Clock()

#Este ejemplo es similar al anterior, pero cada fotograma limipamos la pantalla usando fill
while True:

    screen.fill( (0,0,0) ) #Rellenamos la pantalla de negro antes de dibujar
    #Prueba a bajar el número de framse por segundo para notar el efecto más (ahora mismo está a 30)

    color = ( random.randint(0,255),random.randint(0,255),random.randint(0,255) )
    #La formula del rectángulo es similar a la del círculo
    pos = pygame.Rect(100,100,600,400) #Mediante Rect se indica su esquina superior izquierda y la inferior derecha
    pygame.draw.rect(screen, color, pos, 10) #el último valor es el grosor

    for event in pygame.event.get(): #Salir del programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fspclock.tick(30)
    pygame.display.update() #Refrescar la pantalla
