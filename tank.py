# STEP 1: IMPORTS
# Import Pygame and settings.py.
import pygame
import settings
# STEP 2: CREATE THE Tank CLASS
# Define Tank.__init__(self).
# Store the tank boundaries using the shared settings constants.
# Create a list of peg positions.
# Each peg position should use the same coordinate system as the rings.
# Decide the peg radius and appearance.
# Make the peg positions accessible to physics.py.
class tank: 
  def __init__(self):
    self.width = setting.TANK_WIDTH
    self.height = setting.TANK_HEIGHT


# STEP 3: DEFINE tank.draw(self, screen)
# Draw the tank outline and its boundaries.
# Draw the pegs at the positions stored in the tank.
# Add water colour or other visual details if desired.
# Hint: pygame.draw.rect() can draw the tank boundary.
# Hint: pygame.draw.circle() can draw round pegs.

# STEP 4: KEEP GRAPHICS AND COLLISIONS CONSISTENT
# The visual tank boundaries must match the physics boundaries.
# The visible pegs must match the physics collision shapes.
# If a peg is moved, update the shared peg positions rather than
# changing only the drawing code.

# STEP 5: TEST THE TANK
# Check that rings cannot escape through visible walls.
# Check that rings interact with the pegs where the player expects.
