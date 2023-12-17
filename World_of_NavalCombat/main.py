from People import Human
from Bots import Bot
from Session import GameSession


def player_input(player_number: int):
    """В данной функции игрок выбирает кто будет играть"""
    while True:
        who_is_player = input("Who will play? (User/bot): ").lower()
        user_name = ""
        match who_is_player:
            case "user":
                user_name = input("Enter the user name: ")
                return Human(user_name)
            case "bot":
                user_name = input("Enter the bot name: ")
                return Bot(user_name)
            case _:
                print("Incorrect entry try again")


player1 = player_input(1)
player2 = player_input(2)

GameSession(player1, player2)
