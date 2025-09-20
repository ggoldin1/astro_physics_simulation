This code simulates the atmospheric entry of a meteor and models its brightness over time.

**Main Purpose**

The program calculates how a meteor's physical properties (velocity, mass, height) change as it burns up in Earth's atmosphere, and tracks the resulting light intensity to create what's called an "F-Curve" - a plot showing how bright the meteor appears over time.
Key Physics Modeled
Atmospheric Effects:

Calculates atmospheric density at different altitudes using an exponential decay model
Adjusts gravity based on distance from Earth's center

**Meteor Dynamics:**

Deceleration: The meteor slows down due to atmospheric drag
Mass Loss: Material burns off (ablation) as the meteor heats up from friction
Height Loss: The meteor travels downward at an angle through the atmosphere

**Light Production:**

Calculates light intensity based on the meteor's velocity, mass, and atmospheric density
Converts this to apparent magnitude (astronomical brightness scale)
Uses different luminous efficiency coefficients (tau) depending on velocity

**Simulation Process**

The code runs a time-stepped simulation that:

Starts with initial conditions (30 km/s velocity, 500g mass, 250km altitude)
Each time step (0.0005 seconds):

Updates velocity (decreases due to drag)
Updates height (decreases as meteor descends)
Updates mass (decreases due to ablation)
Calculates resulting light intensity


Continues until the meteor either slows to <1000 m/s or burns up to <0.5g
Stores the light intensity values over time

**Output**

Prints final meteor state (velocity, mass, height, brightness)
Creates a graph showing light intensity vs. time - the characteristic "F-Curve" that astronomers use to study meteor behavior

This type of simulation is used in astronomy and planetary science to understand meteor physics and predict how meteors will appear to observers on the ground.
