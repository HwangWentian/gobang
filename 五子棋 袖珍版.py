def drawChessboard() -> list:
    board = []
    column = "   "
    for i in range(1, 16):
        column += chr(64 + i) + " "
    board.append(column)
    row = ""
    for i in range(1, 16):
        if i < 10:
            row = "0" + str(i) + " "
        else:
            row = str(i) + " "
        row += ". " * 14 + "." + " " + row
        board.append(row)
    board.append(column)
    return board


def displayChessboard(board: list):
    for i in bd:
        print(i)


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
    return 2 * ord(x) - 127, y


def move(board: list, handle: bool) -> tuple:
    if (handle):
        print("黑方行")
    else:
        print("白方行")
    while (True):
        x, y = inputCoordinate()
        if (board[y][x] == "."):
            if (handle):
                board[y] = board[y][:x] + "@" + board[y][x + 1:]
            else:
                board[y] = board[y][:x] + "O" + board[y][x + 1:]
            break
        else:
            print("此位置已有棋")
    return board, x, y


def getRows(x: int, y: int, board: list) -> list:
    rows = []
    if (x >= 13):
        rows.append(board[y][x - 2] + board[y][x - 4] +
                    board[y][x - 6] + board[y][x - 8])
    if (x <= 25):
        rows.append(board[y][x + 2] + board[y][x + 4] +
                    board[y][x + 6] + board[y][x + 8])
    if (y >= 5):
        rows.append(board[y - 1][x] + board[y - 2][x] +
                    board[y - 3][x] + board[y - 4][x])
    if (y <= 11):
        rows.append(board[y + 1][x] + board[y + 2][x] +
                    board[y + 3][x] + board[y + 4][x])
    if (x >= 13 and y >= 5):
        rows.append(board[y - 1][x - 2] + board[y - 2][x - 4] +
                    board[y - 3][x - 6] + board[y - 4][x - 8])
    if (x <= 25 and y >= 5):
        rows.append(board[y - 1][x + 2] + board[y - 2][x + 4] +
                    board[y - 3][x + 6] + board[y - 4][x + 8])
    if (x >= 13 and y <= 11):
        rows.append(board[y + 1][x - 2] + board[y + 2][x - 4] +
                    board[y + 3][x - 6] + board[y + 4][x - 8])
    if (x <= 25 and y <= 11):
        rows.append(board[y + 1][x + 2] + board[y + 2][x + 4] +
                    board[y + 3][x + 6] + board[y + 4][x + 8])
    return rows


def judge(rows: list, black: bool) -> bool:
    if (black):
        chess = "@" * 4
    else:
        chess = "O" * 4
    for row in rows:
        if (row == chess):
            if (black):
                print("黑方胜")
            else:
                print("白方胜")
            return True
    return False


def gameOver(board: list, handle: bool, x: int, y: int) -> bool:
    if (x != -1):
        rows = getRows(x, y, board)
        return judge(rows, handle)
    else:
        return False


if __name__ == "__main__":
    while (True):
        print("五子棋")
        bd = drawChessboard()
        displayChessboard(bd)
        black = False
        x, y = -1, -1
        while (not gameOver(bd, black, x, y)):
            black = not black
            bd, x, y = move(bd, black)
            displayChessboard(bd)
