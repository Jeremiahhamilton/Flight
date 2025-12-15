"""
Flight Math Library - Mathematical functions for flight calculations.

This library provides functions for aerodynamics, flight dynamics,
atmospheric calculations, and unit conversions.
"""

from .aerodynamics import calculate_lift, calculate_drag, lift_to_drag_ratio
from .atmosphere import air_density_at_altitude, temperature_at_altitude, pressure_at_altitude
from .flight_dynamics import thrust_to_weight_ratio, rate_of_climb, turn_radius, bank_angle
from .conversions import (
    knots_to_mps,
    mps_to_knots,
    mph_to_mps,
    mps_to_mph,
    feet_to_meters,
    meters_to_feet,
    celsius_to_kelvin,
    kelvin_to_celsius,
)

__version__ = "0.1.0"
__all__ = [
    # Aerodynamics
    "calculate_lift",
    "calculate_drag",
    "lift_to_drag_ratio",
    # Atmosphere
    "air_density_at_altitude",
    "temperature_at_altitude",
    "pressure_at_altitude",
    # Flight Dynamics
    "thrust_to_weight_ratio",
    "rate_of_climb",
    "turn_radius",
    "bank_angle",
    # Conversions
    "knots_to_mps",
    "mps_to_knots",
    "mph_to_mps",
    "mps_to_mph",
    "feet_to_meters",
    "meters_to_feet",
    "celsius_to_kelvin",
    "kelvin_to_celsius",
]
