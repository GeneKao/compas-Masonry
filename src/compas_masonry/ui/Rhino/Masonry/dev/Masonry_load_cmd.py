__commandname__ = "Masonry_load"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.load()


if __name__ == "__main__":
    RunCommand(True)
