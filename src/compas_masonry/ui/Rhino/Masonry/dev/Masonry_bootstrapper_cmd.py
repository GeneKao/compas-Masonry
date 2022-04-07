__commandname__ = "Masonry_bootstrapper"


def RunCommand(is_interactive):
    import compas_bootstrapper as bc

    from compas_ui.ui import UI
    from compas_ui.rhino.forms import InfoForm

    ui = UI()

    text = "Bootstrapper"
    text += "\n" + "-" * len(text) + "\n"
    text += "\n".join(
        [
            "{}: {}".format(name, getattr(bc, name))
            for name in dir(bc)
            if not name.startswith("_")
        ]
    )

    form = InfoForm(text=text)
    form.show()


if __name__ == "__main__":
    RunCommand(True)
