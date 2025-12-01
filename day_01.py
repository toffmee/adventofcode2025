import time

import utils


def part1(lines: list[str]) -> int:
    zeroes = 0
    number = 50

    for line in lines:
        moves = int(line[1:])
        # print(number, moves, line)

        if line.startswith("L"):
            number = (number - moves) % 100
        else:
            number = (number + moves) % 100

        if number == 0:
            zeroes += 1

    return zeroes


def part2(lines: list[str]) -> int:
    zeroes = 0
    number = 50
    for line in lines:
        moves = int(line[1:])

        if line.startswith("L"):
            if number == 0:
                zeroes += moves // 100
            elif moves >= number:
                zeroes += 1 + (moves - number) // 100

            number = (number - moves) % 100
        else:
            zeroes += (number + moves) // 100
            number = (number + moves) % 100

    return zeroes


def main() -> None:
    test_lines = utils.read_file("tests/day_01.txt")
    assert part1(test_lines) == 3, "part1 test failed"
    assert part2(test_lines) == 6, "part2 test failed"

    input_lines = utils.read_file("inputs/day_01.txt")

    start = time.perf_counter()
    answer1 = part1(input_lines)
    end = time.perf_counter()
    time1_ms = (end - start) * 1000

    start = time.perf_counter()
    answer2 = part2(input_lines)
    end = time.perf_counter()
    time2_ms = (end - start) * 1000

    print(f"Part 1 answer: {answer1} in {time1_ms:.6f}ms")
    print(f"Part 2 answer: {answer2} in {time2_ms:.6f}ms")


if __name__ == "__main__":
    main()
