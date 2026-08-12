speed_light = 299792458  # Speed of light in meters per second
k_e = 8.9875517873681764e9  # Coulomb's constant in N·m²/C²
g = 9.80665  # Acceleration due to gravity in m/s²
g_e = 9.81  # Standard gravity in m/s²
G = 6.67430e-11  # Gravitational constant in N·m²/kg²

def formula_epstein():
    m = float(input("Enter mass (in kg): "))
    E = m * speed_light ** 2
    print(f"Energy (E) = {E} Joules")

def Ohm_Law():
    I = float(input("Enter current (in Amperes): "))
    R = float(input("Enter resistance (in Ohms): "))
    V = I * R
    print(f"Voltage (V) = {V} Volts")

def 