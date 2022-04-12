import os
import compas_rhino
from compas_ui.controller import Controller
from compas_ui.ui import UI

from compas_masonry.rhino.forms.scene import SceneObjectsForm


class MasonryController(Controller):
    def __init__(self, ui):
        super(MasonryController, self).__init__(ui)

    @UI.error()
    def scene_objects(self):
        """Display a form with all objects in the scene.

        Returns
        -------
        None

        """
        form = SceneObjectsForm(self.ui.scene)
        if form.show():
            self.ui.scene.update()
            self.ui.record()

    @UI.error()
    def assembly_create(self):
        """Create an assembly from various types of input.

        Returns
        -------
        None

        """
        from compas_assembly.datastructures import Assembly
        from compas_ui.rhino.forms import FileForm

        options = ["File", "Meshes", "PolySurfaces", "Template"]
        option = compas_rhino.rs.GetString("Create an assembly from", strings=options)

        if not option:
            return

        if option == "File":
            path = FileForm.open(self.ui.dirname or os.path.expanduser("~"))
            if not path:
                return

            basename = os.path.basename(path)
            _, ext = os.path.splitext(path)

            if ext == ".obj":
                raise NotImplementedError
            elif ext == ".off":
                raise NotImplementedError
            elif ext == ".ply":
                raise NotImplementedError
            elif ext == ".json":
                assembly = Assembly.from_json(path)
            else:
                raise NotImplementedError

        elif option == "Meshes":
            guids = compas_rhino.select_meshes()
            if not guids:
                return

            assembly = Assembly()
            assembly.add_blocks_from_rhinomeshes(guids)

        elif option == "PolySurfaces":
            guids = compas_rhino.select_surfaces()
            if not guids:
                return

            assembly = Assembly()
            assembly.add_blocks_from_polysurfaces(guids)

        elif option == "Template":
            raise NotImplementedError

        else:
            raise NotImplementedError

        self.ui.scene.clear()
        self.ui.scene.add(assembly, name=assembly.name)
        self.ui.scene.update()
        self.ui.record()

    @UI.error()
    def assembly_interfaces(self):
        """Identify the interfaces of the assembly.

        Returns
        -------
        None

        """
        objects = self.ui.scene.get(name="Assembly")
        if not objects:
            return

        nmax = self.ui.settings["compas_assembly"]["identify_interfaces"]["nmax"]
        tmax = self.ui.settings["compas_assembly"]["identify_interfaces"]["tmax"]
        amin = self.ui.settings["compas_assembly"]["identify_interfaces"]["amin"]

        obj = objects[0]
        assembly = obj.assembly

        assembly_interfaces = self.ui.proxy.function(
            "compas_assembly.algorithms.assembly_interfaces_numpy"
        )
        assembly = assembly_interfaces(assembly, nmax=nmax, tmax=tmax, amin=amin)

        obj.assembly = assembly
        self.ui.scene.update()
        self.ui.record()

    @UI.error()
    def assembly_export(self):
        """Export an assembly to JSON.

        Returns
        -------
        None

        """
        from compas_ui.rhino.forms import FileForm

        objects = self.ui.scene.get(name="Assembly")
        if not objects:
            return

        obj = objects[0]
        assembly = obj.assembly

        path = FileForm.save(
            dirname=self.ui.dirname or os.path.expanduser("~"), basename="Assembly.json"
        )
        if not path:
            return

        assembly.to_json(path)

    @UI.error()
    def assembly_import(self):
        """Import an assembly from JSON.

        Returns
        -------
        None

        """
        from compas_assembly.datastructures import Assembly
        from compas_ui.rhino.forms import FileForm

        path = FileForm.open(dirname=self.ui.dirname or os.path.expanduser("~"))
        if not path:
            return

        assembly = Assembly.from_json(path)
        self.ui.scene.clear()
        self.ui.scene.add(assembly)
        self.ui.scene.update()
        self.ui.record()

    @UI.error()
    def assembly_equilibrium(self):
        """Compute the state of equilibrium of the model.

        Returns
        -------
        None

        """
        objects = self.ui.scene.get(name="Assembly")
        if not objects:
            return

        obj = objects[0]
        assembly = obj.assembly

        options = ["RBE", "CRA", "PRD", "3DEC", "FEA2"]
        option = compas_rhino.rs.GetString("3D equilibrium solver", strings=options)

        if not option:
            return

        if option == "RBE":
            function = self.proxy.function(
                "compas_rbe.equilibrium.interfaceforces_cvx.compute_interface_forces_cvx"
            )
            params = self.ui.settings["compas_rbe"]["compute_interface_forces_cvx"]

        elif option == "CRA":
            function = self.proxy.function("compas_cra.equilibrium.cra_pyomo.cra_solve")
            params = self.ui.settings["compas_cra"]["cra_solve"]

        elif option == "PRD":
            pass

        else:
            raise NotImplementedError

        if not function:
            return

        assembly = function(assembly, **params)

        obj.assembly = assembly
        self.ui.scene.update()
        self.ui.record()
