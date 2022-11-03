'''Iniciación a pygame.Enero 2021.
IFC Castelar TestLab'''
import os

import pygame, sys, random

from entities.LeonSprite import LeonSprite

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame !!")
fspclock = pygame.time.Clock()

def mostrar_mensaje(texto, size, tiempo):
    # self.font = pygame.font.SysFont("monospace", 60)
    font = pygame.font.Font(os.path.join("assets", "BAUHS93.TTF"), size)

    # render text
    label = font.render(texto, True, (255, 255, 255))
    screen.blit(label, ((800 / 2 - (label.get_rect().width / 2)), (600 / 2 - (label.get_rect().height / 2))))
    pygame.display.update()
    pygame.time.wait(tiempo)

def gestionar_eventos(): #Usamos un método para que el bucle principal se vea más claro
    for event in pygame.event.get():  # Salir del programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            contador = contador + 1
            size = size + 1


contador = 0
size = 60

while True:
    screen.fill("black")
    mostrar_mensaje(str(contador), size, 0)
    fspclock.tick(30)
    pygame.display.update()
