"""
Atmospheric calculations based on the International Standard Atmosphere (ISA).

This module provides functions to calculate atmospheric properties
at various altitudes.
"""

import math


# ISA Standard values at sea level
SEA_LEVEL_TEMPERATURE = 288.15  # K (15°C)
SEA_LEVEL_PRESSURE = 101325  # Pa
SEA_LEVEL_DENSITY = 1.225  # kg/m³
TEMPERATURE_LAPSE_RATE = 0.0065  # K/m (troposphere)
GAS_CONSTANT = 287.05  # J/(kg·K) for air
GRAVITY = 9.80665  # m/s²
TROPOSPHERE_HEIGHT = 11000  # m


def temperature_at_altitude(altitude):
    """
    Calculate temperature at a given altitude using ISA model.
    
    Valid for altitudes up to 11,000 meters (troposphere).
    
    Args:
        altitude (float): Altitude in meters above sea level
    
    Returns:
        float: Temperature in Kelvin
    
    Example:
        >>> temperature_at_altitude(0)
        288.15
        >>> round(temperature_at_altitude(1000), 2)
        281.65
    """
    if altitude < 0:
        raise ValueError("Altitude must be non-negative")
    
    if altitude <= TROPOSPHERE_HEIGHT:
        return SEA_LEVEL_TEMPERATURE - TEMPERATURE_LAPSE_RATE * altitude
    else:
        # Stratosphere (constant temperature)
        return SEA_LEVEL_TEMPERATURE - TEMPERATURE_LAPSE_RATE * TROPOSPHERE_HEIGHT


def pressure_at_altitude(altitude):
    """
    Calculate atmospheric pressure at a given altitude using ISA model.
    
    Valid for altitudes up to 11,000 meters (troposphere).
    
    Args:
        altitude (float): Altitude in meters above sea level
    
    Returns:
        float: Pressure in Pascals
    
    Example:
        >>> pressure_at_altitude(0)
        101325
        >>> round(pressure_at_altitude(1000), 2)
        89874.57
    """
    if altitude < 0:
        raise ValueError("Altitude must be non-negative")
    
    if altitude <= TROPOSPHERE_HEIGHT:
        temperature = temperature_at_altitude(altitude)
        exponent = GRAVITY / (TEMPERATURE_LAPSE_RATE * GAS_CONSTANT)
        return SEA_LEVEL_PRESSURE * (temperature / SEA_LEVEL_TEMPERATURE) ** exponent
    else:
        # Stratosphere calculation
        temp_at_tropopause = temperature_at_altitude(TROPOSPHERE_HEIGHT)
        pressure_at_tropopause = pressure_at_altitude(TROPOSPHERE_HEIGHT - 1)
        return pressure_at_tropopause * math.exp(
            -GRAVITY * (altitude - TROPOSPHERE_HEIGHT) / (GAS_CONSTANT * temp_at_tropopause)
        )


def air_density_at_altitude(altitude):
    """
    Calculate air density at a given altitude using ISA model.
    
    Uses the ideal gas law: ρ = P / (R × T)
    
    Args:
        altitude (float): Altitude in meters above sea level
    
    Returns:
        float: Air density in kg/m³
    
    Example:
        >>> air_density_at_altitude(0)
        1.225
        >>> round(air_density_at_altitude(1000), 3)
        1.112
    """
    if altitude < 0:
        raise ValueError("Altitude must be non-negative")
    
    pressure = pressure_at_altitude(altitude)
    temperature = temperature_at_altitude(altitude)
    
    return pressure / (GAS_CONSTANT * temperature)
