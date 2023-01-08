from os import system as sys
from colorOutput import *


def drawChessboard() -> list:
    board = []
    column = "     "
    row = ""
    for i in range(1, 16):
        column += chr(64 + i) + "   "
    board.append(column)
    for i in range(1, 16):
        row = "   " + "+---" * 15 + "+"
        board.append(row)
        if i < 10:
            row = "0" + str(i)
        else:
            row = str(i)
        row += " |  " * 15 + " | " + row
        board.append(row)
    board.append("   " + "+---" * 15 + "+")
    board.append(column)
    return board


def displayChessboard(board: list):
    clearScreen()
    for row in board:
        row_ = ""
        for i in row:
            if i == "@":
                row_ += color("bold", "bgRed") + " " + color("default")
            elif i == "#":
                row_ += color("bold", "bgBlue") + " " + color("default")
            else:
                row_ += color("dim", "chWhite", "bgBlack") + \
                     i + color("default")
        print(row_)


def inputCoordinate() -> tuple:
    while (True):
        a = input("以“XYY”格式输入点坐标：")
        try:
            x = a[0].upper()
            if (not (65 <= ord(x) <= 79)):
                raise inputError
            y = int(a[1:])
            if (not (1 <= y <= 15)):
                raise inputError
            break
        except:
            print("输入错误")
    return 4 * ord(x) - 255, 2 * y


def move(board: list, handle: bool) -> tuple:
    if handle:
        print("黑方行")
    else:
        print("白方行")
    while (True):
        x, y = inputCoordinate()
        if (board[y][x] == " "):
            if handle:
                board[y] = board[y][:x] + "@" + board[y][x + 1:]
            else:
                board[y] = board[y][:x] + "#" + board[y][x + 1:]
            break
        else:
            print("此位置已有棋")
    return board, x, y


def getRows(x: int, y: int, board: list) -> list:
    rows = []
    if x >= 11:
        rows.append(board[y][x - 4] + board[y][x - 8] +
                    board[y][x - 12] + board[y][x - 16])
    if x <= 35:
        rows.append(board[y][x + 4] + board[y][x + 8] +
                    board[y][x + 12] + board[y][x + 16])
    if y >= 10:
        rows.append(board[y - 2][x] + board[y - 4][x] +
                    board[y - 6][x] + board[y - 8][x])
    if y <= 22:
        rows.append(board[y + 2][x] + board[y + 4][x] +
                    board[y + 6][x] + board[y + 8][x])
    if x >= 11 and y >= 10:
        rows.append(board[y - 2][x - 4] + board[y - 4][x - 8] +
                    board[y - 6][x - 12] + board[y - 8][x - 16])
    if x <= 35 and y >= 10:
        rows.append(board[y - 2][x + 4] + board[y - 4][x + 8] +
                    board[y - 6][x + 8] + board[y - 8][x + 16])
    if x >= 11 and y <= 22:
        rows.append(board[y + 2][x - 4] + board[y + 4][x - 8] +
                    board[y + 6][x - 8] + board[y + 8][x - 16])
    if x <= 43 and y <= 21:
        rows.append(board[y + 2][x + 4] + board[y + 4][x + 8] +
                    board[y + 6][x + 8] + board[y + 8][x + 16])
    return rows


def judge(rows: list, black: bool) -> bool:
    if black:
        chess = "@" * 4
    else:
        chess = "#" * 4
    for row in rows:
        if (row == chess):
            if (black):
                print("黑方胜")
            else:
                print("白方胜")
            return True
    return False


def gameOver(board: list, handle: bool, x: int, y: int) -> bool:
    if x != -1:
        rows = getRows(x, y, board)
        return judge(rows, handle)
    else:
        return False


if __name__ == "__main__":
    while True:
        print("五子棋")
        bd = drawChessboard()
        displayChessboard(bd)
        black = False
        x, y = -1, -1
        while not gameOver(bd, black, x, y):
            black = not black
            bd, x, y = move(bd, black)
            sys("cls")
            displayChessboard(bd)
