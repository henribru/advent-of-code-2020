from typing import Iterable, List


def parse_input(input: Iterable[str]) -> List[int]:
    return [int(line) for line in input]


def part1(numbers: Iterable[int]) -> int:
    seen_numbers = set()
    for num in numbers:
        seen_numbers.add(num)
        if 2020 - num in seen_numbers:
            return (2020 - num) * num
    raise ValueError("Invalid input, no numbers summed to 2020")


def part2(numbers: Iterable[int]) -> int:
    seen_numbers = set()
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            seen_numbers.add(num2)
            if i != j and 2020 - num1 - num2 in seen_numbers:
                return (2020 - num1 - num2) * num1 * num2
    raise ValueError("Invalid input, no numbers summed to 2020")


if __name__ == "__main__":
    with open("inputs/day1.txt") as f:
        input = parse_input(f)
    print(part1(input))
    print(part2(input))
