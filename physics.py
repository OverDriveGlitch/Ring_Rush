# STEP 1: IMPORTS
# Import Pymunk and settings.py if the team chooses Pymunk.
# Import or reference the Ring class as needed.

# STEP 2: CREATE THE Physics CLASS
# Define Physics.__init__(self, tank).
# Create the physics space if using Pymunk.
# Configure gravity and the simulation settings.
# Create static collision shapes for the tank walls.
# Add collision shapes for the pegs using the positions in tank.pegs.
# Keep the physics boundaries aligned with the tank's visual boundaries.

# STEP 3: ADD RINGS TO THE PHYSICS WORLD
# Create a physics body and collision shape for each ring.
# Choose mass, moment of inertia, and collision geometry.
# Add each body and shape to the physics space.
# Make sure ring.py can access the matching physics body.
# Hint: Pymunk bodies and shapes are separate objects.

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
