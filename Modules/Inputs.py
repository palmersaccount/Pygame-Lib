import pygame


CONTROLS = {
    "Left": [pygame.key.K_LEFT, pygame.key.K_A],
    "Right": [pygame.key.K_RIGHT, pygame.key.K_D],
    "Up": [pygame.key.K_UP, pygame.key.K_W],
    "Down": [pygame.key.K_DOWN, pygame.key.K_S]
}


def get_control(control_key):
    return CONTROLS[control_key]


def set_control(control_key, control_value):
    if CONTROLS[control_key] == None:
        CONTROLS[control_key] = []
    if isinstance(control_value, list):
        CONTROLS[control_key].extend(control_value)
    else:
        CONTROLS[control_key].append(control_value)
