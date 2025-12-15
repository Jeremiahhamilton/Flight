"""
Flight dynamics calculations.

This module provides functions for calculating flight performance
parameters such as thrust-to-weight ratio, rate of climb, and turn performance.
"""

import math


GRAVITY = 9.80665  # m/s²


def thrust_to_weight_ratio(thrust, weight):
    """
    Calculate the thrust-to-weight ratio.
    
    This is a key performance metric for aircraft.
    A ratio > 1 means the aircraft can accelerate vertically.
    
    Args:
        thrust (float): Thrust force in Newtons
        weight (float): Weight in Newtons
    
    Returns:
        float: Thrust-to-weight ratio (dimensionless)
    
    Raises:
        ValueError: If weight is zero
    
    Example:
        >>> thrust_to_weight_ratio(10000, 8000)
        1.25
    """
    if weight == 0:
        raise ValueError("Weight cannot be zero")
    if thrust < 0:
        raise ValueError("Thrust must be non-negative")
    if weight < 0:
        raise ValueError("Weight must be non-negative")
    
    return thrust / weight


def rate_of_climb(excess_power, weight):
    """
    Calculate the rate of climb.
    
    ROC = Excess Power / Weight
    
    Args:
        excess_power (float): Excess power available in Watts
        weight (float): Weight in Newtons
    
    Returns:
        float: Rate of climb in m/s
    
    Example:
        >>> rate_of_climb(50000, 10000)
        5.0
    """
    if weight == 0:
        raise ValueError("Weight cannot be zero")
    if weight < 0:
        raise ValueError("Weight must be non-negative")
    
    return excess_power / weight


def turn_radius(velocity, bank_angle_deg):
    """
    Calculate the turn radius for a coordinated turn.
    
    R = V² / (g × tan(φ))
    
    Args:
        velocity (float): Airspeed in m/s
        bank_angle_deg (float): Bank angle in degrees
    
    Returns:
        float: Turn radius in meters
    
    Example:
        >>> round(turn_radius(50, 30), 2)
        436.78
    """
    if velocity < 0:
        raise ValueError("Velocity must be non-negative")
    if bank_angle_deg <= 0 or bank_angle_deg >= 90:
        raise ValueError("Bank angle must be between 0 and 90 degrees (exclusive)")
    
    bank_angle_rad = math.radians(bank_angle_deg)
    return velocity ** 2 / (GRAVITY * math.tan(bank_angle_rad))


def bank_angle(velocity, turn_radius_m):
    """
    Calculate the required bank angle for a coordinated turn.
    
    φ = arctan(V² / (g × R))
    
    Args:
        velocity (float): Airspeed in m/s
        turn_radius_m (float): Desired turn radius in meters
    
    Returns:
        float: Bank angle in degrees
    
    Example:
        >>> round(bank_angle(50, 436.78), 2)
        30.0
    """
    if velocity < 0:
        raise ValueError("Velocity must be non-negative")
    if turn_radius_m <= 0:
        raise ValueError("Turn radius must be positive")
    
    angle_rad = math.atan(velocity ** 2 / (GRAVITY * turn_radius_m))
    return math.degrees(angle_rad)
