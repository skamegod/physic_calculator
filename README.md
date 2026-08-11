# Physic Calculator (CLI)

A simple command-line physics calculator that computes common physics formulas.

## Supported formulas
This program can calculate values for the following physics equations:

1.  **Rest energy (Einstein):** E = mc²
2.  **Ohm's law:** I = U / R
3.  **Coulomb's law:** F = kₑ · |q₁ · q₂| / r²
4.  **Newton's law of universal gravitation:** F = G · m₁ · m₂ / r²
5.  **Pressure:** P = F / S
6.  **Density:** ρ = m / V
7.  **Weight (gravitational force):** F = m · g
8.  **Archimedes' force:** Fₐ = ρ · g · V
9.  **Newton's second law:** F = m · a
10. **Acceleration:** a = (v - v₀) / t

## Build and run

### Linux
Make sure `gcc` and `make` are installed, then run:

```bash
make
./physic
```

### Windows
Use the MinGW compiler to build the executable:

```bash
x86_64-w64-mingw32-gcc main.c -o physic.exe -lm -static
```

## Releases
Prebuilt versions are available in the project releases.
