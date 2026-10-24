# STEP 1: IMPORTS
# Import Pygame and settings.py.
import pygame
import settings
from pathlib import Path

# STEP 2: CREATE THE Tank CLASS
# Define Tank.__init__(self).
# Store the tank boundaries using the shared settings constants.
# Create a list of peg positions.
# Each peg position should use the same coordinate system as the rings.
# Decide the peg radius and appearance.
# Make the peg positions accessible to physics.py.

"""The tank class stores the position and size of th water tank, as well as the three peg positions"""
class Tank: 
  def __init__(self):
    """Calculate the starting position of the tank so it is centered inside the game window
    Store the tank's width and height using the values from settings.py"""
    self.x = (settings.SCREEN_WIDTH - settings.TANK_WIDTH) // 2
    self.y = (settings.SCREEN_HEIGHT - settings.TANK_HEIGHT) // 2
    self.width = settings.TANK_WIDTH
    self.height = settings.TANK_HEIGHT

    """Peg positions
    
    Each tuple has an x and y coordinate
    
    the left peg is halfway down the tank
    
    the middle peg is higher than the other two
    
    the right peg is slightly lower than the left
    
    the positions are calculated in comparision to the tank"""
    self.peg_positions = [
      (self.x + self.width // 4, self.y + self.height // 2),
      (self.x + self.width // 2, self.y + self.height // 4),
      (self.x + self.width * 3 // 4, self.y + self.height * 3 // 5),
       ]

    """Peg collision radius determines the size of each pegs rounded tip"""
    self.peg_radius = 10
    pic_folder = Path(__file__).resolve().parent / "pic"
    self.tank_image = pygame.image.load(
      str(pic_folder / "Ring_Rush.png")
    ).convert_alpha()

    """loading tank, this finds the pic folder and loads the tank image"""
  def draw(self, screen):
    screen.blit(self.tank_image, (0,0))
    #drawing the pink peg
    for x, y in self.peg_positions:
      pygame.draw.line(
        screen,
        (255, 105, 180),
        (x, self.y + 15),
        (x,y),
        6
      )
      pygame.draw.circle(
        screen,
        (255, 105, 180),
        (x, y),
        self.peg_radius
      )


  

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
