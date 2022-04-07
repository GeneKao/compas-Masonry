__commandname__ = "Masonry_redo"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.redo()


if __name__ == "__main__":
    RunCommand(True)
