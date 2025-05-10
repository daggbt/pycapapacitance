"""
Ion and Solvent classes and databases for electrochemical capacitance calculations.
"""

import scipy.constants as sc
from dataclasses import dataclass
from typing import Dict


@dataclass
class Ion:
    """Ion class to store ion properties."""
    name: str
    charge: float  # Elementary charge units
    radiusAng: float  # Ion radius in Angstroms  
    dispersionB: float  # Dispersion coefficient (B) in m³/mol
    ionPolarizability: float  # Ion polarizability in cubic Angstroms
    
    def get_volume_m3(self) -> float:
        """Calculate ion volume in m³ from radius in Angstroms."""
        return 4 * 1e-30 * sc.pi * (self.radiusAng**3) / 3
    
    def get_charge_coulombs(self) -> float:
        """Get charge in Coulombs."""
        return self.charge * sc.e
    
    def get_hydrated_polarizability(self, n_hydration: float, 
                                  water_polarizability: float = 1.4255) -> float:
        """
        Calculate total polarizability of hydrated ion.
        
        Parameters:
        -----------
        n_hydration : float
            Number of water molecules in hydration shell
        water_polarizability : float
            Polarizability of water in cubic Angstroms
            
        Returns:
        --------
        float: Total polarizability in cubic Angstroms
        """
        return self.ionPolarizability + n_hydration * water_polarizability


@dataclass
class Solvent:
    """Solvent class to store solvent properties."""
    name: str
    dielectricConstant: float  # Relative permittivity
    solventPolarizability: float  # Solvent polarizability in cubic Angstroms
    
    def get_permittivity(self) -> float:
        """Get absolute permittivity in F/m."""
        return self.dielectricConstant * sc.epsilon_0


# Ion database
ion_database: Dict[str, Ion] = {
    # Alkali metal cations
    'Li+': Ion(name='Li+', charge=1, radiusAng=0.69, dispersionB=0.0, ionPolarizability=0.03),
    'Na+': Ion(name='Na+', charge=1, radiusAng=1.02, dispersionB=0.0, ionPolarizability=0.139),
    'K+': Ion(name='K+', charge=1, radiusAng=1.38, dispersionB=0.0, ionPolarizability=0.856),
    'Rb+': Ion(name='Rb+', charge=1, radiusAng=1.52, dispersionB=0.0, ionPolarizability=1.43),
    'Cs+': Ion(name='Cs+', charge=1, radiusAng=1.67, dispersionB=0.0, ionPolarizability=2.42),
    
    # Halide anions
    'F-': Ion(name='F-', charge=-1, radiusAng=1.33, dispersionB=0.0, ionPolarizability=1.913),
    'Cl-': Ion(name='Cl-', charge=-1, radiusAng=1.81, dispersionB=0.0, ionPolarizability=3.66),
    'Br-': Ion(name='Br-', charge=-1, radiusAng=1.96, dispersionB=0.0, ionPolarizability=4.78),
    'I-': Ion(name='I-', charge=-1, radiusAng=2.20, dispersionB=0.0, ionPolarizability=7.12),
    
    # Hydrated ions
    'Na+_hydrated': Ion(name='Na+_hydrated', charge=1, radiusAng=2.93, dispersionB=0.0, ionPolarizability=0.139),
    'F-_hydrated': Ion(name='F-_hydrated', charge=-1, radiusAng=1.95, dispersionB=0.0, ionPolarizability=1.913),
    
    # Ionic liquid ions
    'EMIM+': Ion(name='EMIM+', charge=1, radiusAng=3.7, dispersionB=0.0, ionPolarizability=8.0),
    'TFSI-': Ion(name='TFSI-', charge=-1, radiusAng=2.85, dispersionB=0.0, ionPolarizability=5.0),
}

# Solvent database  
solvent_database: Dict[str, Solvent] = {
    'water': Solvent(name='water', dielectricConstant=78.5, solventPolarizability=1.4255),
    'ethanol': Solvent(name='ethanol', dielectricConstant=24.6, solventPolarizability=5.13),
    'methanol': Solvent(name='methanol', dielectricConstant=32.7, solventPolarizability=3.29),
    'acetonitrile': Solvent(name='acetonitrile', dielectricConstant=36.6, solventPolarizability=4.48),
    'dimethylsulfoxide': Solvent(name='dimethylsulfoxide', dielectricConstant=46.7, solventPolarizability=8.13),
    'ionic_liquid': Solvent(name='ionic_liquid', dielectricConstant=1.0, solventPolarizability=0.0),
}