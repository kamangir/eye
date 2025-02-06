from blue_sbc.application import Application as Template
from blue_sbc.logger import logger


class Application(Template):
    def step(self, session):
        logger.info("may26.step()")
        return super().step(session)
