import Modules.Inputs as Inputs
import pygame
import Modules.PGLib as PGLib

# check controls
print(Inputs.CONTROLS)
print()
"""
# add crouch
Inputs.add_control('Crouch', pygame.K_c)
print(Inputs.CONTROLS)
print()

# set crouch
Inputs.add_control('Crouch', pygame.K_F1)
print(Inputs.CONTROLS)
print()

# remove crouch
Inputs.remove_control('Crouch')
print(Inputs.CONTROLS)
print()

# get control
left = Inputs.get_control('Left')
print(left)
print()
"""
# run game
window = PGLib.begin(400, 400, 'Test')

while True:
    # tests for up/down
    PGLib.step()

    if Inputs.is_control_down('Left'):
        print('Left')
    if Inputs.is_control_down('right'):
        print('Right')

    # test for if quit
    PGLib.end()
