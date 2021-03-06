"""
********************************************************************************
compas_masonry
********************************************************************************

.. currentmodule:: compas_masonry


.. toctree::
    :maxdepth: 1


"""

from __future__ import print_function

import os


__author__ = ["tom van mele"]
__copyright__ = "ETH Zurich - Block Research Group"
__license__ = "MIT License"
__email__ = "van.mele@arch.ethz.ch"
__version__ = "0.1.0"


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]
__all_plugins__ = [
    "compas_masonry.install",
    "compas_masonry.rhino.objects"
]
