__commandname__ = "Masonry_bootstrapper"


def RunCommand(is_interactive):
    import compas_bootstrapper as bc

    from compas_ui.ui import UI
    from compas_ui.rhino.forms import InfoForm

    ui = UI()

    text = "Bootstrapper"
    text += "\n" + "-" * len(text) + "\n"

    for name in dir(bc):
        text += "\n\n{}".format(name)
        text += "\n"
        text += " " * 7
        text += "{}".format(getattr(name, bc))

    form = InfoForm(text=text)
    form.show()


if __name__ == "__main__":
    RunCommand(True)
