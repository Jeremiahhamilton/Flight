"""
Aerodynamics calculations for flight.

This module provides functions to calculate lift, drag, and other
aerodynamic properties essential for flight.
"""

import math


def calculate_lift(air_density, velocity, wing_area, lift_coefficient):
    """
    Calculate lift force using the lift equation.
    
    L = 0.5 × ρ × V² × S × CL
    
    Args:
        air_density (float): Air density in kg/m³
        velocity (float): Airspeed in m/s
        wing_area (float): Wing reference area in m²
        lift_coefficient (float): Coefficient of lift (dimensionless)
    
    Returns:
        float: Lift force in Newtons
    
    Example:
        >>> calculate_lift(1.225, 50, 20, 0.5)
        15312.5
    """
    if air_density < 0:
        raise ValueError("Air density must be non-negative")
    if velocity < 0:
        raise ValueError("Velocity must be non-negative")
    if wing_area <= 0:
        raise ValueError("Wing area must be positive")
    
    return 0.5 * air_density * velocity ** 2 * wing_area * lift_coefficient


def calculate_drag(air_density, velocity, reference_area, drag_coefficient):
    """
    Calculate drag force using the drag equation.
    
    D = 0.5 × ρ × V² × S × CD
    
    Args:
        air_density (float): Air density in kg/m³
        velocity (float): Airspeed in m/s
        reference_area (float): Reference area in m²
        drag_coefficient (float): Coefficient of drag (dimensionless)
    
    Returns:
        float: Drag force in Newtons
    
    Example:
        >>> calculate_drag(1.225, 50, 20, 0.05)
        1531.25
    """
    if air_density < 0:
        raise ValueError("Air density must be non-negative")
    if velocity < 0:
        raise ValueError("Velocity must be non-negative")
    if reference_area <= 0:
        raise ValueError("Reference area must be positive")
    
    return 0.5 * air_density * velocity ** 2 * reference_area * drag_coefficient


def lift_to_drag_ratio(lift, drag):
    """
    Calculate the lift-to-drag ratio (L/D).
    
    This is a measure of aerodynamic efficiency.
    
    Args:
        lift (float): Lift force in Newtons
        drag (float): Drag force in Newtons
    
    Returns:
        float: Lift-to-drag ratio (dimensionless)
    
    Raises:
        ValueError: If drag is zero
    
    Example:
        >>> lift_to_drag_ratio(15312.5, 1531.25)
        10.0
    """
    if drag == 0:
        raise ValueError("Drag cannot be zero")
    
    return lift / drag
