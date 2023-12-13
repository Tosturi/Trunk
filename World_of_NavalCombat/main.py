from Players import CreatePlayer
from Session import GameSession

if __name__ == '__main__':
    player1 = CreatePlayer()
    player2 = CreatePlayer()
    game = GameSession(player1, player2)