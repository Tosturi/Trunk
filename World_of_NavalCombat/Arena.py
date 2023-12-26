from enums import ShotResults


class Arena:
    """Работа с игровым полем"""

    def __init__(self):
        self.arena: list[list[dict]] = [[
            {

                "cell_type": 0,
                "ship_number": 0,
                "is_alive": False

            } for _ in range(11)] for _ in range(11)]
        self.row_len = len(self.arena)
        self.column_len = len(self.arena[0])

    def put_ship(self, ship: tuple[int, int], coordinates: tuple[int, int, tuple[int, int]]):
        """Установка корабля на арене"""
        row, column, direct = coordinates
        ship_type, number = ship
        for _ in range(ship_type):
            self.__set_cell(row, column, ship_type, number)
            row += direct[0]
            column += direct[1]

    def __set_cell(self, row: int, column: int, ship_type: int, ship_number: int):
        """Изменения значений в ячейке"""
        cell = self.arena[row][column]
        cell["cell_type"] = ship_type
        cell["ship_number"] = ship_number
        cell["is_alive"] = True

    def __check_cell(self, row: int, column: int) -> bool:
        """Проверка отдельной ячейки на возможность установки корабля"""
        if 0 <= row < self.row_len and 0 <= column < self.column_len:
            for n in range(-1, 2):
                for m in range(-1, 2):
                    new_row = row + n
                    new_column = column + m
                    if 0 <= new_row < self.row_len and 0 <= new_column < self.column_len:
                        cell = self.arena[new_row][new_column]
                        if cell["cell_type"] != 0 or cell["ship_number"] != 0 or cell["is_alive"]:
                            return False
                    else:
                        return False
            return True
        else:
            return False

    def check_direction(self, coordinates: tuple[int, int, tuple], len_cell: int) -> bool:
        """Проверка направления установки корабля"""
        row, column, direct = coordinates
        for _ in range(len_cell):
            if not self.__check_cell(row, column):
                return False
            row += direct[0]
            column += direct[1]
        return True

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
