import settings
import pygame
import pymunk 
import random
import math



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
        """height of the tank"""
        self.jet_y = self.tank.y + self.tank.height - bottom_of_tank
        """jet positions"""
        self.left_x = settings.LEFT_BUTTON
        self.middle_x = settings.MIDDLE_BUTTON
        self.right_x = settings.RIGHT_BUTTON

        """jet timers"""
        self.jet_duration = 0.25

        self.left_timer = 0.0
        self.middle_timer = 0.0
        self.right_timer = 0.0

        self.particles = [] 

    def activate_jet(self, jet_name):
        if jet_name == "left":
            self.left_active = True
            self.left_timer = self.jet_duration 
        elif jet_name == "middle":
            self.middle_active = True
            self.middle_timer = self.jet_duration
        elif jet_name == "right":
            self.right_active = True 
            self.right_timer = self.jet_duration 

    """Creates the method that updates the water jet as time passes"""
    def update(self, dt):
        if self.left_active:
            self.left_timer -= dt

            if self.left_timer <= 0:
                self.left_timer = 0
                self.left_active = False 

        if self.middle_active: 
            self.middle_timer -= dt

            if self.middle_timer <= 0:
                self.middle_timer = 0
                self.middle_active = False

        if self.right_active:
            self.right_timer -= dt

            if self.right_timer <= 0:
                self.right_timer = 0
                self.right_active = False 





        



        
    


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
    # STEP 5: DRAW THE WATER JETS
    def draw(self, screen):
        jet_bottom = self.jet_y
        jet_height = 100
        # Draw the left water jet
        if self.left_active:
            pygame.draw.line(screen, (0, 150, 255),(self.left_x, jet_bottom),(self.left_x, jet_bottom - jet_height), 50)
            pygame.draw.line(screen, (180, 240, 255),(self.left_x, jet_bottom),(self.left_x, jet_bottom - jet_height), 48)
        # Draw the middle water jet
        if self.middle_active:
            pygame.draw.line(screen, (0, 150, 255),(self.middle_x, jet_bottom),(self.middle_x, jet_bottom - jet_height), 50)
            pygame.draw.line(screen, (180, 240, 255),(self.middle_x, jet_bottom),(self.middle_x, jet_bottom - jet_height), 48)
        # Draw the right water jet
        if self.right_active:
            pygame.draw.line(screen, (0, 150, 255),(self.right_x, jet_bottom),(self.right_x, jet_bottom - jet_height), 50)
            pygame.draw.line(screen, (180, 240, 255),(self.right_x, jet_bottom),(self.right_x, jet_bottom - jet_height), 48)
        for p in self.particles:
            pygame.draw.circle(
            screen,
            settings.PARTICLE_COLOR,
            (int(p["x"]), int(p["y"])),
            settings.PARTICLE_RADIUS
        )


        def spawn_particles(self, x):
            for i in range(settings.PARTICLE_COUNT):
                angle = math.radians(-90 + random.uniform(-settings.PARTICLE_SPREAD, settings.PARTICLE_SPREAD))
                speed = settings.PARTICLE_SPEED * random.uniform(0.8, 1.2)
                self.particles.append({
                    "x": x + random.uniform(-6, 6),
                    "y": self.jet_y,
                    "vx": math.cos(angle) * speed,
                    "vy": math.sin(angle) * speed,
                    "life": settings.PARTICLE_LIFETIME,
                })


# STEP 6: EXPOSE THE JET STATE
# Provide a consistent way for physics.py to check whether a jet is active.
# Keep the jet position, direction, and affected region accessible.
# Do not let the visual jet and physics system use different jet locations.

# STEP 7: TEST THE WATER
# First test that the jet activates and expires correctly.
# Then check that its visual direction matches the force in physics.py.

