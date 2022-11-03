'''Iniciación a pygame.Enero 2021.
IFC Castelar TestLab'''
import os

import pygame, sys, random

from entities.LeonSprite import LeonSprite

pygame.init()
screen = pygame.display.set_mode( (800,600) )
pygame.display.set_caption("Pygame !!")
fspclock = pygame.time.Clock()

leon = LeonSprite(screen)
leon.centerx=400
leon.centery=300


def mostrar_mensaje(texto, tiempo):
    # self.font = pygame.font.SysFont("monospace", 60)
    font = pygame.font.Font(os.path.join("assets", "BAUHS93.TTF"), 60)

    # render text
    label = font.render(texto, True, (255, 255, 255))
    screen.blit(label, ((800/2 - (label.get_rect().width/2)), (600/2 - (label.get_rect().height/2))))
    pygame.display.update()
    pygame.time.wait(tiempo)


mostrar_mensaje("Hola World", 2000)
screen.fill("blue" )
mostrar_mensaje("Python 2021", 2000)

while True:
    screen.fill("black" )
    mostrar_mensaje("FIN",0)
    for event in pygame.event.get(): #Salir del programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fspclock.tick(30)

    pygame.display.flip() #flip funciona igual que update sin parámetros, refresancdo siempre la pantalla completa