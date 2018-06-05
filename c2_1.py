#!/user/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    # 获得事件的名称
    event_text.append(str(event))
    # 保存一个屏幕的文字
    event_text = event_text[-SCREEN_SIZE[1]/font_height:]

    if event.type == pygame.QUIT:
        exit()
    
    screen.fill((255,255,255))
    y = SCREEN_SIZE[1] - font_height
    for text in reversed(event_text):
        # 写log
        screen.blit(font.render(text, True, (0,0,0)),(0,y))
        y -= font_height
    
    pygame.display.update()
