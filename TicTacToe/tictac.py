
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
gameGoing = True
flag = ''


def display_board():

    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def chose_sym():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Player 1 Choose X or O : ')
        letter = letter.upper()

    if letter == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def put(pos, pl):
    if board[pos] == "-":
        board[pos] = pl
        display_board()
    else:
        print("Invalid Move")
        pl_choice(pl)


def checkHori(pos, pl):
    global gameGoing
    if pos % 3 == 0:
        if board[pos+1] == board[pos+2] == pl:
            gameGoing = False
    if pos % 3 == 1:
        if board[pos-1] == board[pos+1] == pl:
            gameGoing = False

    if pos % 3 == 2:
        if board[pos-2] == board[pos-1] == pl:
            gameGoing = False


def checkVer(pos, pl):
    global gameGoing
    if pos in [0, 1, 2]:
        if board[pos + 3] == board[pos + 6] == pl:
            gameGoing = False

    if pos in [3, 4, 5]:
        if board[pos + 3] == board[pos - 3] == pl:
            gameGoing = False

    if pos in [6, 7, 8]:
        if board[pos - 3] == board[pos - 6] == pl:
            gameGoing = False


def checkDiag(pos, pl):
    global gameGoing
    if board[0] == board[4] == board[8] == pl:
        gameGoing = False

    if board[2] == board[4] == board[6] == pl:
        gameGoing = False


def checkWin(pos, pl):
    checkHori(pos, pl)
    checkVer(pos, pl)
    checkDiag(pos, pl)

    if not gameGoing:
        global flag
        flag = pl


def pl_choice(pl):
    pos = input(f'Player {pl} Enter your choice (1-9) : ')
    return pos


def play():
    pl1, pl2 = chose_sym()
    while gameGoing:
        pos = pl_choice(pl1)
        put(int(pos)-1, pl1)
        checkWin(int(pos)-1, pl1)
        won()

        pos = pl_choice(pl2)
        put(int(pos)-1, pl2)
        checkWin(int(pos)-1, pl2)
        won()


def won():
    if flag != '':
        print(f'\nPlayer {flag} has Won ')
        exit()


play()

