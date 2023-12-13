from enums import Direction, ShotResult


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
        """Установка коробля на арене"""

    def __set_cell(self, row: int, column: int):
        pass

    def __check_cell(self, row: int, column: int):
        pass


if __name__ == '__main__':
    field = Arena()

    for i in field.arena:
        for j in i:
            print(j, end='\t')
        print()
