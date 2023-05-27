from dataclasses import dataclass, field
from enum import Enum, unique

import numpy as np
import numpy.typing as npt


@dataclass
class TetriminosStruct:
    name: str = field(init=True)
    official_name: str = field(init=True)
    block: npt.NDArray[np.uint8] = field(init=True)
    size: int = field(init=False)

    def __post_init__(self):
        self.size = self.block.shape[0]
        # self.rotate_random()
        self.rotate_counterclockwise()

    def rotate_clockwise(self):
        self.block = np.rot90(self.block, 3)

    def rotate_counterclockwise(self):
        self.block = np.rot90(self.block, 1)

    def rotate_random(self):
        rndm = np.random.randint(low=0, high=4, size=1)
        self.block = np.rot90(self.block, rndm)

    def get_relative_init_posy(self):
        idx = np.nonzero(np.sum(self.block, axis=0))[0][-1]
        return idx

@unique
class Tetriminos(Enum):  # Define NxN shape
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
