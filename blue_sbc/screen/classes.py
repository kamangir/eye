class Screen(object):
    def __init__(self):
        self.key_buffer = []

    def show(
        self,
        image,
        session=None,
        header=[],
        sidebar=[],
        as_file=False,
        on_screen=False,
        sign=True,
    ):
        return self
