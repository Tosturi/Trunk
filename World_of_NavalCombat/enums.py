import enum


class Direction(enum.Enum):
    horizontal: tuple = (0, 1)
    vertical: tuple = (1, 0)


class ShotResult(enum.Enum):
    miss: int = 0
    hit: int = 1
    kill: int = 2
