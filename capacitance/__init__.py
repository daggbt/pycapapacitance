"""
Electrochemical Capacitance Model Package

A package for calculating electrochemical capacitance using steric models.
"""

from .ions import Ion, Solvent, ion_database, solvent_database
from .models import ElectrochemicalSystem, ElectrochemicalModel
from .utils import plot_capacitance_vs_potential, polarizability_angstrom_to_si, save_capacitance_data

__version__ = "0.1.0"
__all__ = [
    'Ion', 
    'Solvent', 
    'ion_database', 
    'solvent_database',
    'ElectrochemicalSystem', 
    'ElectrochemicalModel',
    'plot_capacitance_vs_potential',
    'polarizability_angstrom_to_si',
    'save_capacitance_data'
]