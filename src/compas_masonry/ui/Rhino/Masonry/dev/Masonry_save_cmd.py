__commandname__ = "Masonry_save"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.save()


if __name__ == "__main__":
    RunCommand(True)
