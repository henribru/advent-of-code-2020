from aoc.day3 import part1, part2

input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_part1() -> None:
    assert part1(input) == 7


def test_part2() -> None:
    assert part2(input) == 336
