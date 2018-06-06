import pygame
from pygame import *
from random import *
from math import pi

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
center = [SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2]
radius = 5
angle = 0

def drawArc(surface, color, center, radius, a1, a2, ld):
    rect = (center[0] - radius, center[1] - radius, radius * 2, radius *2)
    pygame.draw.arc(surface, color, rect, a1, a2, ld)
    # pygame.draw.arc(screen, rc, (rect),angle, angle + pi/2, 3)
    pass
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            rc = (randint(0,255), randint(0,255), randint(0,255))
            drawArc(screen, rc, (center), radius, angle, angle + pi/2, 3)
            angle -= pi/2
            dr = 1.618 * radius - radius
            radius *= 1.618
            step = int((-angle*2/pi)%4)
            print(step)
            if step == 0:
                center[1] += dr
            elif step == 1:
                center[0] -= dr
            elif step == 2:
                center[1] -= dr
            elif step == 3:
                center[0] += dr

    pygame.display.update()