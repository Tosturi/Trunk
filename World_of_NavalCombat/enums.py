import enum


class Direction(enum.Enum):
    right: tuple = (0, 1)
    left: tuple = (0, -1)
    down: tuple = (1, 0)
    up: tuple = (-1, 0)


class ShotResults(enum.Enum):
    miss: int = 0
    hit: int = 1
    kill: int = 2
