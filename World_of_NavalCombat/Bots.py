from Players import CreatePlayer
from enums import Direction
import random


class Bot(CreatePlayer):
    """Создание игрока-бота"""
    def deploy_fleet(self):
        """Рандомная расстановка короблей"""
        self.own_arena.put_ship(1, 2, Direction.vertical)
