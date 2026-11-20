speed_light = 299792458  # Speed of light in meters per second
k_e = 8.9875517873681764e9  # Coulomb's constant in N·m²/C²
g = 9.80665  # Acceleration due to gravity in m/s²
g_e = 9.81  # Standard gravity in m/s²
G = 6.67430e-11  # Gravitational constant in N·m²/kg²


def main():
    while True:
        print('''
==== Menu ====
1. Einstein's mass-energy equivalence: E = mc²
2. Ohm's Law: V = IR
3. Coulomb's Law: F = k_e * (q1 * q2) / r²
4. Law of Universal Gravitation: F = G * (m1 * m2) / r²
5. Pressure: P = F / S
6. Density: ρ = m / V
7. Gravity Force: F = m * g
8. Archimedes' Force: F = ρ * V * g
9. Newton's Second Law: F = m * a
10. Acceleration: a = (v - u) / t
11. Impulse body: J = Δp = m * Δv
12. Moment of force: M = F * d
13. Average speed: v = s / t
14. Exit
================''')

        try:
            choice = int(input("Enter your choice (1-14): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 14.")
            continue

        try:
            if choice == 1:
                m = float(input("Enter mass (in kg): "))
                E = m * speed_light ** 2
                print(f"Energy (E) = {E} Joules")
            elif choice == 2:
                I = float(input("Enter current (in Amperes): "))
                R = float(input("Enter resistance (in Ohms): "))
                V = I * R
                print(f"Voltage (V) = {V} Volts")
            elif choice == 3:
                q1 = float(input("Enter charge 1 (in Coulombs): "))
                q2 = float(input("Enter charge 2 (in Coulombs): "))
                r = float(input("Enter distance between charges (in meters): "))
                if r == 0:
                    print("Error: Distance cannot be zero.")
                else:
                    F = k_e * (q1 * q2) / (r ** 2)
                    print(f"Force (F) = {F} Newtons")
            elif choice == 4:
                m1 = float(input("Enter mass 1 (in kg): "))
                m2 = float(input("Enter mass 2 (in kg): "))
                r = float(input("Enter distance between masses (in meters): "))
                if r == 0:
                    print("Error: Distance cannot be zero.")
                else:
                    F = G * (m1 * m2) / (r ** 2)
                    print(f"Gravitational Force (F) = {F} Newtons")
            elif choice == 5:
                F = float(input("Enter force (in Newtons): "))
                S = float(input("Enter area (in square meters): "))
                if S == 0:
                    print("Error: Area cannot be zero.")
                else:
                    P = F / S
                    print(f"Pressure (P) = {P} Pascals")
            elif choice == 6:
                m = float(input("Enter mass (in kg): "))
                V = float(input("Enter volume (in cubic meters): "))
                if V == 0:
                    print("Error: Volume cannot be zero.")
                else:
                    density = m / V
                    print(f"Density (ρ) = {density} kg/m³")
            elif choice == 7:
                m = float(input("Enter mass (in kg): "))
                F = m * g
                print(f"Gravity Force (F) = {F} Newtons")
            elif choice == 8:
                density = float(input("Enter fluid density (in kg/m³): "))
                V = float(input("Enter volume of displaced fluid (in cubic meters): "))
                F = density * V * g
                print(f"Archimedes' Force (F) = {F} Newtons")
            elif choice == 9:
                m = float(input("Enter mass (in kg): "))
                a = float(input("Enter acceleration (in m/s²): "))
                F = m * a
                print(f"Force (F) = {F} Newtons")
            elif choice == 10:
                v = float(input("Enter final velocity (in m/s): "))
                u = float(input("Enter initial velocity (in m/s): "))
                t = float(input("Enter time (in seconds): "))
                if t == 0:
                    print("Error: Time cannot be zero.")
                else:
                    a = (v - u) / t
                    print(f"Acceleration (a) = {a} m/s²")
            elif choice == 11:
                m = float(input("Enter mass (in kg): "))
                v = float(input("Enter final velocity (in m/s): "))
                u = float(input("Enter initial velocity (in m/s): "))
                J = m * (v - u)
                print(f"Impulse (J) = {J} N·s")
            elif choice == 12:
                F = float(input("Enter force (in Newtons): "))
                d = float(input("Enter perpendicular distance (in meters): "))
                M = F * d
                print(f"Moment of force (M) = {M} N·m")
            elif choice == 13:
                s = float(input("Enter distance (in meters): "))
                t = float(input("Enter time (in seconds): "))
                if t == 0:
                    print("Error: Time cannot be zero.")
                else:
                    v = s / t
                    print(f"Average speed (v) = {v} m/s")
            elif choice == 14:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 14.")
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")


if __name__ == "__main__":
    main()
