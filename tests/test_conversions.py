"""Tests for conversions module."""

import unittest
from flight_math.conversions import (
    knots_to_mps,
    mps_to_knots,
    mph_to_mps,
    mps_to_mph,
    feet_to_meters,
    meters_to_feet,
    celsius_to_kelvin,
    kelvin_to_celsius
)


class TestConversions(unittest.TestCase):
    """Test cases for unit conversions."""
    
    def test_knots_to_mps(self):
        """Test knots to m/s conversion."""
        result = knots_to_mps(100)
        self.assertAlmostEqual(result, 51.44, places=1)
    
    def test_mps_to_knots(self):
        """Test m/s to knots conversion."""
        result = mps_to_knots(51.44)
        self.assertAlmostEqual(result, 100.0, places=1)
    
    def test_knots_mps_roundtrip(self):
        """Test that knots <-> m/s conversions are inverse."""
        original = 100
        converted = mps_to_knots(knots_to_mps(original))
        self.assertAlmostEqual(converted, original, places=1)
    
    def test_mph_to_mps(self):
        """Test mph to m/s conversion."""
        result = mph_to_mps(100)
        self.assertAlmostEqual(result, 44.7, places=1)
    
    def test_mps_to_mph(self):
        """Test m/s to mph conversion."""
        result = mps_to_mph(44.7)
        self.assertAlmostEqual(result, 100.0, places=1)
    
    def test_mph_mps_roundtrip(self):
        """Test that mph <-> m/s conversions are inverse."""
        original = 100
        converted = mps_to_mph(mph_to_mps(original))
        self.assertAlmostEqual(converted, original, places=1)
    
    def test_feet_to_meters(self):
        """Test feet to meters conversion."""
        result = feet_to_meters(1000)
        self.assertAlmostEqual(result, 304.8, places=1)
    
    def test_meters_to_feet(self):
        """Test meters to feet conversion."""
        result = meters_to_feet(304.8)
        self.assertAlmostEqual(result, 1000.0, places=1)
    
    def test_feet_meters_roundtrip(self):
        """Test that feet <-> meters conversions are inverse."""
        original = 1000
        converted = meters_to_feet(feet_to_meters(original))
        self.assertAlmostEqual(converted, original, places=1)
    
    def test_celsius_to_kelvin(self):
        """Test Celsius to Kelvin conversion."""
        result = celsius_to_kelvin(15)
        self.assertAlmostEqual(result, 288.15, places=2)
    
    def test_kelvin_to_celsius(self):
        """Test Kelvin to Celsius conversion."""
        result = kelvin_to_celsius(288.15)
        self.assertAlmostEqual(result, 15.0, places=2)
    
    def test_celsius_kelvin_roundtrip(self):
        """Test that Celsius <-> Kelvin conversions are inverse."""
        original = 15
        converted = kelvin_to_celsius(celsius_to_kelvin(original))
        self.assertAlmostEqual(converted, original, places=2)
    
    def test_zero_celsius_to_kelvin(self):
        """Test conversion of 0°C to Kelvin."""
        result = celsius_to_kelvin(0)
        self.assertAlmostEqual(result, 273.15, places=2)
    
    def test_absolute_zero(self):
        """Test conversion of absolute zero."""
        result = kelvin_to_celsius(0)
        self.assertAlmostEqual(result, -273.15, places=2)


if __name__ == '__main__':
    unittest.main()
