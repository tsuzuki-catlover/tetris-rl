import random
import sys

import numpy as np
import pygame

from pygame.locals import QUIT


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

        # Generate grid
        self.nrow = 20
        self.ncol = 10
        self.nrow_add = 4
        self.nrgb = 3

        self.block = np.full((self.ncol, self.nrow), False)
        self.grid = np.full((self.ncol, self.nrow + self.nrow_add), False)
        self.colormap = np.zeros((self.ncol, self.nrow, self.nrgb))

        self.clock = pygame.time.Clock()
        self.counter = 0
        self.block_posy = -2
        self.block_posx = 4

    def update(self):
        self.clock.tick(60)  # set FPS
        self.board.fill((128, 128, 128))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        fps = self.clock.get_fps()
        # print(self.clock.get_rawtime(), 'FPS', fps)
        self.counter += self.clock.get_rawtime()
        if self.counter < 1000 / 96:
            return None
        self.counter = 0
        self.block_posy += 1

        for irow in range(self.nrow):
            for icol in range(self.ncol):
                rgb = (random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))
                pygame.draw.rect(self.play_board, rgb,
                                 (icol * 40, irow * 40, 40, 40))

        self.board.blit(self.play_board, (100, 150))

        pygame.display.update()
