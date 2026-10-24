# STEP 1: IMPORT THE MODULES
# Import Pygame, settings.py, Ring, Physics, Water, Tank, and UI.

import pygame
import pymunk
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from tank import Tank
from physics import Physics
from ui import UI
from ring import Ring 

# STEP 2: INITIALIZE PYGAME
# Initialize Pygame.
# Create the game window using the shared screen dimensions.
# Set the window title.
# Create a clock to control FPS and calculate dt.

pygame.init()

#setting up screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# STEP 3: CREATE THE GAME OBJECTS
# Create one Tank object first so its peg positions are available.
# Create Physics using that tank.
# Create Water and UI objects. (wait for water)
# Create the starting rings and add their physics bodies.
# Hint: Use a loop to create multiple rings rather than repeating code.

tank = Tank()
physics = Physics(tank)
ui = UI()


# STEP 4: START THE GAME LOOP
# Continue until the player closes the window.
# Calculate dt using the elapsed time since the previous frame.
# Limit unusually large dt values to avoid sudden physics jumps.
# Process events, update game logic, then draw the frame.

clock = pygame.time.Clock()

running = True
while running:

    # dt = delta time since last frame, limits fps to 60
    dt = clock.tick(FPS) / 1000 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ui.state =="start":
                ui.start_round()
            elif event.key == pygame.K_r and ui.state =="game_over":
                ui.start_round()

            elif event.key == pygame.K_ESCAPE:
                running = False
    
    keys = pygame.key.get_pressed()
    ui.leftpressed = keys[pygame.K_a]

    ui.update(dt)

    screen.blit(ui.background_image, (0, 0))

    # TANK AND RING DRAWING HERE

    # draw menus
    ui.draw(screen)

    pygame.display.flip()

# STEP 5: HANDLE INPUT
# Handle the window-close event.
# Detect the agreed key or button for activating the water jet.
# Handle start, restart, and exit inputs as appropriate.
# Avoid placing the physics calculations directly inside event handling.

    #elif keys[pygame.K_d]:
     #   ui.rightpressed = True
    #elif keys[pygame.K_s]:
     #   ui.midpressed = True


    


# STEP 6: UPDATE THE GAME
# Call water.update(dt).
# Call physics.update(rings, water, dt).
# Receive the number of newly earned points from physics.py.
# Pass those points to ui.add_score(points).
# Call ui.update(dt) to update the timer and game state.
# Only update gameplay physics while the game is actively being played.



# STEP 7: DRAW THE FRAME
# Clear the screen.
# Draw the tank.
# Draw every ring.
# Draw the water effects.
# Draw the score, timer, and current screen.
# Update the display after all drawing is complete.



# STEP 8: END THE GAME
# Exit the game loop when requested.
# Shut down Pygame cleanly.
# Test that the game closes without errors.

pygame.quit()

# STEP 9: TEST INTEGRATION
# Check that every imported class and called function exists.
# Check that the arguments passed to functions match their definitions.
# Check that score events are not counted more than once.
# Check that all files use the same coordinate system and units.
