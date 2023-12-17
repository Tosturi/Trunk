from Players import CreatePlayer
from enums import Direction
from random import randint


class Bot(CreatePlayer):
    """Создание игрока-бота"""
    def deploy_fleet(self):
        """Расстановка кораблей ботом"""
        self.own_arena.put_ship(1, 2, Direction.vertical)

    def shoot(self) -> tuple[int, int]:
        """Бот выбирает координаты выстрела"""
        row = randint(0, len(self.enemy_arena.arena)-1)
        column = randint(0, len(self.enemy_arena.arena)-1)
        return row, column
