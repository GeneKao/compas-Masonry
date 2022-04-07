__commandname__ = "Masonry_settings"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.update_settings()


if __name__ == "__main__":
    RunCommand(True)
