__commandname__ = "Masonry_undo"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.undo()


if __name__ == "__main__":
    RunCommand(True)
