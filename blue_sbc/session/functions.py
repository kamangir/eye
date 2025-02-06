import os
from typing import List

from abcli.env import ABCLI_PATH_IGNORE
from blue_objects import file

from blue_sbc.logger import logger


def reply_to_bash(
    status: str,  # exit/reboot/seed/shutdown/update
    content: List[str] = [],
) -> bool:
    logger.info(f"session.reply_to_bash({status}).")

    return file.save_text(
        filename=os.path.join(
            ABCLI_PATH_IGNORE,
            f"session_reply_{status}",
        ),
        text=content,
    )
