from People import Human
from Bots import Bot
from Session import GameSession


def player_input():
    """В данной функции игрок выбирает кто будет играть, а так же имя игрока/бота"""
    while True:
        who_is_player = input("Who will play? (User/bot): ").lower()
        match who_is_player:
            case "user":
                user_name = input("Enter the user name: ")
                return Human(user_name)
            case "bot":
                user_name = input("Enter the bot name: ")
                return Bot(user_name)
            case _:
                print("Incorrect entry try again")


player1 = player_input()
player2 = player_input()

GameSession(player1, player2).start_battle()
