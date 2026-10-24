# STEP 1: IMPORTS
# Import Pygame and settings.py.

# STEP 2: CREATE THE UI CLASS
# Define UI.__init__(self).
# Store the current score.
# Store the remaining time in the round.
# Create fonts for text.
# Store the current game state, such as start, playing, or game over.
# Hint: Use one clearly defined set of game-state names.

# STEP 3: DEFINE ui.add_score(self, points)
# Increase the score by the points received from main.py.
# Only accept points for successful ring placements.
# Do not detect collisions or decide whether a ring has landed here.

# STEP 4: DEFINE ui.update(self, dt)
# Decrease the timer while the game is being played.
# Stop the timer when the round ends.
# Switch to the game-over state when time reaches zero.
# Hint: Store time in seconds and use dt.

# STEP 5: DEFINE ui.draw(self, screen)
# Draw the current score and remaining time.
# Draw instructions or prompts when appropriate.
# Draw the start screen or game-over screen based on the game state.
# Keep drawing separate from updating the score and timer.

# STEP 6: DEFINE ANY EXTRA UI FUNCTIONS
# Add separate functions for start instructions, game over, and restart
# if that makes the code easier to organize.
# Agree with main.py on how the player starts and restarts a round.

# STEP 7: TEST THE UI
# Check that the score increases when main.py reports earned points.
# Check that the timer stops when the round ends.
# Check that restarting resets the score and timer correctly.
