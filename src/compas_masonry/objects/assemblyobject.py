from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.geometry import Point
from compas.colors import Color
from compas_ui.objects import Object


class AssemblyObject(Object):
    """Base object for representing assemblies in a scene."""

    SETTINGS = {
        "show.nodes": False,
        "show.edges": False,
        "show.blocks": True,
        "show.interfaces": True,
        "show.reactions": True,
        "show.loads": False,
        "show.selfweight": False,
        "show.forces": False,
        "color.nodes": Color.from_hex("#0092d2"),
        "color.edges": Color.white(),
        "color.selfweight": Color.magenta(),
        "color.reactions": Color.green().darkened(50),
        "color.forces": Color.blue(),
    }

    def __init__(self, *args, **kwargs):
        super(AssemblyObject, self).__init__(*args, **kwargs)

    @property
    def assembly(self):
        return self.item

    @assembly.setter
    def assembly(self, assembly):
        self.item = assembly
        self._anchor = None
        self._location = None
        self._scale = None
        self._rotation = None

    @property
    def anchor(self):
        return self._anchor

    @anchor.setter
    def anchor(self, node):
        if self.assembly.has_node(node):
            self._anchor = node

    @property
    def location(self):
        if not self._location:
            self._location = Point(0, 0, 0)
        return self._location

    @location.setter
    def location(self, location):
        self._location = Point(*location)

    @property
    def scale(self):
        if not self._scale:
            self._scale = 1.0
        return self._scale

    @scale.setter
    def scale(self, scale):
        self._scale = scale

    @property
    def rotation(self):
        if not self._rotation:
            self._rotation = [0, 0, 0]
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = rotation

    @property
    def node_xyz(self):
        return None

    def select_nodes(self):
        raise NotImplementedError

    def select_edges(self):
        raise NotImplementedError

    def modify_nodes(self, nodes, names=None):
        raise NotImplementedError

    def modify_edges(self, edges, names=None):
        raise NotImplementedError

    def move_node(self, node):
        raise NotImplementedError

    def move_edge(self, edge):
        raise NotImplementedError
