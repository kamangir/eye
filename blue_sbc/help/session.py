from typing import List

from blue_options.terminal import show_usage, xtra


def help_session_start(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("app=<application>,dryrun,sudo,~upload", mono=mono)

    return show_usage(
        [
            "@sbc",
            "session",
            "start",
            f"[{options}]",
        ],
        "start a blue_sbc session.",
        mono=mono,
    )


help_functions = {
    "start": help_session_start,
}
