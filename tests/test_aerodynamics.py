"""Tests for aerodynamics module."""

import unittest
import math
from flight_math.aerodynamics import calculate_lift, calculate_drag, lift_to_drag_ratio


class TestAerodynamics(unittest.TestCase):
    """Test cases for aerodynamics calculations."""
    
    def test_calculate_lift_basic(self):
        """Test basic lift calculation."""
        lift = calculate_lift(1.225, 50, 20, 0.5)
        self.assertAlmostEqual(lift, 15312.5, places=1)
    
    def test_calculate_lift_zero_velocity(self):
        """Test lift calculation with zero velocity."""
        lift = calculate_lift(1.225, 0, 20, 0.5)
        self.assertEqual(lift, 0)
    
    def test_calculate_lift_negative_density(self):
        """Test that negative air density raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_lift(-1, 50, 20, 0.5)
    
    def test_calculate_lift_negative_velocity(self):
        """Test that negative velocity raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_lift(1.225, -50, 20, 0.5)
    
    def test_calculate_lift_zero_wing_area(self):
        """Test that zero wing area raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_lift(1.225, 50, 0, 0.5)
    
    def test_calculate_drag_basic(self):
        """Test basic drag calculation."""
        drag = calculate_drag(1.225, 50, 20, 0.05)
        self.assertAlmostEqual(drag, 1531.25, places=1)
    
    def test_calculate_drag_zero_velocity(self):
        """Test drag calculation with zero velocity."""
        drag = calculate_drag(1.225, 0, 20, 0.05)
        self.assertEqual(drag, 0)
    
    def test_calculate_drag_negative_density(self):
        """Test that negative air density raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_drag(-1, 50, 20, 0.05)
    
    def test_lift_to_drag_ratio_basic(self):
        """Test basic L/D ratio calculation."""
        ratio = lift_to_drag_ratio(15312.5, 1531.25)
        self.assertAlmostEqual(ratio, 10.0, places=1)
    
    def test_lift_to_drag_ratio_zero_drag(self):
        """Test that zero drag raises ValueError."""
        with self.assertRaises(ValueError):
            lift_to_drag_ratio(15312.5, 0)
    
    def test_lift_to_drag_ratio_efficient_aircraft(self):
        """Test L/D ratio for efficient aircraft (glider)."""
        # Gliders can have L/D ratios of 40:1 or higher
        ratio = lift_to_drag_ratio(40000, 1000)
        self.assertAlmostEqual(ratio, 40.0, places=1)


if __name__ == '__main__':
    unittest.main()
