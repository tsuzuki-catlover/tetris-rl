from dataclasses import dataclass
from enum import Enum, unique

import numpy as np
import numpy.typing as npt


@dataclass
class TetriminosStruct:
    name: str
    official_name: str
    block: npt.NDArray[np.uint8]

    def rotate_clockwise(self):
        self.block = np.rot90(self.block, 3)

    def rotate_counterclockwise(self):
        self.block = np.rot90(self.block, 1)

    def rotate_random(self):
        rndm = np.random.randint(low=0, high=4,size=1)
        self.block = np.rot90(self.block, rndm)


@unique
class Tetriminos(Enum):
    tm_I = TetriminosStruct(
        name='I',
        official_name='Hero',
        block=np.array([[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0]])) 
    tm_O = TetriminosStruct(
        name='O',
        official_name='Smashboy',
        block=np.array([[1, 1],
                        [1, 1]]))
    tm_T = TetriminosStruct(
        name='T',
        official_name='Teewee',
        block=np.array([[0, 0, 0],
                        [1, 1, 1],
                        [0, 1, 0]]))
    tm_S = TetriminosStruct(
        name='S',
        official_name='Rhode Island Z',
        block=np.array([[0, 0, 0],
                        [0, 1, 1],
                        [1, 1, 0]]))
    tm_Z = TetriminosStruct(
        name='Z',
        official_name='Cleveland Z',
        block=np.array([[0, 0, 0],
                        [1, 1, 0],
                        [0, 1, 1]]))
    tm_J = TetriminosStruct(
        name='J',
        official_name='Blue Ricky',
        block=np.array([[0, 1, 0],
                        [0, 1, 0],
                        [1, 1, 0]]))
    tm_L = TetriminosStruct(
        name='L',
        official_name='Orange Ricky',
        block=np.array([[0, 1, 0],
                        [0, 1, 0],
                        [0, 1, 1]]))


def get_next_tetriminos():
    tetriminos = list(Tetriminos.__members__.keys())


if __name__ == '__main__':
    print()
