from Players import CreatePlayer


class Human(CreatePlayer):
    """Создание игрока-человека"""

    def __init__(self, name):
        super().__init__(name)
        self.row_alpha = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
            "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
            "K": 10, "L": 11, "M": 12, "N": 13, "O": 14,
            "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
            "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24,
            "Z": 25
        }

    def deploy_fleet(self):
        """Расстановка кораблей игроком"""
        ships = self.list_ships
        while len(ships) > 0:
            ship = ships[0]
            print(f"Set {ship[0]}-deck ship")
            r, c = input("Enter the starting coordinates (e.g. A5): ").upper()
            direct = input("Select the direction (Up, down, left, right): ").lower()
            match direct:
                case "up":
                    direction = (-1, 0)
                case "down":
                    direction = (1, 0)
                case "right":
                    direction = (0, 1)
                case "left":
                    direction = (0, -1)
                case _:
                    print("Incorrect direction")
                    continue
            coordinates = (self.row_alpha[r], int(c), direction)
            if self.own_arena.check_direction(coordinates, ship[0]):
                self.own_arena.put_ship(ship, coordinates)
                del ships[0]
            else:
                print("It is not possible to set the ship in this direction, please select another direction.")
        else:
            print(f"Ships are deployed!")

    def shoot(self) -> tuple[int, int]:
        """Спросить у игрока координаты выстрела"""
        while True:
            try:
                r, c = input("Enter the coordinates of the shot (e.g. A5): ").upper()
                row = self.row_alpha[r]
                column = int(c)
                if 0 <= row <= self.row_len and 0 <= column <= self.column_len:
                    return row, column
                else:
                    print("Incorrect values have been entered.\nPlease try again.")
            except ValueError:
                print("Incorrect values have been entered.\nPlease try again.")
