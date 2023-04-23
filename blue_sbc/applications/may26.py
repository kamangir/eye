from blue_sbc.application import Application as Template
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Application(Template):
    def __init__(self):
        super().__init__()

    def process_image(self, frame, image):
        return super().process_image(frame, image)

    def process_message(self, message):
        return super().process_message(message)

    def step(self, session):
        logger.info("may26.step()")
        return super().step(session)

    def update_screen(self, session):
        return super().update_screen(session)
