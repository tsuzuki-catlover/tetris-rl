import random
import sys

from typing import List

import numpy as np
import numpy.typing as npt
import pygame

from pygame.locals import K_LEFT, K_RIGHT, QUIT

from colors import Color
from tetriminos import Tetriminos


class GameBoard:
    def __init__(self,
                 titlename: str = 'TETRIS',
                 board_width: int = 800,
                 board_height: int = 1000):
        # Initialize pygame
        pygame.init()

        # Game board
        self.titlename: str = titlename
        self.b_width: int = board_width
        self.b_height: int = board_height
        self.board = pygame.display.set_mode((self.b_width, self.b_height))
        pygame.display.set_caption(titlename)

        # Play board
        self.play_board = pygame.Surface((400, 800))
        self.play_board = self.play_board.convert()
        self.play_board.fill(Color.BLACK.rgb)

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

        self.posx = 0
        self.posy = 0

        self.clock = pygame.time.Clock()
        self.counter = 0
        # First tetriminos
        self.get_next_block()

    def update(self):
        self.clock.tick(60)  # set FPS
        self.board.fill(Color.GRAY.rgb)
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif pressed_keys[K_RIGHT]:
                self.move_right()
            elif pressed_keys[K_LEFT]:
                self.move_left()

        self.counter += self.clock.get_rawtime()
        if self.counter < 50:
            return None
        elif self.posy == self.nrow + self.nrow_add:
            self.get_next_block()
            self.counter = 0
        else:
            self.move_down()
            self.counter = 0

    def get_next_block(self):
        # Clear grid_moving
        self.grid_moving = np.zeros((self.ncol, self.nrow + self.nrow_add))
        self.current_block = random.choice(self.tetriminos)
        size = self.current_block.size
        x1 = (self.ncol - size) // 2
        y1 = self.nrow_add - self.current_block.get_relative_init_posy()
        x2 = x1 + size
        y2 = size + y1
        # Update grid and positions
        self.grid_moving[x1:x2, y1:y2] = self.current_block.block
        self.posx = x1
        self.posy = 0
        self.update_grid()

    def move_right(self):
        self.move([0, 1])

    def move_left(self):
        self.move([0, -1])

    def move_down(self):
        self.move([1, 0])

    def move(self, direction: List[int]):
        if direction == [0, -1] and self.check_side(-1):
            self.grid_moving = np.roll(self.grid_moving, -1, axis=0)
            self.posx = self.posx - 1
        elif direction == [0, 1] and self.check_side(1):
            self.grid_moving = np.roll(self.grid_moving, 1, axis=0)
            self.posx = self.posx + 1
        elif direction == [1, 0]:
            self.grid_moving = np.roll(self.grid_moving, 1, axis=1)
            self.posy = self.posy + 1
        else:
            return None
        self.update_grid()

    def update_grid(self):
        for irow in range(0, self.nrow + self.nrow_add):
            for icol in range(self.ncol):
                if self.grid_moving[icol, irow] == 1:
                    rgb = self.current_block.color.rgb
                elif self.grid_frozen[icol, irow] == 1:
                    rgb = Color.BROWN.rgb
                else:
                    rgb = Color.BLACK.rgb
                tile_size = 40
                x0 = icol * tile_size
                y0 = (irow - self.nrow_add) * tile_size
                pygame.draw.rect(
                    self.play_board, rgb, (x0, y0, tile_size, tile_size))
        self.board.blit(self.play_board, (100, 150))
        pygame.display.update()

    def check_side(self, change_pos: int):
        tmp_grid = np.roll(self.grid_moving, change_pos, axis=0)
        tmp_sum = np.sum(tmp_grid, axis=1) + np.sum(self.grid_moving, axis=1)
        if tmp_sum[0] > 0 and tmp_sum[-1] > 0:
            return False
        return True
