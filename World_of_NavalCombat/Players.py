from Arena import Arena


class CreatePlayer:
    """Создание сущности игрока"""
    def __init__(self):
        self.own_arena = Arena()
        self.enemy_arena = Arena()

    def deploy_fleet(self):
        """ Расстановка кораблей
            Метод является абстрактным
        """
        raise NotImplementedError("You're using an abstract method")
