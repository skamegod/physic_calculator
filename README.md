# Physic Calculator (CLI)

A simple physics calculator with both C and Python command-line versions.

## Project versions

- `c_version/` — the original C implementation with 10 physics formulas.
- `python_version/` — a Python implementation with more menu options and additional formulas.

## Supported formulas

### Common formulas in both versions

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

### Additional formulas in the Python version

11. **Impulse:** J = m · Δv
12. **Moment of force:** M = F · d

## Build and run

### C version (Linux)
Make sure `gcc` and `make` are installed, then run:

```bash
cd c_version
make
./physic
```

### C version (Windows)
Use the MinGW compiler to build the executable:

```bash
cd c_version
x86_64-w64-mingw32-gcc main.c -o physic.exe -lm -static
```

### Python version
Run the Python calculator with:

```bash
python3 python_version/main.py
```

## Notes

- The Python version includes extra physics options beyond the original C menu.
- Both implementations are command-line applications.

## Releases
Prebuilt versions are available in the project releases.
