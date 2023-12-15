
def player_input(player_number: int):
    """В данной функции игрок выбирает кто будет играть"""
    while True:
        who_is_player = input("Who will play? (User/bot): ").lower()
        user_name = ""
        match who_is_player:
            case "user":
                user_name = input("Enter the user name: ")
            case "bot":
                user_name = input("Enter the bot name: ")
            case _:
                print("Incorrect entry try again")
        return who_is_player, user_name


if __name__ == '__main__':
    print(player_input(1))
    print(player_input(2))
