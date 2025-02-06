from typing import List

from blue_options.terminal import show_usage
from abcli.help.generic import help_functions as generic_help_functions

from blue_sbc.help.camera import help_functions as help_camera
from blue_sbc.help.lepton import help_functions as help_lepton
from blue_sbc.help.scroll_phat_hd import help_functions as help_scroll_phat_hd
from blue_sbc.help.sparkfun_top_phat import help_functions as help_sparkfun_top_phat
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
        "browse blue_plugin.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "browse": help_browse,
        "camera": help_camera,
        "lepton": help_lepton,
        "scroll_phat_hd": help_scroll_phat_hd,
        "sparkfun_top_phat": help_sparkfun_top_phat,
    }
)
