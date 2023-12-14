from Players import CreatePlayer
from enums import Direction
from random import randint, choice


class Bot(CreatePlayer):
    """Создание игрока-бота"""
    def deploy_fleet(self):
        """Расстановка кораблей ботом"""
        self.own_arena.put_ship(1, 2, Direction.vertical)
