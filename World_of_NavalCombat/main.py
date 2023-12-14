from Session import GameSession


def player_input(player_number: int):
    """В данной функции игрок выбирает кто будет играть"""
    who_is_player = input("Who will play? (User/bot): ").lower()
    if who_is_player == 'user':
        user_name = input("Enter the user name: ")
    else:
        user_name = f"Bot {player_number}"

    if who_is_player not in ['user', 'bot']:
        return player_input(player_number)
    else:
        return who_is_player, user_name


if __name__ == '__main__':
    player1 = player_input(1)
    player2 = player_input(2)
    game = GameSession(player1, player2)
