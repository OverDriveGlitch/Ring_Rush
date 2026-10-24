# STEP 1: IMPORTS
# Import Pygame and settings.py.


import pygame
import os
import settings
#images
GAME_HEIGHT = 600
GAME_WIDTH = 900


# STEP 2: CREATE THE UI CLASS
# Define UI.__init__(self).
class UI:
  def __init__(self):
    self.leftpressed = False
    self.remaining_time = settings.ROUND_TIME
    self.state = "start"
    self.score = settings.STARTING_SCORE
    self.button_image = pygame.image.load("pic/button.png")
    print("Button image size:", self.button_image.get_size())
    self.end_image = pygame.image.load("pic/End.png")
    self.start_image = pygame.image.load("pic/Start.png")
    self.background_image = pygame.image.load("pic/Ring_Rush.png")
    pygame.display.set_caption("Ring Rush") #title of the window
    pygame.font.init()
    self.game_font = pygame.font.SysFont("Arial", 24)
    self.button_image = pygame.transform.scale(self.button_image, (175,175))

   
    # Store the current score.

    # Store the remaining time in the round.
  
        
    # Create fonts for text.
    # Store the current game state, such as start, playing, or game over.
    # Hint: Use one clearly defined set of game-state names.
  



    # STEP 3: DEFINE ui.add_score(self, points)
  def add_score(self, points):
      if self.state == "playing" and points > 0: 
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
  def draw(self, screen):
      if self.state == "start":
          screen.blit(self.start_image, (0,0))
          return
      elif self.state == "game_over":
           screen.blit(self.end_image,(0,0))
           return
      score_text = f"Score: {self.score}"
      time_text = f"Time remaning is: {self.remaining_time:.0f}"
      score_surface = self.game_font.render(score_text, True, "white")
      time_surface = self.game_font.render(time_text, True, "white")
    # Draw the current score and remaining time.
      screen.blit(score_surface, (100,100))
      screen.blit(time_surface,(100,200))
    # Draw instructions or prompts when appropriate.
      instruction_text = "Put all the rings inside the hooks"
      instruction_surface = self.game_font.render(instruction_text, True, "white")
      screen.blit(instruction_surface, (450, 20))
    
      #if a button is pressed then the image will change
      """
      IF WE HAVE TIME CHANGE THIS BUTTON PLS OMG ITS BAD
      """
      if self.leftpressed:
          screen.blit(self.button_image, (231, 413))
      if self.midpressed:
          screen.blit(self.button_image, (362, 413))
      if self.rightpressed:
          screen.blit(self.button_image, (501, 413))
     
    # Draw the start screen or game-over screen based on the game state.
    
    # Keep drawing separate from updating the score and timer.
    #already is seperate lowkey
    # STEP 6: DEFINE ANY EXTRA UI FUNCTIONS
    # Add separate functions for start instructions, game over, and restart
  def start_round(self):
      self.score = settings.STARTING_SCORE
      self.remaining_time = settings.ROUND_TIME
      self.state = "playing"
        # if that makes the code easier to organize.
    # Agree with main.py on how the player starts and restarts a round.
  
    # STEP 7: TEST THE UI
    # Check that the score increases when main.py reports earned points.
    # Check that the timer stops when the round ends.
    # Check that restarting resets the score and timer correctly.


