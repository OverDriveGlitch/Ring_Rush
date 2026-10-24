# STEP 1: IMPORTS
# Import Pygame for drawing and settings.py for shared constants.

# STEP 2: CREATE THE Ring CLASS
# Define Ring.__init__(self, x, y).
# Inputs: the ring's starting x and y coordinates.
# Store x and y as the ring's current position.
# Create vx and vy to represent horizontal and vertical velocity.
# Store radius and colour for drawing.
# Add an is_landed flag to track whether the ring has scored.
# Add an is_scored flag so the same ring cannot score repeatedly.
# If using Pymunk, store or reference the corresponding physics body.

# STEP 3: CREATE ring.draw(self, screen)
# Draw the ring on the Pygame screen using its current position.
# Hint: pygame.draw.circle() can draw a ring outline using a width value.
# Convert floating-point coordinates to integers when drawing.
# The drawing position must match the physics body's position.

# STEP 4: DECIDE HOW LANDED RINGS WORK
# A landed ring should not continue moving freely as if it were floating.
# Decide whether the physics system will lock it in place or attach it
# to a peg using a suitable physics constraint.
# Keep the ring's landed/scored state consistent with physics.py.
