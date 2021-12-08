import time
from typing import List
from functools import lru_cache


def day(lanternfish: List):
    for n, number in enumerate(lanternfish):
        if number == 0:
            lanternfish.append(9)
            lanternfish[n] = 6
        else:
            lanternfish[n] -= 1


@lru_cache
def rec(day: int, days: int, primary: bool = False) -> int:
    if day > days:
        return 0
    else:
        val = 0
        initial = day + 9 if not primary else day + 7
        if initial <= total_days:
            val = rec(initial, days) + 1
            seq = initial + 7

            while seq <= total_days:
                if seq <= total_days:
                    val += rec(seq, days) + 1
                seq = seq + 7

        return val


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readline()

    lanternfish = [int(n) for n in data.split(",")]
    total_days = 256
    start = time.time()

    # for n in range(total_days):
    # day(lanternfish)

    # print(f"total lanternfish: {len(lanternfish)}")
    # print(f"total time: {time.time() - start}")

    lanternfish = [int(n) for n in data.split(",")]
    secondary = []
    for day in lanternfish:
        if day < total_days:
            secondary.append(day + 1)
            day += 8
            while total_days - day >= 0:
                if day <= total_days:
                    secondary.append(day)
                day += 7

    res = 0
    for sec in secondary:
        res += rec(sec, total_days)

    print(f"total lanternfish: {len(lanternfish)+len(secondary)+res}")
    print(f"time: {time.time() - start}")
