__commandname__ = "Masonry_scene_objects"


def RunCommand(is_interactive):
    from compas_ui.ui import UI

    ui = UI()
    ui.controller.scene_objects()


if __name__ == "__main__":
    RunCommand(True)
