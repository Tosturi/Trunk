from Arena import Arena
from enums import ShotResults


class CreatePlayer:
    """Создание сущности игрока"""
    def __init__(self, name: str):
        self.own_arena = Arena()
        self.enemy_arena = Arena()
        self.name = name
        self.row_len = len(self.enemy_arena.arena)
        self.column_len = len(self.enemy_arena.arena[0])

    def shoot(self) -> tuple[int, int]:
        """Выстрел игрока/бота. Возвращает координаты (row, column)"""
        raise NotImplementedError

    def deploy_fleet(self):
        """ Расстановка кораблей
            Метод является абстрактным
        """
        raise NotImplementedError("You're using an abstract method")

    def check_shoot(self, row: int, column: int) -> ShotResults:
        """Проверяем результат выстрела"""
        return self.enemy_arena.check_shoot(row, column)

    def all_dead(self) -> bool:
        """Проверяем остались ли корабли на вражеской арене"""
        for i in self.enemy_arena.arena:
            for j in i:
                if j["is_alive"]:
                    return True
        return False
