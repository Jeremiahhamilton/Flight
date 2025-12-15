"""Tests for flight_dynamics module."""

import unittest
from flight_math.flight_dynamics import (
    thrust_to_weight_ratio,
    rate_of_climb,
    turn_radius,
    bank_angle
)


class TestFlightDynamics(unittest.TestCase):
    """Test cases for flight dynamics calculations."""
    
    def test_thrust_to_weight_ratio_basic(self):
        """Test basic thrust-to-weight ratio."""
        twr = thrust_to_weight_ratio(10000, 8000)
        self.assertAlmostEqual(twr, 1.25, places=2)
    
    def test_thrust_to_weight_ratio_equal(self):
        """Test TWR when thrust equals weight."""
        twr = thrust_to_weight_ratio(10000, 10000)
        self.assertEqual(twr, 1.0)
    
    def test_thrust_to_weight_ratio_zero_weight(self):
        """Test that zero weight raises ValueError."""
        with self.assertRaises(ValueError):
            thrust_to_weight_ratio(10000, 0)
    
    def test_thrust_to_weight_ratio_negative_thrust(self):
        """Test that negative thrust raises ValueError."""
        with self.assertRaises(ValueError):
            thrust_to_weight_ratio(-10000, 8000)
    
    def test_thrust_to_weight_ratio_negative_weight(self):
        """Test that negative weight raises ValueError."""
        with self.assertRaises(ValueError):
            thrust_to_weight_ratio(10000, -8000)
    
    def test_rate_of_climb_basic(self):
        """Test basic rate of climb calculation."""
        roc = rate_of_climb(50000, 10000)
        self.assertAlmostEqual(roc, 5.0, places=1)
    
    def test_rate_of_climb_zero_power(self):
        """Test rate of climb with zero excess power."""
        roc = rate_of_climb(0, 10000)
        self.assertEqual(roc, 0)
    
    def test_rate_of_climb_zero_weight(self):
        """Test that zero weight raises ValueError."""
        with self.assertRaises(ValueError):
            rate_of_climb(50000, 0)
    
    def test_turn_radius_basic(self):
        """Test basic turn radius calculation."""
        radius = turn_radius(50, 30)
        # At 50 m/s and 30° bank, radius should be ~441.55 m
        self.assertAlmostEqual(radius, 441.55, places=1)
    
    def test_turn_radius_steep_bank(self):
        """Test turn radius with steep bank angle."""
        radius = turn_radius(50, 60)
        # Steeper bank = tighter turn
        radius_shallow = turn_radius(50, 30)
        self.assertLess(radius, radius_shallow)
    
    def test_turn_radius_zero_bank(self):
        """Test that zero bank angle raises ValueError."""
        with self.assertRaises(ValueError):
            turn_radius(50, 0)
    
    def test_turn_radius_90_degree_bank(self):
        """Test that 90° bank angle raises ValueError."""
        with self.assertRaises(ValueError):
            turn_radius(50, 90)
    
    def test_turn_radius_negative_velocity(self):
        """Test that negative velocity raises ValueError."""
        with self.assertRaises(ValueError):
            turn_radius(-50, 30)
    
    def test_bank_angle_basic(self):
        """Test basic bank angle calculation."""
        angle = bank_angle(50, 441.55)
        # Should be approximately 30°
        self.assertAlmostEqual(angle, 30.0, places=1)
    
    def test_bank_angle_tight_turn(self):
        """Test bank angle for tight turn."""
        angle_tight = bank_angle(50, 200)
        angle_wide = bank_angle(50, 500)
        # Tighter turn requires steeper bank
        self.assertGreater(angle_tight, angle_wide)
    
    def test_bank_angle_negative_velocity(self):
        """Test that negative velocity raises ValueError."""
        with self.assertRaises(ValueError):
            bank_angle(-50, 436.78)
    
    def test_bank_angle_zero_radius(self):
        """Test that zero turn radius raises ValueError."""
        with self.assertRaises(ValueError):
            bank_angle(50, 0)
    
    def test_turn_radius_and_bank_angle_inverse(self):
        """Test that turn_radius and bank_angle are inverse operations."""
        velocity = 50
        bank_deg = 30
        # Calculate radius from bank angle
        radius = turn_radius(velocity, bank_deg)
        # Calculate bank angle from radius
        calculated_bank = bank_angle(velocity, radius)
        self.assertAlmostEqual(bank_deg, calculated_bank, places=1)


if __name__ == '__main__':
    unittest.main()
