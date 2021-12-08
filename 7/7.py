import sys
from functools import lru_cache


@lru_cache
def fuel_usage(position: int, target: int, rate: int = 1) -> int:
    if position == target:
        return 0
    else:
        if position > target:
            cost = fuel_usage(position-1, target, rate+1) + 1*rate
        else:
            cost = fuel_usage(position+1, target, rate+1) + 1*rate

        return cost


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readline()

    positions = [int(pos) for pos in data.split(",")]

    sys.setrecursionlimit(30000)
    print(sys.getrecursionlimit())

    max_num = max(positions)
    min_num = min(positions)
    cost = (float('inf'), 0)
    for n in range(min_num, max_num):
        temp_cost = 0
        fuel = 0
        for position in positions:
            fuel = fuel_usage(position, n)
            temp_cost += fuel

        if temp_cost < cost[0]:
            cost = (temp_cost, n)

    print(f"cost: {cost[0]} to {cost[1]}")

    
