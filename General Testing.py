import Modules.Inputs as Inputs
import pygame
import Modules.PGLib as PGLib
import sys

# run game
window = PGLib.begin(400, 400, 'Test')

while True:
    # tests for up/down
    PGLib.step()

    if Inputs.is_control_down('Left'):
        print('Left')
    if Inputs.is_control_down('Right'):
        print('Right')
    if Inputs.is_quitting():
        sys.exit
    # test for if quit
    PGLib.end()
