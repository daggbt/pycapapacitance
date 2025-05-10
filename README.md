# Electrochemical Capacitance Model

A Python package for calculating electrochemical capacitance using steric models (Carnahan-Starling or Liu) for ion interactions.

## Authors

- Dagmawi Tadesse
- Drew Parsons

## Features

- Ion and Solvent classes with physical properties
- Pre-defined database of common ions and solvents
- Electrochemical system modeling with hydration effects
- Steric energy calculations using Carnahan-Starling or Liu models
- Capacitance calculations with potential-dependent dielectric effects
- Visualization utilities for capacitance curves

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from capacitance import ion_database, solvent_database
from capacitance import ElectrochemicalSystem, ElectrochemicalModel
from capacitance import plot_capacitance_vs_potential

# Create a system
system = ElectrochemicalSystem(
    cation=ion_database['Na+'],
    anion=ion_database['F-'],
    solvent=solvent_database['water'],
    concentration=3.89,  # mol/L
    temperature=298.15,  # K
    n_hydration_cation=3.5,
    n_hydration_anion=2.7
)

# Create the model
model = ElectrochemicalModel(system, steric_model='cs')

# Calculate capacitance at a specific potential
potential = 0.5  # V
capacitance = model.analytical_capacitance(potential)
print(f"Capacitance at {potential}V: {capacitance:.2f} μF/cm²")

# Plot capacitance curve
potentials, capacitances = plot_capacitance_vs_potential(
    system,
    potential_range=(-1, 1),
    num_points=101
)
```

## Ion Database

The package includes predefined ions:
- Alkali metal cations: Li+, Na+, K+, Rb+, Cs+
- Halide anions: F-, Cl-, Br-, I-
- Hydrated ions
- Ionic liquid ions: EMIM+, BF4-, TFSI-

## Solvent Database

Available solvents:
- Water
- Ethanol
- Methanol
- Acetonitrile
- Dimethylsulfoxide
- Ionic liquid

## License

MIT License