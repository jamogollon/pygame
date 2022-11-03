'''Iniciación a pygame.Enero 2021.
IFC Castelar TestLab'''
import os

import pygame, sys, random

from entities.LeonSprite import LeonSprite

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame !!")
fspclock = pygame.time.Clock()

def gestionar_eventos(): #Usamos un método para que el bucle principal se vea más claro
    for event in pygame.event.get():  # Salir del programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Ratón pulsado")

        if event.type == pygame.MOUSEMOTION:
            leon.centerx, leon.centery = pygame.mouse.get_pos()

leon = LeonSprite(screen)
leon.centerx = 400
leon.centery = 300
leon.update()

pygame.mouse.set_pos((400,300) ) #Posicionamos el cursor en el centro de la pantalla
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR) #Cambiamos su apariencia
pygame.mouse.set_visible(True) #Podríamos ocultarlo
while True:
    screen.fill("dark green")
    gestionar_eventos()

    leon.update()  # Actualizamos la posición del león según el cambio del evento
    leon.blit()  # Dibujamos

    fspclock.tick(30)
    pygame.display.flip()  # flip funciona igual que update sin parámetros, refresancdo siempre la pantalla completa
