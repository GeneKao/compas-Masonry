import os
import json

HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, "config.json")) as f:
    CONFIG = json.load(f)


__commandname__ = "Masonry_init"


def RunCommand(is_interactive):
    from compas_ui.ui import UI
    from compas_ui.rhino.forms import InfoForm
    from controller import MasonryController

    UI.reset()

    ui = UI(config=CONFIG, controller_class=MasonryController)
    ui.scene_clear()

    form = InfoForm(text="COMPAS Masonry initialised.")
    form.show()


if __name__ == "__main__":
    RunCommand(True)
