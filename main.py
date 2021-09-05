"""This is a tic-tac-toe game
"""

BOARD_SIZE = 3

class Player:
    def __init__(self, name):
        self.name = name

    def move(self, b):
        # asks user for x-y coordinates
        # while loop

        # update board
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


def check_full(b):
    if b.count == 9:
        return True
    return False


if '__main__' == __name__:

    p1 = Player("1")
    p2 = Player("2")
    b = Board()

    curr_player = p1
    b.display_board()

    # while not check_winner(board, curr_player) and not check_full(board):
    #     pass
















