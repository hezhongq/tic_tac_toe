"""This is a tic-tac-toe game
"""


class Player:
    def __init__(self, name):
        self.name = name

    def move(self, b):
        # asks user for x-y coordinates
        # while loop

        # update board

        board.count += 1



class Board:
    def __init__(self):
        self.board = []
        self.count = 0
        # TODO
        # initialize board

    def display_board(self):
        # TODO
        # display board


def check_winner(b, Player):
    """

    :param board:
    :param Player:
    :return: return True if current player win
    """
    # check horizontal


    # check vertical


    # check diagonal



def check_full(b):
    if board.count == 9:
        return True
    return False


if "__main__" == __name__:

    p1 = Player("1")
    p2 = Player("2")
    board = Board()

    curr_player = p1

    while not check_winner(board, curr_player) and not check_full(board):
        pass
















