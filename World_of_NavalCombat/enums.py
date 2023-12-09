import enum


class Direction(enum.Enum):
    horizontal = (0, 1)
    vertical = (1, 0)


class ShotResult(enum.Enum):
    miss = 0
    hit = 1
    kill = 2

