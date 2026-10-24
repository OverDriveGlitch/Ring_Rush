# STEP 1: IMPORTS
# Import Pygame for drawing and settings.py for shared constants.
import pygame
import pymunk
import settings

# STEP 2: CREATE THE Ring CLASS
# Define Ring.__init__(self, x, y).
# Inputs: the ring's starting x and y coordinates.
# Store x and y as the ring's current position.
# Create vx and vy to represent horizontal and vertical velocity.
# Store radius and colour for drawing.
# Add an is_landed flag to track whether the ring has scored.
# Add an is_scored flag so the same ring cannot score repeatedly.
# If using Pymunk, store or reference the corresponding physics body.
class Ring:
    def __init__(self, x,y):
        #storing the starting spot of the ring
        self.x=x
        self.y=y

        #storing velocit
        self.vx=0
        self.vy=0

        # storing radius and color
        self.rad = settings.RING_RAD
        self.clr = (255, 0, 0)
        
        # connecting body in physics.py
        self.body = None

        #tracking if it lands or scores
        self.it_lands=False
        self.it_scores=False



# STEP 3: CREATE ring.draw(self, screen)    
# Draw the ring on the Pygame screen using its current position.
# Hint: pygame.draw.circle() can draw a ring outline using a width value.
# Convert floating-point coordinates to integers when drawing.
# The drawing position must match the physics body's position.
    def draw (self,screen):
        if self.body is not None:
            #checking if the ring has a body
            x, y = self.body.position
        else:
            x, y = self.x, self.y

        # Draw a hollow ring
        #draw.circle(where, color, position, radius, thickness)
        pygame.draw.circle(
            screen,self.colour,(int(x), int(y)),self.radius,4
        )


# STEP 4: DECIDE HOW LANDED RINGS WORK
# A landed ring should not continue moving freely as if it were floating.
# Decide whether the physics system will lock it in place or attach it
# to a peg using a suitable physics constraint.
# Keep the ring's landed/scored state consistent with physics.py.
