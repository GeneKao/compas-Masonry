__commandname__ = "Masonry_assembly_import"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.controller.assembly_import()


if __name__ == "__main__":
    RunCommand(True)
