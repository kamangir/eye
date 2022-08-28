from abcli.modules.session import session
from blue_eye.session import Blue_Eye_Session
from blue_eye import NAME
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def start_session():
    session(Blue_Eye_Session)
    return True
