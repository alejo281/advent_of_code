from typing import List, Tuple


def draw_line(vents_map: List[List], pair1: Tuple[int, int], pair2: Tuple[int, int]):
    diff_x = pair2[0] - pair1[0]
    diff_y = pair2[1] - pair1[1]

    print(f"diff_x: {diff_x} diff_y: {diff_y}, {pair1}, {pair2}")
    if diff_x != 0 and diff_y == 0:
        if diff_x > 0:
            for n in range(diff_x+1):
                vents_map[pair1[0]+n][pair1[1]] += 1
        else:
            for n in range(diff_x*(-1)+1):
                vents_map[pair1[0]-n][pair1[1]] += 1

    elif diff_x == 0 and diff_y != 0:
        if diff_y > 0:
            for n in range(diff_y+1):
                vents_map[pair1[0]][pair1[1]+n] += 1
        else:
            for n in range(diff_y*(-1)+1):
                vents_map[pair1[0]][pair1[1]-n] += 1

    elif diff_x != 0 and diff_y != 0:
        if diff_x > 0 and diff_y > 0:
            for n in range(diff_x+1):
                vents_map[pair1[0]+n][pair1[1]+n] += 1

        elif diff_x > 0 and diff_y < 0:
            for n in range(diff_x+1):
                vents_map[pair1[0]+n][pair1[1]-n] += 1

        elif diff_x < 0 and diff_y < 0:
            for n in range(diff_x*(-1)+1):
                vents_map[pair1[0]-n][pair1[1]-n] += 1
        
        elif diff_x < 0 and diff_y > 0:
            for n in range(diff_x*(-1)+1):
                vents_map[pair1[0]-n][pair1[1]+n] += 1

    return vents_map


def count_points(vents_map: List[List]) -> int:
    score = 0
    for row in vents_map:
        for number in row:
            if number > 1:
                score += 1
    return score


def print_map(vents_map: List[List]):
    print()
    for row in vents_map:
        print(row)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = []
        data = f.readline()
        while data != "":
            points = data.split(" -> ")
            point1 = points[0].split(",")
            pair1 = (int(point1[0]), int(point1[1]))

            point2 = points[1].split(",")
            pair2 = (int(point2[0]), int(point2[1]))

            lines.append([pair1, pair2])
            data = f.readline()

    # remove non horizontal or vertical lines
    # lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

    vents_map = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        vents_map = draw_line(vents_map, line[0], line[1])


    score = count_points(vents_map)
    print(f"score: {score}")
