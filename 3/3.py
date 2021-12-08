from typing import List, Dict


def bit_counter(diagnostic: List) -> Dict:
    bits = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}

    for number in diagnostic:
        for n, bit in enumerate(number):
            if bit == "1":
                bits[n] += 1

    return bits


def gama_epsilon_decoder(count: Dict, size: int) -> int:
    gama = ''
    epsilon = ''
    for position in count:
        if  count[position] > size/2:
            gama += "1"
            epsilon += "0"
        else:
            gama += "0"
            epsilon += "1"
            
    return gama, epsilon


def string_to_int(string: str) -> int:
    output = 0
    for n, char in enumerate(reversed(string)):
        if char == "1":
            output += 2**n

    return output


def most_least_common(diagnostic: List, pos: int) -> List:
    list_1s = []
    list_0s = []

    for number in diagnostic:
        if number[pos] == "1":
            list_1s.append(number)

        if number[pos] == "0":
            list_0s.append(number)

    if len(list_1s) >= len(list_0s):
        return list_1s, list_0s
    else:
        return list_0s, list_1s
        


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

    diagnostic = [line.strip("\n") for line in data]
    count = bit_counter(diagnostic)
    print(count)

    gama, epsilon = gama_epsilon_decoder(count, len(diagnostic))
    print(f"gama {gama} epsilon {epsilon}")

    gama = string_to_int(gama)
    epsilon = string_to_int(epsilon)
    print(f"gama {gama} epsilon {epsilon}, power {gama*epsilon}")

    most, least = most_least_common(diagnostic, 0)
    start = 1
    while len(most) > 1:
        most, _ = most_least_common(most, start)
        start += 1
    most = string_to_int(most[0])
    
    start = 1
    while len(least) > 1:
        _, least = most_least_common(least, start)
        start += 1
    least = string_to_int(least[0])
    print(f"oxygen {most}, C02 {least}, life support {most*least}")
