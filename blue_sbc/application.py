from blue_sbc.logger import logger


class Application:
    def __init__(self):
        logger.info(f"{self.__class__.__name__} initialized.")

    def process_image(self, frame, image):
        return None

    def process_message(self, message):
        return None

    def step(self, session):
        return None

    def update_screen(self, session):
        return None
