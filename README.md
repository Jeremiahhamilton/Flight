# Flight Math Library

**Math that will help us fly!**

A comprehensive Python library for flight-related mathematical calculations, including aerodynamics, atmospheric modeling, flight dynamics, and unit conversions.

## Features

### 🛩️ Aerodynamics
- **Lift Calculation**: Calculate lift force using the lift equation (L = 0.5 × ρ × V² × S × CL)
- **Drag Calculation**: Calculate drag force using the drag equation (D = 0.5 × ρ × V² × S × CD)
- **Lift-to-Drag Ratio**: Measure aerodynamic efficiency (L/D)

### 🌍 Atmospheric Calculations
- **Temperature at Altitude**: ISA (International Standard Atmosphere) model
- **Pressure at Altitude**: Atmospheric pressure calculations
- **Air Density at Altitude**: Density calculations using ideal gas law

### ✈️ Flight Dynamics
- **Thrust-to-Weight Ratio**: Key performance metric for aircraft
- **Rate of Climb**: Calculate vertical speed capability
- **Turn Radius**: Calculate turn radius for coordinated turns
- **Bank Angle**: Determine required bank angle for turns

### 🔄 Unit Conversions
- **Speed**: Knots ↔ m/s ↔ mph
- **Altitude**: Feet ↔ meters
- **Temperature**: Celsius ↔ Kelvin

## Installation

```bash
# Clone the repository
git clone https://github.com/Jeremiahhamilton/Flight.git
cd Flight

# Add to your Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## Quick Start

```python
import flight_math as fm

# Calculate lift at sea level
lift = fm.calculate_lift(
    air_density=1.225,  # kg/m³
    velocity=50,        # m/s
    wing_area=20,       # m²
    lift_coefficient=0.5
)
print(f"Lift: {lift:,.1f} N")  # Lift: 15,312.5 N

# Calculate air density at altitude
density = fm.air_density_at_altitude(5000)  # 5000 meters
print(f"Density at 5000m: {density:.3f} kg/m³")  # 0.736 kg/m³

# Convert units
knots = 100
mps = fm.knots_to_mps(knots)
print(f"{knots} knots = {mps:.2f} m/s")  # 100 knots = 51.44 m/s
```

## Examples

Run the comprehensive demonstration:

```bash
cd Flight
PYTHONPATH=. python examples/demo.py
```

## API Reference

### Aerodynamics Module

#### `calculate_lift(air_density, velocity, wing_area, lift_coefficient)`
Calculate lift force in Newtons.

**Parameters:**
- `air_density` (float): Air density in kg/m³
- `velocity` (float): Airspeed in m/s
- `wing_area` (float): Wing reference area in m²
- `lift_coefficient` (float): Coefficient of lift (dimensionless)

**Returns:** Lift force in Newtons

#### `calculate_drag(air_density, velocity, reference_area, drag_coefficient)`
Calculate drag force in Newtons.

#### `lift_to_drag_ratio(lift, drag)`
Calculate the lift-to-drag ratio (aerodynamic efficiency).

### Atmosphere Module

#### `temperature_at_altitude(altitude)`
Calculate temperature at altitude using ISA model. Returns temperature in Kelvin.

#### `pressure_at_altitude(altitude)`
Calculate atmospheric pressure at altitude. Returns pressure in Pascals.

#### `air_density_at_altitude(altitude)`
Calculate air density at altitude. Returns density in kg/m³.

### Flight Dynamics Module

#### `thrust_to_weight_ratio(thrust, weight)`
Calculate thrust-to-weight ratio (dimensionless).

#### `rate_of_climb(excess_power, weight)`
Calculate rate of climb in m/s.

#### `turn_radius(velocity, bank_angle_deg)`
Calculate turn radius in meters for a given velocity and bank angle.

#### `bank_angle(velocity, turn_radius_m)`
Calculate required bank angle in degrees for a given velocity and turn radius.

### Conversions Module

- `knots_to_mps(knots)` / `mps_to_knots(mps)`
- `mph_to_mps(mph)` / `mps_to_mph(mps)`
- `feet_to_meters(feet)` / `meters_to_feet(meters)`
- `celsius_to_kelvin(celsius)` / `kelvin_to_celsius(kelvin)`

## Testing

Run the test suite:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

All 55 tests should pass successfully.

## Use Cases

- **Flight Simulation**: Calculate realistic aerodynamic forces
- **Aircraft Design**: Evaluate performance characteristics
- **Flight Planning**: Calculate fuel requirements and performance
- **Education**: Learn and teach flight mechanics and aerodynamics
- **Drone Development**: Calculate flight parameters for UAVs

## Technical Notes

- All calculations use SI units (meters, kilograms, seconds, Newtons, Pascals)
- Atmospheric calculations based on International Standard Atmosphere (ISA) model
- Valid for altitudes up to ~11,000 meters (troposphere) with simplified stratosphere handling
- Standard gravity: 9.80665 m/s²
- Gas constant for air: 287.05 J/(kg·K)

## License

MIT License - See LICENSE file for details.

Copyright (c) 2025 Jeremiah Hamilton

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Cybernetic Entity Flight Parts

Part of the Flight project for building cybernetic entity flight systems.
