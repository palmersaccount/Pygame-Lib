import pygame


WIDTH = 1600
HEIGHT = 900
SIZE = [WIDTH, HEIGHT]
CAPTION = 'PGLIB Game'


def begin(w, h, name):
    global WIDTH, HEIGHT, SIZE, CAPTION

    pygame.init()
    window = pygame.display.set_mode((w, h))

    WIDTH = w
    HEIGHT = h
    SIZE = [WIDTH, HEIGHT]
    CAPTION = name

    pygame.display.set_caption(name)
    return window
