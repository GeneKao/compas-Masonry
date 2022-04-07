from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin
from compas_assembly.datastructures import Assembly
from compas_ui.objects import Object

from .assemblyobject import RhinoAssemblyObject


@plugin(category="ui", requires=["Rhino"])
def register_objects():
    Object.register(Assembly, RhinoAssemblyObject, context="Rhino")


__all__ = ["RhinoAssemblyObject"]
