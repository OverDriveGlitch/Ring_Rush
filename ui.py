# STEP 1: IMPORTS
# Import Pygame and settings.py.
import pygame
import os
import settings
#images
GAME_HEIGHT = 600
GAME_WIDTH = 900
background_image = pygame.image.load(os.path.join("downloads","Ring_Rush.png"))
window = pygame.display.set_mode ((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Ring Rush") #title of the window
pygame.font.init()
game_font = pygame.font.SysFont("Arial", 24)

# STEP 2: CREATE THE UI CLASS
# Define UI.__init__(self).
class UI:
  def __init__(self):
    self.remaining_time = 100
    self.start = "start"
    self.score = 0
  
  
  
# Store the current score.

# Store the remaining time in the round.
def update(self, dt):
  if self.state == "playing"
        
# Create fonts for text.
# Store the current game state, such as start, playing, or game over.
# Hint: Use one clearly defined set of game-state names.
pygame.display.set_caption("Ring Rush") #title of the window



# STEP 3: DEFINE ui.add_score(self, points)
  def add_score(self, points):
    self.score += points
# Increase the score by the points received from main.py.

# Only accept points for successful ring placements.
# Do not detect collisions or decide whether a ring has landed here.

# STEP 4: DEFINE ui.update(self, dt)
  def update(self, dt):
        if self.state == "playing":
            self.remaining_time -= dt

            if self.remaining_time <= 0:
                self.remaining_time = 0
                self.state = "game_over"
# Decrease the timer while the game is being played.
# Stop the timer when the round ends.
# Switch to the game-over state when time reaches zero.
# Hint: Store time in seconds and use dt.

# STEP 5: DEFINE ui.draw(self, screen)
def draw(self, screen)
  score_text = f"Score: {self.score}"
  time_text = f"Time remaning is: {self.time_remaining:.0f}"
  score_surface = game_font.render(score_text, True, "white")
  time_surface = game_font.render(time_text, True, "white")
  window.blit(score_surface, (100,100))
  window.blit(time_surface,(100,200))
  
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
