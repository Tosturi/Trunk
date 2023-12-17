from Players import CreatePlayer
from enums import Direction


class Human(CreatePlayer):
    """Создание игрока-человека"""

    def deploy_fleet(self):
        """Расстановка кораблей игроком"""

    def shoot(self) -> tuple[int, int]:
        """Спросить у игрока координаты выстрела"""
        while True:
            row = input("Enter a number between 0 and 9: ")
            column = input("Enter a number between 0 and 9: ")
            try:
                if 0 <= int(row) <= 9 and 0 <= int(column) <= 9:
                    return int(row), int(column)
                else:
                    print("Incorrect values have been entered.\nPlease try again.")
            except ValueError:
                print("Incorrect values have been entered.\nPlease try again.")
