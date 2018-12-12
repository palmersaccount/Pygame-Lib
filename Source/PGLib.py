import pygame

def begin(w, h, name):
    pygame.init()
    window = pygame.display.set_mode((w, h))
    pygame.display.set_caption(name)
    return window

def draw_sprites(sprites):
    pass
