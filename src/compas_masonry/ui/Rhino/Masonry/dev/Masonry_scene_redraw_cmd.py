__commandname__ = "Masonry_scene_redraw"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.scene_update()


if __name__ == "__main__":
    RunCommand(True)
