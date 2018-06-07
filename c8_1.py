import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load("sushiplate.jpg").convert()
sprite = pygame.image.load("fugu.png")

x = 0.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    x += 10.

    if x > 640.:
        x = 0.

    pygame.display.update()