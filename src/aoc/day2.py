import re
from collections import Counter
from dataclasses import dataclass
from typing import Iterable, List, Tuple


@dataclass
class PasswordPolicy:
    first: int
    second: int
    character: str


InputLine = Tuple[PasswordPolicy, str]


def parse_input(input: Iterable[str]) -> List[InputLine]:
    def parse_line(line: str) -> Tuple[PasswordPolicy, str]:
        match = re.match(
            r"(?P<first>\d+)-(?P<second>\d+) (?P<character>\w): (?P<password>.+)", line
        )
        if not match:
            raise ValueError(f"Invalid input '{line}'")
        return (
            PasswordPolicy(
                int(match["first"]), int(match["second"]), match["character"]
            ),
            match["password"],
        )

    return [parse_line(line) for line in input]


def part1(input: Iterable[InputLine]) -> int:
    def valid_password(policy: PasswordPolicy, password: str) -> bool:
        return policy.first <= Counter(password)[policy.character] <= policy.second

    return sum(valid_password(policy, password) for policy, password in input)


def part2(input: Iterable[InputLine]) -> int:
    def valid_password(policy: PasswordPolicy, password: str) -> bool:
        return (password[policy.first - 1] == policy.character) != (
            password[policy.second - 1] == policy.character
        )

    return sum(valid_password(policy, password) for policy, password in input)


if __name__ == "__main__":
    with open("inputs/day2.txt") as f:
        input = parse_input(f)
    print(part1(input))
    print(part2(input))
