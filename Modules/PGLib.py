import pygame
import sys
import time
import Modules.Inputs as Inputs


def begin(w=1600, h=900, name='PGLIB Game', background=None):
    global WIDTH, HEIGHT, SIZE, CAPTION, WINDOW
    global BACKGROUND, BACKGROUND_COLOR

    pygame.init()
    window = pygame.display.set_mode((w, h))

    WIDTH = w
    HEIGHT = h
    SIZE = [WIDTH, HEIGHT]
    CAPTION = name
    BACKGROUND_COLOR = [0, 0, 0]
    pygame.display.set_caption(name)

    WINDOW = window
    return window


def draw_background():
    global BACKGROUND_COLOR, BACKGROUND, WINDOW, SIZE
    WINDOW.fill(BACKGROUND_COLOR)

    # if BACKGROUND != None:
    #    pygame.image.blit(BACKGROUND, [0, 0], SIZE)


def step():
    draw_background()
    time.sleep(.003)


def end():
    if Inputs.is_quitting():
        pygame.quit()
        sys.exit()
