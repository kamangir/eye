class Screen(object):
    def __init__(self):
        self.key_buffer = []

    def show(
        self,
        image,
        header=[],
        sidebar=[],
        as_file=False,
        on_screen=False,
        sign=True,
    ):
        """
        show
        :param image: image
        :param header: header
        :param sidebar: sidebar
        :param options:
            . as_file   : save as file
                       default : False
            . on_screen : show on screen
                       default : False
            . sign   : sign image.
                       default : True
        :return: self
        """
        return self
