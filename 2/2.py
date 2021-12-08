
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
        
    commands = [command.strip("\n").split() for command in data]

    depth = 0
    position = 0
    for command, movement in commands:
        if command == "forward":
            position += int(movement)

        if command == "down":
            depth += int(movement)

        if command == "up":
            depth -= int(movement)

    print(f"depth: {depth}, position: {position}")
    print(depth*position)


    aim = 0
    depth = 0
    position = 0
    for command, movement in commands:
        if command == "forward":
            position += int(movement)
            depth += aim*int(movement)

        if command == "down":
            aim += int(movement)

        if command == "up":
            aim -= int(movement)

    print(f"depth: {depth}, position: {position}, aim: {aim}")
    print(depth*position)
