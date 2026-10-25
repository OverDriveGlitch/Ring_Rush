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

    #Friction adds resistance that it has with the wall
    wall_left.friction = 0.5
    wall_top.friction = 0.5
    wall_right.friction = 0.5
    wall_bottom.friction = 0.5
    #Elasticity makes the rings bounce when it toaches the wall
    wall_left.elasticity = 0.3
    wall_top.elasticity = 0.3
    wall_right.elasticity = 0.3
    wall_bottom.elasticity = 0.3

    self.space.add(wall_left, wall_right, wall_bottom, wall_top) #this adds the walls to the collision calculations that pymuck has to do
    
    # Add collision shapes for the pegs using the positions in tank.pegs.
  
    peg_shape1 = pymunk.Circle(
      self.space.static_body,
      tank.peg_radius,
      tank.peg_positions[0]
    )

    peg_shape2 = pymunk.Circle(
        self.space.static_body,
        tank.peg_radius,
        tank.peg_positions[1]
      )

    peg_shape3 = pymunk.Circle(
        self.space.static_body,
        tank.peg_radius,
        tank.peg_positions[2]
      )

    for peg in [peg_shape1, peg_shape2, peg_shape3]:
            peg.friction = 0.5
            peg.elasticity = 0.5

    self.space.add(peg_shape1, peg_shape2, peg_shape3)
    
    self.peg_positions = tank.peg_positions
  

# STEP 3: ADD RINGS TO THE PHYSICS WORLD
# Create a physics body and collision shape for each ring.
# Choose mass, moment of inertia, and collision geometry.
# Add each body and shape to the physics space.
# Make sure ring.py can access the matching physics body.
# Hint: Pymunk bodies and shapes are separate objects.
  def add_ring(self, ring):
    #create a physics body for the ring
    moment = pymunk.moment_for_circle(settings.RING_MASS,0,settings.RING_RAD)
    #calling function moment_for_circle from pymunk and calculates how difficult the ring is to rotate
    body = pymunk.Body(settings.RING_MASS, moment)
    #creates the ring's physics body using its mass and rotational movement
    body.position = (ring.x, ring.y)
    #starts the physics body at the ring's current position.
    shape = pymunk.Circle(body, settings.RING_RAD)#collision space is circular
    # Add the body and shape to the physics world
    shape.friction = 0.5
    shape.elasticity = 0.3
    self.space.add(body, shape)
    ring.body = body #adds the body back to ring object

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
  def update(self, rings, water, dt):
    #applies upward force to simulate bouyancy
    for ring in rings:
        if ring.body is not None:
            body=ring.body

            body.apply_force_at_local_point(
                (0, -ring.body.mass * 700),
                (0, 0)
            )
            # Reduce horizontal and vertical velocity gradually
            body.velocity = (
                body.velocity.x * 0.99,
                body.velocity.y * 0.99
            )

            # Check the left, middle, and right water jets
            jets = [
                (water.left_active, water.left_x),
                (water.middle_active, water.middle_x),
                (water.right_active, water.right_x)
            ]

            for jet_active, jet_x in jets:
                if not jet_active:
                    continue

                # Check whether the ring is within the jet's range
                ring_x = body.position.x
                ring_y = body.position.y

                horizontal_distance = abs(ring_x - jet_x)
                vertical_distance = water.jet_y - ring_y

                if (
                    horizontal_distance <= settings.RING_RAD + 12
                    and -settings.RING_RAD <= vertical_distance <= 100
                ):
                    # Push the ring upward
                    self.apply_water_force(
                        ring,
                        0,
                        -body.mass * 2500
                    )
    #using the pymunk advance simulation by dt seconds 
    self.space.step(dt)
    # updates the rings position with the current
    for ring in rings:
        if ring.body is not None:
            ring.x = ring.body.position.x
            ring.y = ring.body.position.y
    # retuns the updated score
    return self.check_scoring(rings)

# STEP 5: APPLY WATER FORCES
# Only push rings that are within the jet's affected region.
# Decide the jet's position, direction, range, and force falloff.
# Apply force over time for a sustained push, or an impulse for a quick kick.
# Make sure the visual jet and the physical force agree.
# Hint: A jet that pushes every ring equally will feel less convincing.
  def apply_water_force(self, ring, force_x, force_y):
    if ring.body is not None:
        ring.body.apply_force_at_local_point(
            (force_x, force_y),
            (0, 0)
        )


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
  
  def check_scoring(self, rings):
    points = 0
    for ring in rings:
        if ring.body is None or ring.it_scores:
            continue
        ring_position = ring.body.position
        ring_velocity = ring.body.velocity
        for peg_position in self.peg_positions:
            dx = ring_position.x - peg_position[0]
            dy = ring_position.y - peg_position[1]
            distance = (dx * dx + dy * dy) ** 0.5
            # Temporary check for a ring settled beside a peg
            target_distance = settings.RING_RAD * 2
            tolerance = 5
            speed = (ring_velocity.x ** 2 + ring_velocity.y ** 2) ** 0.5
            if (abs(distance - target_distance) <= tolerance and speed < 20):
                ring.it_lands = True
                ring.it_scores = True

                ring.body.velocity = (0, 0)
                ring.body.angular_velocity = 0
                ring.body.body_type = pymunk.Body.KINEMATIC
                points += 1
                break

    return points

