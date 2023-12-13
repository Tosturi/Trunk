from Players import CreatePlayer
from enums import Direction


class Human(CreatePlayer):
    """Создание игрока-человека"""

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def deploy_fleet(self):
        """Расстановка короблей игроком"""
