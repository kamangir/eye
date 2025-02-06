from typing import List

from blue_options.terminal import show_usage
from abcli.help.generic import help_functions as generic_help_functions

from blue_sbc.help.adafruit_rgb_matrix import help_functions as help_adafruit_rgb_matrix
from blue_sbc.help.camera import help_functions as help_camera
from blue_sbc.help.grove import help_functions as help_grove
from blue_sbc.help.hat import help_functions as help_hat
from blue_sbc.help.lepton import help_functions as help_lepton
from blue_sbc.help.scroll_phat_hd import help_functions as help_scroll_phat_hd
from blue_sbc.help.sparkfun_top_phat import help_functions as help_sparkfun_top_phat
from blue_sbc.help.session import help_functions as help_session
from blue_sbc.help.unicorn_16x16 import help_functions as help_unicorn_16x16
from blue_sbc import ALIAS


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "actions|repo"

    return show_usage(
        [
            "@plugin",
            "browse",
            f"[{options}]",
        ],
        "browse blue_sbc.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "adafruit_rgb_matrix": help_adafruit_rgb_matrix,
        "browse": help_browse,
        "camera": help_camera,
        "grove": help_grove,
        "hat": help_hat,
        "lepton": help_lepton,
        "scroll_phat_hd": help_scroll_phat_hd,
        "session": help_session,
        "sparkfun_top_phat": help_sparkfun_top_phat,
        "unicorn_16x16": help_unicorn_16x16,
    }
)
