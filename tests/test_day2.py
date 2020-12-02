from typing import List

import pytest

from aoc.day2 import InputLine, parse_input, part1, part2


@pytest.fixture
def input() -> List[InputLine]:
    input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()
    return parse_input(input)


def test_part1(input: List[InputLine]) -> None:
    assert part1(input) == 2


def test_part2(input: List[InputLine]) -> None:
    assert part2(input) == 1
