import Modules.Inputs as Inputs
import pygame

# check controls
print(Inputs.CONTROLS)
print()

# add crouch
Inputs.set_control('Crouch', pygame.key.K_C)
print(Inputs.CONTROLS)
print()
