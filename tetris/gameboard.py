import random
import sys

import numpy as np
import pygame

from pygame.locals import QUIT

from tetriminos import Tetriminos


class GameBoard:
    def __init__(self,
                 titlename: str = 'TETRIS',
                 board_width: int = 800,
                 board_height: int = 1000):
        pygame.init()

        self.titlename = titlename
        self.b_width = board_width
        self.b_height = board_height

        self.board = pygame.display.set_mode((self.b_width, self.b_height))
        pygame.display.set_caption(titlename)

        self.play_board = pygame.Surface((400, 800))
        self.play_board = self.play_board.convert()
        self.play_board.fill((255, 255, 255))

        tm = list(Tetriminos)
        self.tetriminos = [tm[i].value for i in range(len(tm))]

        # Generate grid
        self.nrow = 20
        self.ncol = 10
        self.nrow_add = max([i.size for i in self.tetriminos])
        self.nrgb = 3

        self.grid_moving = np.zeros((self.ncol, self.nrow + self.nrow_add))
        self.grid_frozen = np.zeros((self.ncol, self.nrow + self.nrow_add))
        self.colormap = np.zeros((self.ncol, self.nrow, self.nrgb))

        self.clock = pygame.time.Clock()
        self.counter = 0
        self.block_posx = -1
        self.block_posy = 3

    def update(self):
        self.clock.tick(60)  # set FPS
        self.board.fill((128, 128, 128))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # fps = self.clock.get_fps()
        # print(self.clock.get_rawtime(), 'FPS', fps)
        self.counter += self.clock.get_rawtime()
        if self.counter < 1000 / 96:
            return None
        self.counter = 0

        self.grid_moving = np.zeros((self.ncol, self.nrow + self.nrow_add))
        self.current_block = random.choice(self.tetriminos)
        size = self.current_block.size
        x1 = (self.ncol - size) // 2 + 1
        y1 = self.nrow_add - self.current_block.get_relative_init_posy()
        x2 = x1 + size
        y2 = size + y1
        self.grid_moving[x1:x2, y1:y2] = self.current_block.block
        for irow in range(0, self.nrow + self.nrow_add):
            for icol in range(self.ncol):
                if self.grid_moving[icol, irow] == 1:
                    rgb = (255, 0, 255)
                elif self.grid_frozen[icol, irow] == 1:
                    rgb = (128, 128, 128)
                else:
                    rgb = (0, 0, 0)
                pygame.draw.rect(
                    self.play_board,
                    rgb,
                    (icol * 40, (irow - self.nrow_add) * 40, 40, 40)
                    )

        self.board.blit(self.play_board, (100, 150))

        pygame.display.update()
