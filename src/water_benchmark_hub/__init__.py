import os

from .benchmarks import load

# Add version number
with open(os.path.join(os.path.dirname(__file__), 'VERSION'), encoding="utf-8") as f:
    VERSION = f.read().strip()

# Trigger registration of benchmarks
from . import gecco_waterquality
from . import water_usage
from . import networks
from . import batadal
from . import leakdb
from . import battledim
from . import bwdf
