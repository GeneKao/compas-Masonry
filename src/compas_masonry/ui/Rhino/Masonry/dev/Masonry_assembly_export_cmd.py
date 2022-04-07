__commandname__ = "Masonry_assembly_export"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.controller.assembly_export()


if __name__ == "__main__":
    RunCommand(True)
