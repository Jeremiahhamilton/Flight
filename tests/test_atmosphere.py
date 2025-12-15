"""Tests for atmosphere module."""

import unittest
from flight_math.atmosphere import (
    temperature_at_altitude,
    pressure_at_altitude,
    air_density_at_altitude,
    SEA_LEVEL_TEMPERATURE,
    SEA_LEVEL_PRESSURE,
    SEA_LEVEL_DENSITY
)


class TestAtmosphere(unittest.TestCase):
    """Test cases for atmospheric calculations."""
    
    def test_temperature_at_sea_level(self):
        """Test temperature at sea level."""
        temp = temperature_at_altitude(0)
        self.assertEqual(temp, SEA_LEVEL_TEMPERATURE)
        self.assertAlmostEqual(temp, 288.15, places=2)
    
    def test_temperature_at_1000m(self):
        """Test temperature at 1000m altitude."""
        temp = temperature_at_altitude(1000)
        # Should be approximately 281.65 K (15°C - 6.5°C)
        self.assertAlmostEqual(temp, 281.65, places=1)
    
    def test_temperature_negative_altitude(self):
        """Test that negative altitude raises ValueError."""
        with self.assertRaises(ValueError):
            temperature_at_altitude(-100)
    
    def test_temperature_above_troposphere(self):
        """Test temperature above troposphere."""
        temp = temperature_at_altitude(15000)
        # Should be constant in stratosphere
        self.assertAlmostEqual(temp, 216.65, places=1)
    
    def test_pressure_at_sea_level(self):
        """Test pressure at sea level."""
        pressure = pressure_at_altitude(0)
        self.assertEqual(pressure, SEA_LEVEL_PRESSURE)
    
    def test_pressure_at_1000m(self):
        """Test pressure at 1000m altitude."""
        pressure = pressure_at_altitude(1000)
        # Should be approximately 89874.57 Pa
        self.assertAlmostEqual(pressure, 89874.57, places=0)
    
    def test_pressure_decreases_with_altitude(self):
        """Test that pressure decreases with altitude."""
        p0 = pressure_at_altitude(0)
        p1000 = pressure_at_altitude(1000)
        p5000 = pressure_at_altitude(5000)
        self.assertGreater(p0, p1000)
        self.assertGreater(p1000, p5000)
    
    def test_pressure_negative_altitude(self):
        """Test that negative altitude raises ValueError."""
        with self.assertRaises(ValueError):
            pressure_at_altitude(-100)
    
    def test_air_density_at_sea_level(self):
        """Test air density at sea level."""
        density = air_density_at_altitude(0)
        self.assertAlmostEqual(density, SEA_LEVEL_DENSITY, places=3)
    
    def test_air_density_at_1000m(self):
        """Test air density at 1000m altitude."""
        density = air_density_at_altitude(1000)
        # Should be approximately 1.112 kg/m³
        self.assertAlmostEqual(density, 1.112, places=2)
    
    def test_air_density_decreases_with_altitude(self):
        """Test that air density decreases with altitude."""
        d0 = air_density_at_altitude(0)
        d1000 = air_density_at_altitude(1000)
        d5000 = air_density_at_altitude(5000)
        self.assertGreater(d0, d1000)
        self.assertGreater(d1000, d5000)
    
    def test_air_density_negative_altitude(self):
        """Test that negative altitude raises ValueError."""
        with self.assertRaises(ValueError):
            air_density_at_altitude(-100)


if __name__ == '__main__':
    unittest.main()
