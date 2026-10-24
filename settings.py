import pygame
import pymunk

# STEP 1: SCREEN SETTINGS
# Create constants for the screen width, screen height, and FPS.
# Hint: Pygame coordinates start at (0, 0) in the top-left corner.
# x increases to the right; y increases downward.

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

# STEP 2: TANK SETTINGS
# Define the left, right, top, and bottom boundaries of the tank.
# The tank drawing and physics collision boundaries must use the same values.

TANK_WIDTH = 347
TANK_HEIGHT = 300

LEFT_TANK = 290
RIGHT_TANK = 637
TOP_TANK = 44
BOTTOM_TANK = 348

# STEP 3: RING SETTINGS
# Define the starting number of rings, their radius, and their mass.
# Keep the mass consistent with the physics system if using Pymunk.

NUM_RINGS = 4
RING_RAD = 20
RING_MASS = 1 

# STEP 4: WATER SETTINGS
# Define water jet strength, jet duration, and water particle settings.
# Tune these values through testing rather than guessing the final values.

JET_STRENGTH = 500
JET_TIME = 0.7


# STEP 5: PHYSICS SETTINGS
# Define gravity, water drag, and approximate buoyancy settings.
# If using Pymunk, check its expected units and keep your units consistent.
# Positions: pixels; velocities: pixels per second; dt: seconds.

GRAVITY = 500
WATER_DRAG = 0.7
BUOYANCY = 0.5

# STEP 6: GAME SETTINGS
# Define the round duration, starting score, and points per successful ring.
# Import these constants into other files instead of duplicating the values.

ROUND_TIME = 180
STARTING_SCORE = 0
RING_POINTS = 50
