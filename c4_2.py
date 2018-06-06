# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
# help(pygame)
screen = pygame.display.set_mode((640, 480) ,0, 32)
# 系统字体
# my_font = pygame.font.SysFont("arial", 64)
# ttf文件
font = pygame.font.Font("Arial Unicode.ttf", 40)
# font = pygame.font.SysFont("SimHei", 64)
text_surface = font.render(u"你好", True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height())/2 

background = pygame.image.load("sushiplate.jpg").convert()

while True:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0,0))
    x -= 2
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()
    screen.blit(text_surface, (x,y))
    pygame.display.update()