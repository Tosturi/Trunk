from Arena import Arena


class GameSession:
    """Сессия в рамках которой проходит игра"""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.winner = None
        self.enemy = player1
        self.arena = Arena()


