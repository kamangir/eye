from typing import List

from blue_options.terminal import show_usage


def help_capture(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "image|video"

    args = [
        "[--length 10]",
        "[--preview 1]",
    ]

    return show_usage(
        [
            "@sbc",
            "camera",
            "capture",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "camera.capture",
        mono=mono,
    )


def help_preview(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@sbc",
            "camera",
            "preview",
        ],
        "camera.preview.",
        mono=mono,
    )


help_functions = {
    "capture": help_capture,
    "preview": help_preview,
}
