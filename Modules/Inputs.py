import pygame


CONTROLS = {
    "Left": [pygame.K_LEFT, pygame.K_a],
    "Right": [pygame.K_RIGHT, pygame.K_d],
    "Up": [pygame.K_UP, pygame.K_w],
    "Down": [pygame.K_DOWN, pygame.K_s]
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
