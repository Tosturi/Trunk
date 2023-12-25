from enums import Direction, ShotResults


class Arena:
    """Работа с игровым полем"""

    def __init__(self):
        self.arena: list[list[dict]] = [[
            {

                "cell_type": 0,
                "ship_number": 0,
                "is_alive": False

            } for _ in range(10)] for _ in range(10)]
        self.row_len = len(self.arena)
        self.column_len = len(self.arena[0])

    def put_ship(self, ships: tuple[int, int], coordinates: tuple[int, int, Direction]):
        """Установка корабля на арене"""
        ship_type, number = ships
        for row, column, direct in coordinates:
            if 0 <= row <= self.row_len and 0 <= column <= self.column_len:
                self.arena[row][column]["cell_type"] = ship_type
                self.arena[row][column]["ship_number"] = number
                self.arena[row][column]["is_alive"] = True

    def __set_cell(self, row: int, column: int):
        """Изменения значений в ячейке"""

    def __check_cell(self, row: int, column: int):
        """Проверка отдельной ячейки"""

    def __check_kill(self, row: int, column: int) -> bool:
        """Проверяем уничтожен ли корабль после попадания"""
        ship_type = self.arena[row][column]["cell_type"]
        ship_number = self.arena[row][column]["ship_number"]
        for i in self.arena:
            for j in i:
                if j["cell_type"] == ship_type and j["ship_number"] == ship_number:
                    if j["is_alive"]:
                        return False
        return True

    def check_shoot(self, row: int, column: int) -> ShotResults:
        """Проверяем результат выстрела"""
        if self.arena[row][column]["is_alive"]:
            self.arena[row][column]["is_alive"] = False
            if self.__check_kill(row, column):
                return ShotResults.kill
            else:
                return ShotResults.hit
        else:
            return ShotResults.miss
