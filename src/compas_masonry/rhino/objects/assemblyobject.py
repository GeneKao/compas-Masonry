from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import compas_rhino

from compas_ui.rhino.objects import RhinoObject
from compas_masonry.objects import AssemblyObject


class RhinoAssemblyObject(RhinoObject, AssemblyObject):
    def __init__(self, *args, **kwargs):
        super(RhinoAssemblyObject, self).__init__(*args, **kwargs)
        self._guid_node = {}
        self._guid_edge = {}
        self._guid_block = {}
        self._guid_interface = {}

    @property
    def assembly(self):
        return self.item

    @assembly.setter
    def assembly(self, assembly):
        self.item = assembly
        self._guid_node = {}
        self._guid_edge = {}
        self._guid_block = {}
        self._guid_interface = {}

    @property
    def guid_node(self):
        if not self._guid_node:
            self._guid_node = {}
        return self._guid_node

    @guid_node.setter
    def guid_node(self, values):
        self._guid_node = dict(values)

    @property
    def guid_edge(self):
        if not self._guid_edge:
            self._guid_edge = {}
        return self._guid_edge

    @guid_edge.setter
    def guid_edge(self, values):
        self._guid_edge = dict(values)

    @property
    def guid_block(self):
        if not self._guid_block:
            self._guid_block = {}
        return self._guid_block

    @guid_block.setter
    def guid_block(self, values):
        self._guid_block = dict(values)

    @property
    def guid_interface(self):
        if not self._guid_interface:
            self._guid_interface = {}
        return self._guid_interface

    @guid_interface.setter
    def guid_interface(self, values):
        self._guid_interface = dict(values)

    def clear(self):
        compas_rhino.delete_objects(self.guids, purge=True)
        self._guids = []
        self._guid_node = {}
        self._guid_edge = {}
        self._guid_block = {}
        self._guid_interface = {}

    def draw(self):
        self.clear()
        if not self.visible:
            return

        if self.settings["show.nodes"]:
            nodes = list(self.assembly.nodes())
            guids = self.artist.draw_nodes(color=self.settings["color.nodes"])
            self.guids += guids
            self.guid_node = zip(guids, nodes)

        if self.settings["show.edges"]:
            edges = list(self.assembly.edges())
            guids = self.artist.draw_edges(color=self.settings["color.edges"])
            self.guids += guids
            self.guid_edge = zip(guids, edges)

        if self.settings["show.blocks"]:
            blocks = list(self.assembly.blocks())
            guids = self.artist.draw_blocks()
            self.guids += guids
            self.guid_block = zip(guids, blocks)

        if self.settings["show.interfaces"]:
            interfaces = list(self.assembly.interfaces())
            guids = self.artist.draw_interfaces()
            self.guids += guids
            self.guid_interface = zip(guids, interfaces)

    def select_nodes(self):
        """Select nodes of the network.

        Returns
        -------
        list[hashable]
            A list of node identifiers.

        """
        guids = compas_rhino.select_points()
        nodes = [self.guid_node[guid] for guid in guids if guid in self.guid_node]
        return nodes

    def select_edges(self):
        """Select edges of the network.

        Returns
        -------
        list[tuple[hashable, hashable]]
            A list of edge identifiers.

        """
        guids = compas_rhino.select_lines()
        edges = [self.guid_edge[guid] for guid in guids if guid in self.guid_edge]
        return edges

    def modify(self):
        """Update the attributes of the network.

        Returns
        -------
        bool
            True if the update was successful.
            False otherwise.

        """
        pass

    def modify_nodes(self, nodes, names=None):
        """Update the attributes of the nodes.

        Parameters
        ----------
        nodes : list
            The identifiers of the nodes to update.
        names : list, optional
            The names of the atrtibutes to update.
            Default is to update all attributes.

        Returns
        -------
        bool
            True if the update was successful.
            False otherwise.

        """
        pass

    def modify_edges(self, edges, names=None):
        """Update the attributes of the edges.

        Parameters
        ----------
        edges : list
            The identifiers of the edges to update.
        names : list, optional
            The names of the atrtibutes to update.
            Default is to update all attributes.

        Returns
        -------
        bool
            True if the update was successful.
            False otherwise.

        """
        pass

    def move_node(self, node):
        """Move a single node of the network object and update the data structure accordingly.

        Parameters
        ----------
        node : int
            The identifier of the node.

        Returns
        -------
        bool
            True if the operation was successful.
            False otherwise.

        """
        pass
