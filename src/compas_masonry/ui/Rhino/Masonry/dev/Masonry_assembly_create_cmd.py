__commandname__ = "Masonry_assembly_create"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.controller.assembly_create()


if __name__ == "__main__":
    RunCommand(True)
