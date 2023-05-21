from gameboard import GameBoard


def tetris():
    game_board = GameBoard()

    while True:
        game_board.update()


if __name__ == '__main__':
    tetris()
