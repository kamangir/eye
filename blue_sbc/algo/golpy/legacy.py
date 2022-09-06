# content copied from https://github.com/Zeta611/golpy

import textwrap
from typing import Dict, Tuple

import numpy as np


def count_neighbors(grid: np.ndarray) -> np.ndarray:
    #  neighbor_cnts[y, x] is the number of live neighbors of grid[y, x].
    #  scipy.signal.convolve2d() can be used, but manually adding is faster than using convolution.
    neighbor_cnts = np.empty(grid.shape, dtype="uint8")
    # fmt:off
    # Inner area
    neighbor_cnts[1:-1, 1:-1] = (
        grid[:-2, :-2]  # top-left
        + grid[:-2, 1:-1]  # top
        + grid[:-2, 2:]  # top right
        + grid[1:-1, 2:]  # right
        + grid[1:-1, :-2]  # left
        + grid[2:, 2:]  # bottom-right
        + grid[2:, 1:-1]  # bottom
        + grid[2:, :-2]  # bottom-left
    )
    # Four corners
    neighbor_cnts[0, 0] = (  # top-left
        grid[0, 1]  # right
        + grid[1, 1]  # bottom-right
        + grid[1, 0]  # bottom
    )
    neighbor_cnts[0, -1] = (  # top-right
        grid[1, -1]  # bottom
        + grid[1, -2]  # bottom-left
        + grid[0, -2]  # left
    )
    neighbor_cnts[-1, -1] = (  # bottom-right
        grid[-1, -2]  # left
        + grid[-2, -2]  # top-left
        + grid[-2, -1]  # top
    )
    neighbor_cnts[-1, 0] = (  # bottom-left
        grid[-2, 0]  # top
        + grid[-2, 1]  # top-right
        + grid[-1, 1]  # right
    )
    # Four edges
    neighbor_cnts[0, 1:-1] = (  # top
        grid[0, 2:]  # right
        + grid[1, 2:]  # bottom-right
        + grid[1, 1:-1]  # bottom
        + grid[1, :-2]  # bottom-left
        + grid[0, :-2]  # left
    )
    neighbor_cnts[1:-1, -1] = (  # right
        grid[2:, -1]  # bottom
        + grid[2:, -2]  # bottom-left
        + grid[1:-1, -2]  # left
        + grid[:-2, -2]  # top-left
        + grid[:-2, -1]  # top
    )
    neighbor_cnts[-1, 1:-1] = (  # bottom
        grid[-1, :-2]  # left
        + grid[-2, :-2]  # top-left
        + grid[-2, 1:-1]  # top
        + grid[-2, 2:]  # top-right
        + grid[-1, 2:]  # right
    )
    neighbor_cnts[1:-1, 0] = (  # left
        grid[:-2, 0]  # top
        + grid[:-2, 1]  # top-right
        + grid[1:-1, 1]  # right
        + grid[2:, 1]  # bottom-right
        + grid[2:, 0]  # bottom
    )
    # fmt:on
    return neighbor_cnts


def progress(grid: np.ndarray) -> None:
    """Progress grid to the next generation."""

    neighbor_cnts = count_neighbors(grid)

    grid_v = grid.ravel()
    neighbor_cnt_v = neighbor_cnts.ravel()

    birth_rule = (grid_v == 0) & (neighbor_cnt_v == 3)
    survive_rule = (grid_v == 1) & ((neighbor_cnt_v == 2) | (neighbor_cnt_v == 3))

    grid_v[...] = 0
    grid_v[birth_rule | survive_rule] = 1


def grid_print(grid: np.ndarray, generation: int) -> None:
    """Print the formatted grid on screen."""

    print("==== GEN {} ====".format(generation))
    for row in grid:
        for cell in row:
            if cell:
                print("■", end="")
            else:
                print("□", end="")
        print()


def parse_grid(
    text: str, size: Tuple[int, int], pos: str = "C", live: str = "O"
) -> np.ndarray:
    lines = textwrap.dedent(text).strip().splitlines()
    text_width = max(len(line) for line in lines)
    text_height = len(lines)

    width, height = size
    if width < text_width or height < text_height:
        raise ValueError(
            "given text of size {} larger than grid size {}".format(
                (text_width, text_height), size
            )
        )

    grid = np.zeros((height, width), dtype="uint8")

    pos_idx = {
        "C": (height // 2 - text_height // 2, width // 2 - text_width // 2),
        "T": (0, width // 2 - text_width // 2),
        "B": (height - text_height, width // 2 - text_width // 2),
        "L": (height // 2 - text_height // 2, 0),
        "R": (height // 2 - text_height // 2, width - text_width),
        "TL": (0, 0),
        "TR": (0, width - text_width),
        "BL": (height - text_height, 0),
        "BR": (height - text_height, width - text_width),
    }
    offset = pos_idx[pos.upper()]

    for i, line in enumerate(lines):
        if i >= height:
            break
        for j, char in enumerate(line):
            if j >= width:
                break
            grid[i + offset[0], j + offset[1]] = char == live
    return grid


def get_demo(name: str, size: Tuple[int, int], pos: str = "C") -> np.ndarray:
    if name == "random":
        return np.random.randint(0, 2, size, dtype="uint8")

    demos = {
        "glidergun": lambda: parse_grid(
            """\
    ........................O
    ......................O.O
    ............OO......OO............OO
    ...........O...O....OO............OO
    OO........O.....O...OO
    OO........O...O.OO....O.O
    ..........O.....O.......O
    ...........O...O
    ............OO
    """,
            size,
            pos,
        ),
        "glidergen": lambda: parse_grid(
            """\
    ....OOOO

    ..OOOOOOOO

    OOOOOOOOOOOO

    ..OOOOOOOO

    ....OOOO
    """,
            size,
            pos,
        ),
    }

    return demos[name]()
