# Meteor Atmospheric Entry Simulation

A Python simulation that models the physics of a meteor burning up in Earth's atmosphere and generates the characteristic light curve (F-Curve) observed by astronomers.

## Overview

This program simulates the atmospheric entry of a meteor by calculating how its physical properties change over time as it encounters atmospheric drag and burns up due to friction. The simulation produces a light intensity curve showing how bright the meteor appears to ground-based observers.

## Features

- **Real-time Physics Simulation**: Models atmospheric drag, mass ablation, and gravitational effects
- **Atmospheric Modeling**: Calculates air density variations with altitude
- **Light Curve Generation**: Produces F-Curves used in meteor astronomy research
- **Customizable Parameters**: Adjustable meteor properties and atmospheric conditions

## Physics Modeled

### Atmospheric Effects
- Exponential atmospheric density decay with altitude
- Gravity variation with distance from Earth's center
- Temperature and gas constant considerations

### Meteor Dynamics
- **Deceleration**: Atmospheric drag reduces meteor velocity
- **Mass Loss**: Ablation removes material as the meteor heats up
- **Trajectory**: Angular descent through atmospheric layers

### Light Production
- Luminous efficiency based on velocity regime
- Atmospheric density effects on brightness
- Apparent magnitude calculations for observers

## Initial Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Velocity | 30.0 km/s | Initial meteor speed |
| Mass | 500.0 g | Initial meteor mass |
| Height | 250.0 km | Starting altitude |
| Angle | 45° | Entry angle from horizontal |
| Density | 0.005 g/cm³ | Meteor material density |
| Time Step | 0.0005 s | Simulation resolution |

## Simulation Process

1. **Initialize** meteor with starting conditions
2. **Time-step loop** continues while meteor velocity > 1000 m/s and mass > 0.5g:
   - Calculate atmospheric density at current height
   - Update velocity (drag deceleration)
   - Update height (downward trajectory)
   - Update mass (ablation loss)
   - Calculate light intensity
   - Store data points
3. **Generate** F-Curve plot showing light intensity vs. time
4. **Output** final meteor state

## Dependencies

```python
import matplotlib.pyplot as plt
import numpy as np
import math
```

## Usage

Run the script directly:
```bash
python meteor_simulation.py
```

The program will:
- Execute the simulation automatically
- Print final meteor parameters
- Display an F-Curve plot showing light intensity over time

## Output

### Terminal Output
- Final velocity, mass, height, light intensity, and apparent magnitude
- Total simulation steps completed

### Graphical Output
- **F-Curve**: Light intensity vs. time plot
- Grid lines and axis labels for easy interpretation
- Shows the characteristic meteor brightness pattern

## Applications

This simulation is useful for:
- **Meteor astronomy research**: Understanding observed light curves
- **Atmospheric entry studies**: Modeling spacecraft or debris reentry
- **Educational purposes**: Demonstrating atmospheric physics
- **Mission planning**: Predicting meteor shower observations

## Scientific Accuracy

The model incorporates:
- Realistic atmospheric density profiles
- Velocity-dependent luminous efficiency
- Physical ablation processes
- Gravitational field variations
- Observer distance calculations

## Limitations

- Assumes spherical meteor geometry
- Single-body fragmentation not modeled
- Simplified atmospheric composition
- Fixed drag coefficient throughout entry

---

*This simulation provides a foundation for understanding meteor physics and can be extended with additional atmospheric and fragmentation models for more complex scenarios.*
