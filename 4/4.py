import copy
from typing import List, Dict


def bingo(board: List[List], position: (int, int)) -> bool:
    if board[position[0]].count(None) == len(board[0]):
        return True

    for i in range(len(board[0])):
        if board[i][position[1]] is not None:
            return False

    return True


def contains(board: List[List], number: int) -> (int, int):
    for i, column in enumerate(board):
        if number in column:
            index = column.index(number)
            column[index] = None
            return i, index

    return -1,-1


def sum_res(board: List[List]):
    res = 0
    for column in board:
        for number in column:
            if number is not None:
                res += int(number)

    return res


def print_board(board: List[list]):
    for column in board:
        print(column)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        numbers = f.readline()
        numbers = numbers.strip("\n").split(",")

        f.readline()
        next_line = f.readline()
        boards = []
        while next_line != "":
            board = []
            while next_line != "\n":
                board.append(next_line.strip("\n").split())
                next_line = f.readline()

            boards.append(board)
            next_line = f.readline()
            
    pop = []
    for i, number in enumerate(numbers):
        for n, board in enumerate(boards):

            pos = contains(board, number)
            if pos != (-1, -1):
                winner = bingo(board, pos)

            if winner:
                score = sum_res(board) * int(number)
                print(f"board winner: {n}, after {i} numbers, with score: {score}")
                print(f"final number {number}, sum: {sum_res(board)}")
                print(f"boards left {len(boards)}, numbers left: {len(numbers) - i}")
                print_board(board)
                print()
                pop.append(n)
                winner = False


        pop = [n for n in reversed(sorted(pop))]
        for n in pop:
            boards.pop(n)

        pop = []

