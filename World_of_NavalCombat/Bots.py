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
        row = randint(0, self.row_len - 1)
        column = randint(0, self.column_len - 1)
        direct = choice((Direction.vertical, Direction.horizontal))
        self.own_arena.put_ship(row, column, direct)

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
