import time

import utils


def part1(lines: list[str]) -> int:
    total_joltage = 0

    for line in lines:
        digits = [int(character) for character in line]
        best_for_line = 0

        for i in range(len(digits) - 1):
            for j in range(i + 1, len(digits)):
                value = 10 * digits[i] + digits[j]
                if value > best_for_line:
                    best_for_line = value
        total_joltage += best_for_line

    return total_joltage


def part2(lines: list[str]) -> int:
    total_joltage = 0

    for line in lines:
        digits = [int(character) for character in line]
        funny_numbers = []
        drop = len(digits) - 12

        for digit in digits:
            while funny_numbers and funny_numbers[-1] < digit and drop > 0:
                funny_numbers.pop()
                drop -= 1
                # print("funny:", funny_numbers, "digit:", digit, "drop:", drop)
            # print("Appending:", digit)
            funny_numbers.append(digit)

        result_digits = funny_numbers[:12]

        value = 0
        for digit in result_digits:
            value = value * 10 + digit

        total_joltage += value

    return total_joltage


def main() -> None:
    test_lines = utils.read_file("tests/day_03.txt")
    assert part1(test_lines) == 357, "part1 test failed"
    assert part2(test_lines) == 3121910778619, "part2 test failed"

    input_lines = utils.read_file("inputs/day_03.txt")

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
