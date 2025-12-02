import time

import utils


def part1(lines: list[str]) -> int:
    ranges = lines[0].split(",")
    weird_numbers = 0
    for sequence in ranges:
        first, second = map(int, sequence.split("-"))
        processing = second
        while processing >= first:
            if len(str(processing)) % 2 != 0:
                processing -= 1
                continue
            if (
                str(processing)[: len(str(processing)) // 2 + len(str(processing)) % 2]
                == str(processing)[
                    len(str(processing)) // 2 + len(str(processing)) % 2 :
                ]
            ):
                weird_numbers += processing
            processing -= 1

    return weird_numbers


def part2(lines: list[str]) -> int:
    ranges = lines[0].split(",")
    weird_numbers = 0
    for sequence in ranges:
        first, second = map(int, sequence.split("-"))
        processing = second
        while processing >= first:
            # print(processing)
            processingprocessing = (str(processing) * 2)[1:-1]
            if str(processing) in processingprocessing:
                weird_numbers += processing
            processing -= 1
    return weird_numbers


def main() -> None:
    test_lines = utils.read_file("tests/day_02.txt")
    assert part1(test_lines) == 1227775554, "part1 test failed"
    assert part2(test_lines) == 4174379265, "part2 test failed"

    input_lines = utils.read_file("inputs/day_02.txt")

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
