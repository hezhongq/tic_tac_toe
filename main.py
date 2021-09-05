"""This is a tic-tac-toe game
"""

BOARD_SIZE = 3


class Player:
    def __init__(self, name):
        self.name = name

    def move(self, b):
        # asks user for x-y coordinates
        row = int(input("Please enter the row of your move"))
        col = int(input("Please enter the column of your move"))
        # while loop
        while not (0 <= row < BOARD_SIZE) or not (0 <= col < BOARD_SIZE) or b.board[row][col] != " ":
            print("Invalid input, please try again.")
            row = int(input("Please enter the row of your move"))
            col = int(input("Please enter the column of your move"))
        # update board
        b.board[row][col] = self.name
        b.count += 1


class Board:
    def __init__(self):
        self.board = []
        self.count = 0
        # initialize board
        for i in range(BOARD_SIZE):
            temp = []
            for j in range(BOARD_SIZE):
                temp.append(" ")
            self.board.append(temp)

    def display_board(self):
        s1 = ''
        for i in range(BOARD_SIZE):
            s1 += '   ' + str(i + 1)
        print(s1)
        for i in range(BOARD_SIZE):
            temp = str(i + 1)
            for j in range(BOARD_SIZE):
                temp += ' ' + str(self.board[i][j]) + ' |'
            temp = temp[:-1] + ' '
            print(temp)
            if i < BOARD_SIZE - 1:
                temp = ' '
                for j in range(BOARD_SIZE):
                    temp += '---+'
                temp = temp[:-1]
                print(temp)


def check_winner(b, player):
    """ check who is the winner

    :param board:
    :param Player:
    :return: return True if current player win
    """
    # check horizontal
    if b.board[0][0] == b.board[0][1] == b.board[0][2] == curr_player or \
            b.board[1][0] == b.board[1][1] == b.board[1][2] == curr_player or \
            b.board[2][0] == b.board[2][1] == b.board[2][2] == curr_player:
        return curr_player
    # check vertical
    elif b.board[0][1] == b.board[1][1] == b.board[2][1] == curr_player or \
            b.board[0][0] == b.board[1][0] == b.board[2][0] == curr_player or \
            b.board[0][2] == b.board[1][2] == b.board[2][2] == curr_player:
        return curr_player
    # check diagonal
    elif b.board[0][0] == b.board[1][1] == b.board[2][2] == curr_player or \
            b.board[0][2] == b.board[1][1] == b.board[2][0] == curr_player:
        return curr_player
    return False


def check_full(b):
    if b.count == 9:
        return True
    return False


if '__main__' == __name__:

    p1 = Player("O")
    p2 = Player("X")
    b = Board()

    c = 0
    curr_player = p1

    while True:
        if check_full(b):
            print("Tie!")
            break

        rtn = check_winner(b, curr_player)
        if rtn is not False:
            print("the winner is {}".format(rtn))
            break

        curr_player.move(b)
        b.display_board()
        if c % 2 == 0:
            curr_player = p2
            c = 1
        else:
            curr_player = p1
            c = 0

    print("done!")
















