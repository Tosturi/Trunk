class GameSession:
    """Сессия в рамках которой проходит игра"""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.current_player = player1
        self.enemy = player1

    def __switch_player(self):
        self.current_player, self.enemy = self.enemy, self.current_player
