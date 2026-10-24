import settings
import pygame
import pymunk 

bottom_of_tank = 20

# STEP 1: IMPORTS
# Import Pygame and the shared values from settings.py.

# STEP 2: CREATE THE Water CLASS
class Water:
    def __init__(self, tank):
        self.tank = tank

        self.left_active = False
        self.middle_active = False
        self.right_active = False

        self.jet_y = self.tank.y + self.tank.height - bottom_of_tank

        
    


# Define Water.__init__(self).
# Store whether the jet is active.
# Store how much time remains before the jet switches off.
# Store the jet's position and direction.
# Create a collection for water particles or bubbles.
# Hint: A list is suitable for managing multiple particle objects.

# STEP 3: DEFINE water.activate_jet(self)
# Activate the jet when the player presses the appropriate control.
# Set the remaining jet duration.
# Avoid resetting the duration continuously while a key is held,
# unless continuous activation is the intended mechanic.
# Decide whether the player can activate multiple jets independently.

# STEP 4: DEFINE water.update(self, dt)
# Reduce the remaining jet duration while it is active.
# Turn the jet off when its duration expires.
# Move water particles and bubbles using dt.
# Remove particles that have expired or left the visible area.
# Hint: dt is the elapsed time in seconds, not the number of frames.

# STEP 5: DEFINE water.draw(self, screen)
# Draw the jet while it is active.
# Draw bubbles, splashes, and particles.
# Use colours, transparency effects, or small shapes to suggest water.
# Keep drawing separate from movement and physics calculations.

# STEP 6: EXPOSE THE JET STATE
# Provide a consistent way for physics.py to check whether a jet is active.
# Keep the jet position, direction, and affected region accessible.
# Do not let the visual jet and physics system use different jet locations.

# STEP 7: TEST THE WATER
# First test that the jet activates and expires correctly.
# Then check that its visual direction matches the force in physics.py.
