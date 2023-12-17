from Players import CreatePlayer
from enums import Direction
from random import randint, choice


class Bot(CreatePlayer):
    """Создание игрока-бота"""
    def deploy_fleet(self) -> None:
        """Расстановка кораблей ботом"""
        row = randint(0, len(self.enemy_arena.arena) - 1)
        column = randint(0, len(self.enemy_arena.arena) - 1)
        direct = choice((Direction.vertical, Direction.horizontal))
        self.own_arena.put_ship(row, column, direct)

    def shoot(self) -> tuple[int, int]:
        """Бот выбирает координаты выстрела"""
        row = randint(0, len(self.enemy_arena.arena)-1)
        column = randint(0, len(self.enemy_arena.arena)-1)
        return row, column
