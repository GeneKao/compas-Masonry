__commandname__ = "Masonry_assembly_interfaces"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.controller.assembly_interfaces()


if __name__ == "__main__":
    RunCommand(True)
