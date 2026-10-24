# STEP 1: IMPORTS
# Import Pymunk and settings.py if the team chooses Pymunk.
# Import or reference the Ring class as needed.
import pygame
import pymunk
import settings
# STEP 2: CREATE THE Physics CLASS
# Define Physics.__init__(self, tank).
# Create the physics space if using Pymunk.
# Configure gravity and the simulation settings.
# Keep the physics boundaries aligned with the tank's visual boundaries.
class Physics:
  def __init__(self, tank):
    """
    This function always runs when creating a new physics object. The perameters of this function are as followed:
      self: refers to the physics object being created
      tank: dimension and peg positionss.
    """
    self.tank=tank
    self.space=pymunk.Space() #creates a pysical space for the object Pysics
    self.space.gravity=(0,900) #horizontal acceleration is zero and vertical acceleration is 900

    # Create static collision shapes for the tank walls.
    #creating a wall that is 900 by 600 and has a static body
    wall_left=pymunk.Segment(
      self.space.static_body,
      (settings.LEFT_TANK,settings.TOP_TANK),
      (settings.LEFT_TANK,settings.BOTTOM_TANK),
      5
    )
    wall_top=pymunk.Segment(
      self.space.static_body,
      (settings.LEFT_TANK, settings.TOP_TANK),
      (settings.RIGHT_TANK, settings.TOP_TANK),
      5
    )
    wall_right=pymunk.Segment(
      self.space.static_body,
      (settings.RIGHT_TANK, settings.TOP_TANK),
      (settings.RIGHT_TANK, settings.BOTTOM_TANK),
      5
    )
    wall_bottom=pymunk.Segment(
      self.space.static_body,
      (settings.LEFT_TANK, settings.BOTTOM_TANK),
      (settings.RIGHT_TANK, settings.BOTTOM_TANK),
      5
    )
    self.space.add(wall_left, wall_right, wall_bottom, wall_top) #this adds the walls to the collision calculations that pymuck has to do
    
    # Add collision shapes for the pegs using the positions in tank.pegs.
  
    peg_shape1 = pymunk.Circle(
      self.space.static_body,
      2,
      (settings.P_X1+(settings.P_X1-settings.P_X2), settings.P_Y1+(settings.P_Y1-settings.P_Y2))
    )

    peg_shape2 = pymunk.Circle(
        self.space.static_body,
        2,
        (settings.P2_X1+(settings.P2_X1-settings.P2_X2), settings.P2_Y1+(settings.P2_Y1-settings.P2_Y2))
      )

    peg_shape3 = pymunk.Circle(
        self.space.static_body,
        2,
        (settings.P3_X1+(settings.P3_X1-settings.P3_X2), settings.P3_Y1+(settings.P3_Y1-settings.P3_Y2))
      )
  

# STEP 3: ADD RINGS TO THE PHYSICS WORLD
# Create a physics body and collision shape for each ring.
# Choose mass, moment of inertia, and collision geometry.
# Add each body and shape to the physics space.
# Make sure ring.py can access the matching physics body.
# Hint: Pymunk bodies and shapes are separate objects.
  def add_ring(self, ring):
    #create a physics body for the ring
    pass

# STEP 4: DEFINE physics.update(self, rings, water, dt)
# This function is called once per game frame by main.py.
# Read the current water-jet state from water.py.
# Apply forces to rings affected by an active jet.
# Apply the chosen approximation of buoyancy and water drag.
# Advance the physics simulation using dt.
# Detect or process collisions with walls, pegs, and other rings.
# Check for new successful ring placements.
# Return the number of newly earned points for this frame.
# Hint: Use Pymunk collision handlers or carefully designed overlap checks.
# Do not advance the simulation by a fixed amount if frame times vary.

# STEP 5: APPLY WATER FORCES
# Only push rings that are within the jet's affected region.
# Decide the jet's position, direction, range, and force falloff.
# Apply force over time for a sustained push, or an impulse for a quick kick.
# Make sure the visual jet and the physical force agree.
# Hint: A jet that pushes every ring equally will feel less convincing.

# STEP 6: SIMULATE FLOATING
# Approximate buoyancy by applying an upward force.
# Use gravity and drag to create movement that settles naturally.
# Tune these forces until the rings feel responsive rather than weightless.
# Remember: Pymunk does not automatically simulate real fluid dynamics.

# STEP 7: DETECT SUCCESSFUL RING PLACEMENTS
# Determine when a ring has moved over a peg and is properly settled.
# Consider the ring's inner opening, the peg position, and the ring's motion.
# A simple circle overlap alone is not enough to guarantee a valid landing.
# Mark a successful ring so it cannot score again.
# Return points only when a ring newly scores.
