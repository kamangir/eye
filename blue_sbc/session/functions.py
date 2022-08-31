import os
from abcli import file
from abcli.logging import crash_report
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def reply_to_bash(status, content=[]):
    """return to bash with status.

    Args:
        status (str): exit/reboot/seed/shutdown/update
        content (list, optional): content of the status. Defaults to [].
    """
    logger.info(f"session.reply_to_bash({status}).")
    file.create(
        os.path.join(
            os.getenv("abcli_path_cookie", ""),
            f"session_reply_{status}",
        ),
        content,
    )
