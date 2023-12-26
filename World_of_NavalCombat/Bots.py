from Players import CreatePlayer
from enums import Direction
from random import randint, choice


class Bot(CreatePlayer):
    """Создание игрока-бота"""

    def __init__(self, name: str):
        super().__init__(name)
        self.bot_steps = set()

    def deploy_fleet(self) -> None:
        """Расстановка кораблей ботом"""
        ships = self.list_ships
        while len(ships) > 0:
            ship = ships[0]
            row = randint(0, self.row_len - 1)
            column = randint(0, self.column_len - 1)
            direct = choice(((0, 1), (0, -1), (1, 0), (-1, 0)))
            coordinates = row, column, direct
            if self.own_arena.check_direction(coordinates, ship[0]):
                self.own_arena.put_ship(ship, coordinates)
                print(f"The {ship[0]}-deck ship is set")
                del ships[0]
        else:
            print(f"Ships are deployed!")

    def shoot(self) -> tuple[int, int]:
        """Бот выбирает координаты выстрела"""
        while True:
            row = randint(0, self.row_len-1)
            column = randint(0, self.column_len-1)
            if (row, column) not in self.bot_steps:
                self.bot_steps.add((row, column))
                return row, column
            elif len(self.bot_steps) == self.row_len * self.column_len:
                print("The bot went through every possible option!")
                exit()
