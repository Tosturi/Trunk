from Players import CreatePlayer
from enums import Direction


class Human(CreatePlayer):
    """Создание игрока-человека"""

    def deploy_fleet(self):
        """Расстановка кораблей игроком"""

    def shoot(self) -> tuple[int, int]:
        """Спросить у игрока координаты выстрела"""
        while True:
            row = int(input("Enter a number between 0 and 9: "))
            column = int(input("Enter a number between 0 and 9: "))
            if 0 <= row <= 9 and 0 <= column <= 9:
                return row, column
            else:
                print("Incorrect values have been entered.\nPlease try again.")


