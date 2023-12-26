from Players import CreatePlayer


class Human(CreatePlayer):
    """Создание игрока-человека"""

    def deploy_fleet(self):
        """Расстановка кораблей игроком"""
        ships = self.list_ships
        while len(ships) > 0:
            try:
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
                    print(f"The {ship[0]}-deck ship is set")
                    del ships[0]
                    self.show_arena(self.own_arena.arena)
                else:
                    print("It is not possible to set the ship in this direction, please select another direction.")
            except ValueError:
                print("Incorrect value")
                continue
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
