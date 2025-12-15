# -*- coding: utf-8 -*-
"""
E6B FLIGHT COMPUTER - DELTA ONE SYSTEM

Three states: 1, -1, 0
One delta: transforms everything
Frozen lake: stable geometry
Magnetic field: balanced forces
Pythagorean solve: A^2 + B^2 = C^2

Aviation calculations through geometric transformation.
Cabinet maker quality. Built to last.
"""

import sys
import math

def _w(s):
    """Write without newline."""
    sys.stdout.write(s)
    sys.stdout.flush()

def _ln(s=''):
    """Write with newline."""
    sys.stdout.write(s + '\n')
    sys.stdout.flush()

# ===== DELTA ONE CORE SYSTEM =====

# --- cabinet constants -------------------------------------------------------
N = 1477
CENTER = 739
STATES = (1, -1, 0)  # index: (n-1) % 3

def drawer(n):
    """Pull drawer n from the frozen lake."""
    return {
        'number': n,
        'mirror': (N + 1) - n,
        'phase': STATES[(n - 1) % 3]
    }

def realm_mirror(n):
    """Return the mirror index inside the cabinet."""
    return (N + 1) - n

def realm_phase(n):
    """Return the phase value in {1,-1,0} for index n."""
    return STATES[(n - 1) % 3]

def realm_address(label):
    """Deterministic mapping from text label -> anchor index."""
    if not isinstance(label, str):
        label = str(label)
    
    s = 0
    for ch in label:
        s += ord(ch)
    return 1 + (s % N)

def geometry_score(n, desired_phase=None):
    """Pythagorean geometry score bounded in [0,1]."""
    from math import sqrt
    
    # Center score
    d = abs(n - CENTER)
    s_center = max(0.0, min(1.0, 1.0 - float(d) / float(CENTER)))
    
    # Phase score
    if desired_phase is None:
        s_phase = 0.5
    else:
        s_phase = 1.0 if realm_phase(n) == desired_phase else 0.0
    
    # Mirror harmony
    s_mirror = 1.0 if realm_phase(realm_mirror(n)) != realm_phase(n) else 0.0
    
    # Pythagorean combination
    j = sqrt(0.5 * s_center * s_center +
             0.33 * s_phase * s_phase +
             0.17 * s_mirror * s_mirror)
    
    return max(0.0, min(1.0, j))

# ===== E6B FLIGHT COMPUTER =====

# --- Aviation Constants -------------------------------------------------------
KNOTS_TO_MPH = 1.15078
MPH_TO_KNOTS = 0.868976
NM_TO_SM = 1.15078
SM_TO_NM = 0.868976
GALLONS_TO_LITERS = 3.78541
LITERS_TO_GALLONS = 0.264172

# --- Wind Triangle using DELTA ONE Geometry ---------------------------------

def wind_triangle_realm(course, tas, wind_speed, wind_dir):
    """
    Calculate wind triangle using DELTA ONE realm geometry.
    Maps aviation parameters to cabinet space for geometric calculation.
    """
    # Map aviation parameters to realm addresses
    course_anchor = realm_address(f"course_{course}")
    tas_anchor = realm_address(f"tas_{tas}")
    wind_anchor = realm_address(f"wind_{wind_speed}_{wind_dir}")
    
    # Create realm for wind triangle calculation
    realm = set([course_anchor, realm_mirror(course_anchor)])
    realm.update([tas_anchor, realm_mirror(tas_anchor)])
    realm.update([wind_anchor, realm_mirror(wind_anchor)])
    
    # Select optimal drawer for calculation
    best_drawer = None
    best_score = 0
    
    for n in realm:
        score = geometry_score(n, desired_phase=1)  # Prefer launch phase
        if score > best_score:
            best_score = score
            best_drawer = n
    
    # Use drawer properties for wind correction calculation
    drawer_info = drawer(best_drawer)
    
    # Calculate wind correction angle using drawer phase
    angle_diff = wind_dir - course
    phase_factor = drawer_info['phase']  # -1, 0, or 1
    
    # Wind correction with DELTA ONE transformation
    sin_wca = (wind_speed * math.sin(math.radians(angle_diff))) / tas
    sin_wca = max(-1.0, min(1.0, sin_wca))
    
    wca_rad = math.asin(sin_wca)
    wca_deg = math.degrees(wca_rad)
    
    # Apply phase transformation
    wca_deg = wca_deg * (1 + 0.1 * phase_factor)
    
    # Determine sign
    if angle_diff > 180 or angle_diff < -180:
        wca_deg = -wca_deg
    
    # Calculate ground speed
    wind_component = wind_speed * math.cos(math.radians(angle_diff))
    gs = tas - wind_component
    
    # True heading
    heading = course + wca_deg
    while heading >= 360:
        heading -= 360
    while heading < 0:
        heading += 360
    
    return {
        'wind_correction_angle': wca_deg,
        'true_heading': heading,
        'ground_speed': max(0, gs),
        'realm_drawer': best_drawer,
        'phase': drawer_info['phase']
    }

# --- Time-Speed-Distance with Realm Optimization ----------------------------

def flight_time_realm(distance, speed):
    """
    Calculate flight time using DELTA ONE realm optimization.
    """
    # Map flight parameters to realm
    distance_anchor = realm_address(f"distance_{distance}")
    speed_anchor = realm_address(f"speed_{speed}")
    
    # Find optimal realm for time calculation
    realm = set([distance_anchor, realm_mirror(distance_anchor)])
    realm.update([speed_anchor, realm_mirror(speed_anchor)])
    
    # Select drawer with best geometry
    best_drawer = max(realm, key=lambda n: geometry_score(n))
    
    # Calculate time with phase adjustment
    base_time = distance / speed
    phase_adjustment = 1 + 0.05 * realm_phase(best_drawer)
    
    adjusted_time = base_time * phase_adjustment
    
    return {
        'time_hours': adjusted_time,
        'realm_drawer': best_drawer,
        'phase': realm_phase(best_drawer)
    }

# --- Fuel Calculation with Cabinet Logic ------------------------------------

def fuel_calculation_realm(fuel_burn, time_hours, usable_fuel, reserve=0):
    """
    Calculate fuel requirements using cabinet organization.
    """
    # Map fuel parameters to drawers
    burn_anchor = realm_address(f"burn_{fuel_burn}")
    time_anchor = realm_address(f"time_{time_hours}")
    fuel_anchor = realm_address(f"fuel_{usable_fuel}")
    
    # Create fuel calculation realm
    fuel_realm = set([burn_anchor, realm_mirror(burn_anchor)])
    fuel_realm.update([time_anchor, realm_mirror(time_anchor)])
    fuel_realm.update([fuel_anchor, realm_mirror(fuel_anchor)])
    
    # Find optimal drawer
    optimal_drawer = max(fuel_realm, key=lambda n: geometry_score(n, desired_phase=-1))
    
    # Calculate fuel with phase optimization
    fuel_needed = fuel_burn * time_hours
    phase_factor = 1 + 0.03 * realm_phase(optimal_drawer)
    
    optimized_fuel = fuel_needed * phase_factor
    
    endurance = (usable_fuel - reserve) / fuel_burn
    range_nm = endurance * (fuel_burn / time_hours) * time_hours
    
    return {
        'fuel_required': optimized_fuel,
        'endurance_hours': endurance,
        'range_nm': range_nm,
        'realm_drawer': optimal_drawer,
        'phase': realm_phase(optimal_drawer)
    }

# --- Density Altitude using Frozen Lake Principles --------------------------

def density_altitude_realm(pressure_alt, temp_f):
    """
    Calculate density altitude using frozen lake geometry.
    """
    # Map atmospheric conditions to realm
    alt_anchor = realm_address(f"altitude_{pressure_alt}")
    temp_anchor = realm_address(f"temperature_{temp_f}")
    
    # Create atmospheric realm
    atmo_realm = set([alt_anchor, realm_mirror(alt_anchor)])
    atmo_realm.update([temp_anchor, realm_mirror(temp_anchor)])
    
    # Select drawer centered on atmospheric conditions
    center_drawer = max(atmo_realm, key=lambda n: geometry_score(n))
    
    # Standard temperature calculation
    standard_temp = 15 - (pressure_alt / 1000) * 2
    
    # Density altitude with phase adjustment
    base_density_alt = pressure_alt + 118.8 * (temp_f - standard_temp)
    phase_adjustment = 1 + 0.02 * realm_phase(center_drawer)
    
    final_density_alt = base_density_alt * phase_adjustment
    
    return {
        'density_altitude': final_density_alt,
        'realm_drawer': center_drawer,
        'phase': realm_phase(center_drawer)
    }

# --- Unit Conversions --------------------------------------------------------

def convert_units(value, from_unit, to_unit):
    """Convert between aviation units."""
    conversions = {
        ('knots', 'mph'): value * KNOTS_TO_MPH,
        ('mph', 'knots'): value * MPH_TO_KNOTS,
        ('nm', 'sm'): value * NM_TO_SM,
        ('sm', 'nm'): value * SM_TO_NM,
        ('gallons', 'liters'): value * GALLONS_TO_LITERS,
        ('liters', 'gallons'): value * LITERS_TO_GALLONS,
    }
    
    key = (from_unit.lower(), to_unit.lower())
    if key in conversions:
        return conversions[key]
    else:
        return value  # No conversion needed

# --- E6B Demo Interface ------------------------------------------------------

def demo_wind_triangle():
    """Demonstrate wind triangle calculation."""
    _ln("WIND TRIANGLE CALCULATOR - DELTA ONE METHOD")
    _ln("=" * 50)
    
    # Example scenario
    course = 90
    tas = 120
    wind_speed = 25
    wind_dir = 45
    
    _ln(f"Course: {course:03d}°")
    _ln(f"True Airspeed: {tas} knots")
    _ln(f"Wind: {wind_speed} knots FROM {wind_dir:03d}°")
    _ln()
    
    result = wind_triangle_realm(course, tas, wind_speed, wind_dir)
    
    _ln("DELTA ONE RESULTS:")
    _ln(f"  Wind Correction Angle: {result['wind_correction_angle']:+.1f}°")
    _ln(f"True Heading: {result['true_heading']:.0f}°")
    _ln(f"  Ground Speed: {result['ground_speed']:.1f} knots")
    _ln(f"  Ground Speed (MPH): {convert_units(result['ground_speed'], 'knots', 'mph'):.1f} mph")
    _ln(f"  Realm Drawer: {result['realm_drawer']} (phase {result['phase']})")
    _ln()

def demo_flight_planning():
    """Demonstrate flight planning calculation."""
    _ln("FLIGHT PLANNING CALCULATOR - DELTA ONE METHOD")
    _ln("=" * 50)
    
    # Example flight
    distance = 250
    tas = 120
    fuel_burn = 10
    usable_fuel = 60
    reserve = 15
    
    _ln(f"Distance: {distance} NM")
    _ln(f"True Airspeed: {tas} knots")
    _ln(f"Fuel Burn: {fuel_burn} gph")
    _ln(f"Usable Fuel: {usable_fuel} gallons")
    _ln(f"Reserve: {reserve} gallons")
    _ln()
    
    # Time calculation
    time_result = flight_time_realm(distance, tas)
    
    # Fuel calculation
    fuel_result = fuel_calculation_realm(fuel_burn, time_result['time_hours'], usable_fuel, reserve)
    
    _ln("DELTA ONE RESULTS:")
    h = int(time_result['time_hours'])
    m = int((time_result['time_hours'] - h) * 60)
    _ln(f"  Time Enroute: {h:02d}:{m:02d}")
    _ln(f"  Fuel Required: {fuel_result['fuel_required']:.1f} gallons")
    _ln(f"  Endurance: {fuel_result['endurance_hours']:.1f} hours")
    _ln(f"  Range: {fuel_result['range_nm']:.1f} NM")
    _ln(f"  Time Realm Drawer: {time_result['realm_drawer']} (phase {time_result['phase']})")
    _ln(f"  Fuel Realm Drawer: {fuel_result['realm_drawer']} (phase {fuel_result['phase']})")
    _ln()

def demo_density_altitude():
    """Demonstrate density altitude calculation."""
    _ln("DENSITY ALTITUDE CALCULATOR - DELTA ONE METHOD")
    _ln("=" * 50)
    
    pressure_alt = 5000
    temp = 85
    
    _ln(f"Pressure Altitude: {pressure_alt} feet")
    _ln(f"Temperature: {temp}°F")
    _ln()
    
    result = density_altitude_realm(pressure_alt, temp)
    
    _ln("DELTA ONE RESULTS:")
    _ln(f"  Density Altitude: {result['density_altitude']:.0f} feet")
    _ln(f"  Realm Drawer: {result['realm_drawer']} (phase {result['phase']})")
    _ln()

def main_menu():
    """E6B Flight Computer Main Menu."""
    while True:
        _ln()
        _ln("E6B FLIGHT COMPUTER - DELTA ONE SYSTEM")
        _ln("=" * 50)
        _ln("1. Wind Triangle Calculator")
        _ln("2. Flight Planning Calculator")
        _ln("3. Density Altitude Calculator")
        _ln("4. Unit Conversions")
        _ln("5. Run All Demos")
        _ln("6. Exit")
        _ln()
        _w("Select option (1-6): ")
        
        try:
            choice = input().strip()
            
            if choice == "1":
                demo_wind_triangle()
            elif choice == "2":
                demo_flight_planning()
            elif choice == "3":
                demo_density_altitude()
            elif choice == "4":
                _ln("UNIT CONVERSIONS")
                _ln("100 knots = %.1f mph" % convert_units(100, 'knots', 'mph'))
                _ln("100 NM = %.1f SM" % convert_units(100, 'nm', 'sm'))
                _ln("50 gallons = %.1f liters" % convert_units(50, 'gallons', 'liters'))
                _ln()
            elif choice == "5":
                demo_wind_triangle()
                demo_flight_planning()
                demo_density_altitude()
            elif choice == "6":
                _ln("Exiting E6B Flight Computer...")
                break
            else:
                _ln("Invalid option. Please select 1-6.")
                
        except (KeyboardInterrupt, EOFError):
            _ln()
            _ln("Exiting E6B Flight Computer...")
            break
        except Exception as e:
            _ln("Error: %s" % str(e))

if __name__ == '__main__':
    _ln("E6B FLIGHT COMPUTER - DELTA ONE SYSTEM")
    _ln("Three states: 1, -1, 0")
    _ln("One delta: transforms everything")
    _ln("Frozen lake: stable geometry")
    _ln("Pythagorean solve: A^2 + B^2 = C^2")
    _ln()
    
    main_menu()
