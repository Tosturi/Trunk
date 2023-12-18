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

    def put_ship(self, row: int, column: int, direction: Direction):
        """Установка корабля на арене"""

    def __set_cell(self, row: int, column: int):
        """Изменения значений в ячейке"""

    def __check_cell(self, row: int, column: int):
        """Проверка отдельной ячейки"""

    def check_shoot(self, row: int, column: int) -> ShotResults:
        """Проверяем результат выстрела"""
        if self.arena[row][column]["is_alive"]:
            self.arena[row][column]["is_alive"] = False
            return ShotResults.hit
        else:
            return ShotResults.miss


if __name__ == '__main__':
    field = Arena()

    for i in field.arena:
        for j in i:
            print(j, end='\t')
        print()
