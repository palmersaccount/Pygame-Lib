import pygame


WIDTH = 1600
HEIGHT = 900
SIZE = [WIDTH, HEIGHT]


def begin(w, h, name):
    global WIDTH, HEIGHT, SIZE

    pygame.init()
    window = pygame.display.set_mode((w, h))

    WIDTH = w
    HEIGHT = h
    SIZE = [WIDTH, HEIGHT]

    pygame.display.set_caption(name)
    return window
