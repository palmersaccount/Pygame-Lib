import pygame

CONTROLS = {
    "Left": [pygame.K_LEFT],
    "Right": [pygame.K_RIGHT],
    "Up": [pygame.K_UP],
    "Down": [pygame.K_DOWN],
    "Exit": [pygame.K_ESCAPE]
}


# get a specific control
def get_control(control_key):
    return CONTROLS[control_key]


# add a specific control
def add_control(control_key, control_value):
    if control_key in CONTROLS.keys():
        CONTROLS[control_key].append(control_value)
    else:
        CONTROLS[control_key] = []
        CONTROLS[control_key].append(control_value)


# remove a specific control
def remove_control(control_key):
    CONTROLS.pop(control_key)


# clear a specific control
def clear_control(control_key):
    CONTROLS[control_key] = []


# get if a control is down
def is_control_down(control_key):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in CONTROLS[control_key]:
                return True
    return False


# get if a control is up
def is_control_up(control_key):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key in CONTROLS[control_key]:
                return True
    return False


# get if the user is quitting
def is_quitting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.key in CONTROLS['Exit']:
                return True
    return False
