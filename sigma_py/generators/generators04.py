from typing import Generator


def columns(row: list[int]) -> Generator[int, None, None]:
    yield from row


def cells(board: list[list[int]]) -> Generator[int, None, None]:
    for row in board:
        yield from columns(row)


numbers_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for cell in cells(numbers_board):
    print(cell)
