from os import system as sys


def drawChessboard() -> list:
    board = []
    column = "   "
    for i in range(1, 16):
        column += chr(64 + i) + "   "
    board.append(column)
    row = ""
    for i in range(1, 16):
        if i < 10:
            row = "0" + str(i) + " "
        else:
            row = str(i) + " "
        row += "+---" * 14 + "+" + " " + row
        board.append(row)
        if i < 15:
            board.append("   " + "|   " * 14 + "|")
    board.append(column)
    return board


def displayChessboard(board: list):
    for i in bd:
        print(i)


def inputCoordinate() -> tuple:
    while(True):
        a = input("按照“XYY”格式输入点坐标：")
        x = a[0].upper()
        try:
            if (not(65 <= ord(x) <= 79)):
                raise inputError
            y = int(a[1:])
            if (not(1 <= y <= 15)):
                raise inputError
            break
        except:
            print("输入错误")
    x = 4 * ord(x) - 257
    y = 2 * y - 1
    return x, y


def move(board: list, handle: bool) -> list:
    if (handle):
        print("黑方行")
    else:
        print("白方行")
    while (True):
        x, y = inputCoordinate()
        if (board[y][x] == "+"):
            if (handle):
                board[y] = board[y][:x - 1] + " @ " + board[y][x + 2:]
            else:
                board[y] = board[y][:x - 1] + " O " + board[y][x + 2:]
            break
        else:
            print("此位置已有棋")
    return board


def gameOver(board: list, handle: bool) -> bool:
    return False


if __name__ == "__main__":
    bd = drawChessboard()
    displayChessboard(bd)
    black = True
    while(not gameOver(bd, black)):
        bd = move(bd, black)
        displayChessboard(bd)
        black = not black
