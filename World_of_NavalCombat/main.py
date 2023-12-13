from Players import CreatePlayer
from People import Human
from Bots import Bot
from Session import GameSession

if __name__ == '__main__':
    player1 = Human("Вася")
    player2 = Bot()
    game = GameSession(player1, player2)