#!/usr/bin/env python
"""
Demo script showing usage of the flight_math library.

This script demonstrates various flight calculations using the library.
"""

import flight_math as fm


def print_section(title):
    """Print a section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)


def aerodynamics_demo():
    """Demonstrate aerodynamics calculations."""
    print_section("Aerodynamics Calculations")
    
    # Calculate lift at sea level
    air_density = 1.225  # kg/m³ at sea level
    velocity = 50  # m/s (about 97 knots)
    wing_area = 20  # m²
    lift_coeff = 0.5
    
    lift = fm.calculate_lift(air_density, velocity, wing_area, lift_coeff)
    print(f"\nLift Force:")
    print(f"  Air density: {air_density} kg/m³")
    print(f"  Velocity: {velocity} m/s ({fm.mps_to_knots(velocity):.1f} knots)")
    print(f"  Wing area: {wing_area} m²")
    print(f"  Lift coefficient: {lift_coeff}")
    print(f"  → Lift: {lift:,.1f} N")
    
    # Calculate drag
    drag_coeff = 0.05
    drag = fm.calculate_drag(air_density, velocity, wing_area, drag_coeff)
    print(f"\nDrag Force:")
    print(f"  Drag coefficient: {drag_coeff}")
    print(f"  → Drag: {drag:,.1f} N")
    
    # Calculate L/D ratio
    ld_ratio = fm.lift_to_drag_ratio(lift, drag)
    print(f"\nAerodynamic Efficiency:")
    print(f"  → Lift-to-Drag ratio: {ld_ratio:.1f}")


def atmosphere_demo():
    """Demonstrate atmospheric calculations."""
    print_section("Atmospheric Calculations")
    
    altitudes = [0, 1000, 5000, 10000]  # meters
    
    print(f"\n{'Altitude (m)':>15} {'Altitude (ft)':>15} {'Temp (°C)':>12} {'Pressure (kPa)':>15} {'Density (kg/m³)':>18}")
    print('-' * 80)
    
    for altitude in altitudes:
        temp_k = fm.temperature_at_altitude(altitude)
        temp_c = fm.kelvin_to_celsius(temp_k)
        pressure = fm.pressure_at_altitude(altitude)
        density = fm.air_density_at_altitude(altitude)
        
        print(f"{altitude:>15} {fm.meters_to_feet(altitude):>15.0f} {temp_c:>12.1f} {pressure/1000:>15.2f} {density:>18.3f}")


def flight_dynamics_demo():
    """Demonstrate flight dynamics calculations."""
    print_section("Flight Dynamics")
    
    # Thrust-to-weight ratio
    thrust = 10000  # N
    weight = 8000  # N
    twr = fm.thrust_to_weight_ratio(thrust, weight)
    print(f"\nThrust-to-Weight Ratio:")
    print(f"  Thrust: {thrust:,} N")
    print(f"  Weight: {weight:,} N")
    print(f"  → T/W: {twr:.2f}")
    
    # Rate of climb
    excess_power = 50000  # W
    roc = fm.rate_of_climb(excess_power, weight)
    print(f"\nRate of Climb:")
    print(f"  Excess power: {excess_power:,} W")
    print(f"  Weight: {weight:,} N")
    print(f"  → Rate of climb: {roc:.1f} m/s ({roc * 196.85:.0f} ft/min)")
    
    # Turn performance
    velocity_kt = 100  # knots
    velocity = fm.knots_to_mps(velocity_kt)
    bank_angles = [15, 30, 45, 60]
    
    print(f"\nTurn Performance at {velocity_kt} knots:")
    print(f"{'Bank Angle (°)':>16} {'Turn Radius (m)':>18} {'Turn Radius (ft)':>18}")
    print('-' * 60)
    
    for bank in bank_angles:
        radius_m = fm.turn_radius(velocity, bank)
        radius_ft = fm.meters_to_feet(radius_m)
        print(f"{bank:>16} {radius_m:>18.1f} {radius_ft:>18.0f}")


def conversions_demo():
    """Demonstrate unit conversions."""
    print_section("Unit Conversions")
    
    print("\nSpeed Conversions:")
    knots = 100
    print(f"  {knots} knots = {fm.knots_to_mps(knots):.2f} m/s")
    print(f"  {knots} knots = {fm.knots_to_mps(knots) * 3.6:.2f} km/h")
    
    mph = 100
    print(f"  {mph} mph = {fm.mph_to_mps(mph):.2f} m/s")
    print(f"  {mph} mph = {fm.mps_to_knots(fm.mph_to_mps(mph)):.2f} knots")
    
    print("\nAltitude Conversions:")
    feet = 10000
    print(f"  {feet:,} feet = {fm.feet_to_meters(feet):.1f} meters")
    
    meters = 3048
    print(f"  {meters:,} meters = {fm.meters_to_feet(meters):.0f} feet")
    
    print("\nTemperature Conversions:")
    celsius = 15
    print(f"  {celsius}°C = {fm.celsius_to_kelvin(celsius):.2f} K")
    
    kelvin = 288.15
    print(f"  {kelvin} K = {fm.kelvin_to_celsius(kelvin):.2f}°C")


def main():
    """Run all demonstrations."""
    print("\n" + "="*60)
    print("  FLIGHT MATH LIBRARY - DEMONSTRATION")
    print("="*60)
    
    aerodynamics_demo()
    atmosphere_demo()
    flight_dynamics_demo()
    conversions_demo()
    
    print("\n" + "="*60)
    print("  Demo Complete!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
