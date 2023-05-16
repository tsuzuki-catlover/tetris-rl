import sys

from itertools import product

import pygame

from pygame.locals import *


class GameBoard:
    def __init__(self,
                 titlename: str = 'TETRIS',
                 board_width: int = 800,
                 board_height: int = 1000):
        pygame.init()

        self.titlename = titlename
        self.b_width = board_width
        self.b_height = board_height

        board = pygame.display.set_mode((self.b_width, self.b_height))
        pygame.display.set_caption(titlename)
        font = pygame.font.Font(None, 60)
        
        # Generate grid
        self.nrow = 20
        self.ncol = 10
        locked_pos = {}
        grid = [(0, 0, 0)
                for _ in product(range(self.ncol), range(self.nrow))]
        for y in range(self.nrow):
            for x in range(self.ncol):
                if (x, y) in locked_pos:
                    color = locked_pos[(x, y)]
                    grid[y][x] = color

        while True:
            board.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
