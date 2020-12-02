from typing import List

import pytest

from aoc.day1 import parse_input, part1, part2


@pytest.fixture
def input() -> List[int]:
    input = """1721
979
366
299
675
1456""".splitlines()
    return parse_input(input)


def test_part1(input: List[int]) -> None:
    assert part1(input) == 514579


def test_part2(input: List[int]) -> None:
    assert part2(input) == 241861950
