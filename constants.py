#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Nov 2019
# This module contains constants for the alien game

# CircuitPython screen size is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
# Using for Button State
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}
