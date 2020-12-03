def trees(input: str, x_slope: int, y_slope: int) -> int:
    input = input.splitlines()
    x = 0
    trees = 0
    for y in range(y_slope, len(input), y_slope):
        x = (x + x_slope) % len(input[y])
        if input[y][x] == "#":
            trees += 1
    return trees


def part1(input: str) -> int:
    return trees(input, x_slope=3, y_slope=1)


def part2(input: str) -> int:
    answer = 1
    for x_slope, y_slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        answer *= trees(input, x_slope, y_slope)
    return answer


if __name__ == "__main__":
    with open("inputs/day3.txt") as f:
        input = f.read()
    print(part1(input))
    print(part2(input))
