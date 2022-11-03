'''Iniciación a pygame.Enero 2021.
IFC Castelar TestLab'''

import pygame, sys, random

from entities.LeonSprite import LeonSprite

pygame.init()
screen = pygame.display.set_mode( (800,600) )
pygame.display.set_caption("Pygame !!")
fspclock = pygame.time.Clock()

leon = LeonSprite(screen)
leon.centerx=400
leon.centery=300
#Este ejemplo es similar al anterior, pero cada fotograma limipamos la pantalla usando fill
while True:

    screen.fill("white" ) #Rellenamos la pantalla de blanco antes de dibujar
    #Prueba a bajar el número de framse por segundo para notar el efecto más (ahora mismo está a 30)

    for event in pygame.event.get(): #Salir del programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                leon.centery = leon.centery -1
            if event.key == pygame.K_DOWN:
                leon.centery = leon.centery + 1

    leon.update()
    leon.blit()
    fspclock.tick(30)

    pygame.display.flip() #flip funciona igual que update sin parámetros, refresancdo siempre la pantalla completa