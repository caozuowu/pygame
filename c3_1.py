#-*- coding:utf-8 –*-
#!/user/bin/env python
# 全屏切换

background_image_filename = "sushiplate.jpg"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480),0, 32)
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((640, 480),pygame.FULLSCREEN,32)
            else:
                screen = pygame.display.set_mode((640, 480),0,32)
    screen.blit(background, (0,0))
    pygame.display.update()
