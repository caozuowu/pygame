import pygame
from pygame import *
from random import *
from math import pi

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
radius = 100
diameter = 100
angle = 0


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            rc = (randint(0,255), randint(0,255), randint(0,255))
            # rp = (randint(0,639), randint(0,479))
            # rs = (639-randint(rp[0], 639), 479-randint(rp[1], 479))
            # pygame.draw.rect(screen, rc, Rect(center, (radius,radius)))
            pygame.draw.arc(screen, rc, (center[0],center[1],radius,radius),angle, angle + pi/2, 3)
            # radius *= 1.618
            angle -= pi/2

    pygame.display.update()