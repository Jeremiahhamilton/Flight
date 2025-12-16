"""
Unit conversion utilities for aviation.

This module provides functions to convert between different units
commonly used in aviation and aeronautics.
"""


# Speed conversion constants
KNOTS_TO_MPS = 0.514444
MPS_TO_KNOTS = 1.94384
MPH_TO_MPS = 0.44704
MPS_TO_MPH = 2.23694

# Length conversion constants
FEET_TO_METERS = 0.3048
METERS_TO_FEET = 3.28084


def knots_to_mps(knots):
    """
    Convert speed from knots to meters per second.
    
    Args:
        knots (float): Speed in knots
    
    Returns:
        float: Speed in meters per second
    
    Example:
        >>> round(knots_to_mps(100), 2)
        51.44
    """
    return knots * KNOTS_TO_MPS


def mps_to_knots(mps):
    """
    Convert speed from meters per second to knots.
    
    Args:
        mps (float): Speed in meters per second
    
    Returns:
        float: Speed in knots
    
    Example:
        >>> round(mps_to_knots(51.44), 2)
        100.0
    """
    return mps * MPS_TO_KNOTS


def mph_to_mps(mph):
    """
    Convert speed from miles per hour to meters per second.
    
    Args:
        mph (float): Speed in miles per hour
    
    Returns:
        float: Speed in meters per second
    
    Example:
        >>> round(mph_to_mps(100), 2)
        44.7
    """
    return mph * MPH_TO_MPS


def mps_to_mph(mps):
    """
    Convert speed from meters per second to miles per hour.
    
    Args:
        mps (float): Speed in meters per second
    
    Returns:
        float: Speed in miles per hour
    
    Example:
        >>> round(mps_to_mph(44.7), 2)
        99.99
    """
    return mps * MPS_TO_MPH


def feet_to_meters(feet):
    """
    Convert length from feet to meters.
    
    Args:
        feet (float): Length in feet
    
    Returns:
        float: Length in meters
    
    Example:
        >>> round(feet_to_meters(1000), 2)
        304.8
    """
    return feet * FEET_TO_METERS


def meters_to_feet(meters):
    """
    Convert length from meters to feet.
    
    Args:
        meters (float): Length in meters
    
    Returns:
        float: Length in feet
    
    Example:
        >>> round(meters_to_feet(304.8), 2)
        1000.0
    """
    return meters * METERS_TO_FEET


def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Kelvin
    
    Example:
        >>> celsius_to_kelvin(15)
        288.15
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    
    Args:
        kelvin (float): Temperature in Kelvin
    
    Returns:
        float: Temperature in Celsius
    
    Example:
        >>> kelvin_to_celsius(288.15)
        15.0
    """
    return kelvin - 273.15
