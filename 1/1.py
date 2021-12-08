

def increase_counter(measurements: list) -> int:
    counter = 0
    for n, m in zip(measurements[1:], measurements):
        if n > m:
            counter += 1

    return counter


def window_sum(measurements: list) -> list:
    return [sum(measurements[i:i+3]) for i in range(len(measurements))]


with open('input.txt', 'r') as f:
    data = f.readlines()
    measurements = [int(depth.strip('\n')) for depth in data]

    print(increase_counter(measurements))

    aggregate = window_sum(measurements)
    print(increase_counter(aggregate))
