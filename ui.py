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
  def __init__(self, button_sound):
    #bascially just loads all the images from our files  
    self.button_sound=button_sound
    self.last_sound_time = 0      # when the sound last played (milliseconds)
    self.sound_delay = 300 
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
    self.game_font = pygame.font.SysFont("arialrounded", 24)
    self.button_image = pygame.transform.scale(self.button_image, (175,175))
    self.win_image = pygame.image.load("pic/Win.png")
    self.win_image = pygame.transform.scale(self.win_image, (900, 600))
   
    
    # STEP 3: DEFINE ui.add_score(self, points)
  
  def add_score(self, points):
      #once game starts playing it'll start tracking the score
      if self.state == "playing" and points > 0: 
        self.score += points
        #win condition
        if self.score >= 150:
            self.state = "win"
      
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
  #prints the 3 different scenarios onto main
  def draw(self, screen):
      if self.state == "start":
          screen.blit(self.start_image, (0,0))
          return
      elif self.state == "game_over":
           screen.blit(self.end_image,(0,0))
           return
      if self.state == "win":
          screen.blit(self.win_image,(0,0))
          return
      score_text = f"SCORE: {self.score}"
      time_text = f"TIME REMAINING: {self.remaining_time:.0f}"
      score_surface = self.game_font.render(score_text, True, "white", (204, 85, 0))
      time_surface = self.game_font.render(time_text, True, "white", (204, 85, 0))
    # Draw the current score and remaining time.
      screen.blit(score_surface, (50,100))
      screen.blit(time_surface,(20,200))
    # Draw instructions or prompts when appropriate.
      
  
      #if a button is pressed then the image will change
      """
      IF WE HAVE TIME CHANGE THIS BUTTON PLS OMG ITS BAD
      """

      play_sound = False
      
      if self.leftpressed:
        screen.blit(self.button_image, (231, 413))
        play_sound = True
      if self.midpressed:
        screen.blit(self.button_image, (362, 413))
        play_sound = True
      if self.rightpressed:
        screen.blit(self.button_image, (501, 413))
        play_sound = True

      now = pygame.time.get_ticks()
      if play_sound and now - self.last_sound_time >= self.sound_delay:
        self.button_sound.play()
        self.last_sound_time = now
     
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
  
   

