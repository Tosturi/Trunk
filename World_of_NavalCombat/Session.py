from Players import CreatePlayer
from enums import ShotResults
from Human import Human


class GameSession:
    """Сессия в рамках которой проходит игра"""
    def __init__(self, player1: CreatePlayer, player2: CreatePlayer):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.current_player = self.player1
        self.enemy = self.player2

        self.player1.deploy_fleet()
        self.player2.deploy_fleet()

    def __switch_player(self) -> None:
        """Метод призванный менять передавать ход следующему игроку"""
        self.current_player, self.enemy = self.enemy, self.current_player

    def start_battle(self) -> None:
        while self.winner is None:
            print(f"{self.current_player.name}'s move")
            self.current_player.show_arena(self.current_player.enemy_arena.arena)
            # Спрашиваем координаты выстрела
            row, column = self.current_player.shoot()
            # Спрашиваем каков результат выстрела
            shoot_result = self.enemy.check_shoot(row, column)

            match shoot_result:
                case ShotResults.miss:
                    print("Miss!")
                    self.current_player.enemy_arena.arena[row][column]["cell_type"] = 1
                    self.__switch_player()
                case ShotResults.hit:
                    print("hit!")
                    self.current_player.enemy_arena.arena[row][column]["cell_type"] = 2
                case ShotResults.kill:
                    self.current_player.enemy_arena.arena[row][column]["cell_type"] = 2
                    if self.enemy.all_dead():
                        self.winner = self.current_player

        print(f"{self.winner.name} is winner!")
