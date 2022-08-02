# 20010011068 / Ali Ekber / KARA

# This function adds mines to the Minesweeper game.
def add_mines(num_m):
    mArray = []
    mcount = 0
    mtries = 0
    while mcount < num_m:
        mtries += 1
        mrow = random.randint(0, board_row - 1)
        mcol = random.randint(0, board_row - 1)
        if board[mcol][mrow] != 'X':
            board[mcol][mrow] = 'X'
            mList = [mcol, mrow]
            mArray.append(mList)
            mcount += 1
    return mArray


# -----------------------------------------------------------------------------

# This function prints the current game board.
def draw_board(modes):
    print("\n----------------------MINESWEEPER----------------------\n")
    print("\t(Number of Mines:{})".format(number_mines), "\n\n")
    print("\t", *range(board_row))
    print("   ", "_ " * (board_row + 1))

    for r in range(board_row):
        playground = []
        for c in range(board_row):
            if modes == "hide" and board[c][r] == "X":
                playground.append("?")
            else:
                playground.append(board[c][r])
        print(r, " |", *playground, "|")

    print("   ", "_ " * (board_row + 1))
    return


# ---------------------------------------------------------------------------

# This function returns the number of bombs around a block.
def get_number_tiles(icol, irow):
    number = 0
    hide = 0

    # if tile has bomb placed, return to function
    if board[icol][irow] == "X":
        number = 9
        return number

    # code looks for bombs placed around current tile
    for i in range(icol - 1, icol + 2):
        for j in range(irow - 1, irow + 2):
            if i < 0 or j < 0 or i == board_row or j == board_row:
                pass
            elif icol == i and irow == j and board[i][j] == "X":
                pass
            elif board[i][j] == 'X':
                number += 1
            elif board[i][j] == '?':
                hide += 1
            else:
                pass
    return number


# ---------------------------------------------------------------------------

# This function reveals a user-selected block.
def user_select_tiles(icol, irow):
    tilecount = get_number_tiles(icol, irow)

    # if its a bomb
    if tilecount == 9:
        return False

    # if tile is between 0-8 then uncover tile
    elif 0 <= tilecount <= 8:
        board[icol][irow] = chr(48 + tilecount)
    return True


# ---------------------------------------------------------------------------

# This function determines whether the user wins.
def did_you_win():
    for r in range(board_row):
        for c in range(board_row):
            if board[c][r] == "?":
                return False
    return True


# ---------------------------------------------------------------------------


# end of functions, start of main code

# imports
import random

wrong = 0

while True:
    while True:
        board_row = int(input("\n\nEnter a size (min : 10): "))
        if board_row < 10:
            print("\nSORRY" + " :(" + "\nINVALID SIZE\n")
            continue
        else:
            break

    board = [["?" for c in range(board_row)] for r in range(board_row)]

    mode = input("\nEnter a mode type: (hidden: 'hide' or obvious: 'show') ")

    number_mines = int(((board_row ** 2) * 30) / 100)

    add_mines(number_mines)

    score = 0
    # ----------------------------------------------------------------
    keeptrying = True
    while keeptrying:
        if mode == "hide":
            draw_board("hide")
        elif mode == "show":
            draw_board("show")
            mode = input("\nEnter 'hide' to return to the game: ")
            continue
        else:
            mode = input("\nThere is no such mode. Please try again: (hidden: 'hide' or obvious: 'show') ")
            continue
        row = int(input("\nRow: "))
        column = int(input("Column: "))
        print("\n")
        if row >= board_row or column >= board_row:
            print("That number is too high. The order goes 0 to", board_row - 1)
            wrong = 1
        elif board[column][row] != "?" and board[column][row] != "X":
            print("Please enter another location.")
            wrong = 1
        else:
            wrong = 0
            score += 1
            keeptrying = user_select_tiles(column, row)

        if wrong != 1:
            if not keeptrying:
                print("BOOOM!!!!\nYOU LOSE\nYOUR SCORE:", (score - 1) * 10)
                draw_board("show")
                break
            elif did_you_win():
                print("CONGRATS\nYOU WIN\nYOUR SCORE:", score * 10)
                draw_board("show")
                break
    end = input("\nEnter 'new' to play a new game, 'exit' to log out: ")
    if end == "new":
        continue
    elif end == "exit":
        break
