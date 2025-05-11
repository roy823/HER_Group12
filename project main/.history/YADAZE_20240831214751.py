from ase.build import fcc100, add_adsorbate, molecule
from ase.optimize import LBFGS
from fairchem.core import OCPCalculator

# Set up your system as an ASE atoms object
slab = fcc100('Cu', (3, 3, 3), vacuum=8)
adsorbate = molecule("CO")
add_adsorbate(slab, adsorbate, 2.0, 'bridge')

calc = OCPCalculator(
    model_name="EquiformerV2-31M-S2EF-OC20-All+MD",
    local_cache="pretrained_models",
    cpu=False,
)
slab.calc = calc

# Set up LBFGS dynamics object
dyn = LBFGS(slab)
dyn.run(0.05, 100)