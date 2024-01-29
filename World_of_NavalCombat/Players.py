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
        self.row_alpha = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
            "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
            "K": 10, "L": 11, "M": 12, "N": 13, "O": 14,
            "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
            "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24,
            "Z": 25
        }
        self.list_ships = [(4, 1), (3, 1), (3, 2), (2, 1),
                           (2, 2), (2, 3), (1, 1), (1, 2),
                           (1, 3), (1, 4)]

    def shoot(self) -> tuple[int, int]:
        """Выстрел игрока/бота. Возвращает координаты (row, column)"""
        raise NotImplementedError

    def deploy_fleet(self) -> None:
        """ Расстановка кораблей
            Метод является абстрактным
        """
        raise NotImplementedError("You're using an abstract method")

    def check_shoot(self, row: int, column: int) -> ShotResults:
        """Проверяем результат выстрела"""
        return self.own_arena.check_shoot(row, column)

    def all_dead(self) -> bool:
        """Проверяем остались ли корабли на вражеской арене"""
        for i in self.own_arena.arena:
            for j in i:
                if j["is_alive"]:
                    return False
        return True

    def show_arena(self, arena) -> None:
        """Вывод арены игроку"""
        print(' ', end='\t')
        for m in range(self.column_len):
            print(m, end='\t')
        print('\n')
        for index, row in enumerate(arena):
            print(list(self.row_alpha.keys())[index], end='\t')
            for cell in row:
                print(cell["cell_type"], end='\t')
            print()
