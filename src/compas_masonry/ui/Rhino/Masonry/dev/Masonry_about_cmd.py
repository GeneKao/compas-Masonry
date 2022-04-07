__commandname__ = "Masonry_about"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.about()


if __name__ == "__main__":
    RunCommand(True)
