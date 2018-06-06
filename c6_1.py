import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    rand_col = (randint(0, 255),randint(0, 255),randint(0, 255))
    # 锁定屏幕进入绘图,避免set_at反复锁定
    screen.lock()
    for _ in xrange(100):
        rand_pos = (randint(0,693), randint(0, 479))
        # 画点
        screen.set_at(rand_pos, rand_col)
    screen.unlock()
    pygame.display.update()