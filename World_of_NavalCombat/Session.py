from Players import CreatePlayer


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

    def __switch_player(self):
        self.current_player, self.enemy = self.enemy, self.current_player
