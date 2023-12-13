from Players import CreatePlayer


class Human(CreatePlayer):
    """Создание игрока-человека"""

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        