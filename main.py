from game_engine import GameEngine


def display_matrix(matrix):
    print(f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} \n"
          "------------\n"
          f" {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} \n"
          "------------\n"
          f" {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} \n")


def get_row():
    while True:
        try:
            value = int(input("Type row number (1, 2, 3):"))
            if value not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Wrong value!!")
        else:
            return value


def get_column():
    while True:
        try:
            value = int(input("Type column number (1, 2, 3):"))
            if value not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Wrong value!!")
        else:
            return value


def get_num_of_players():
    print("🔵 Tic Tac Toe game can play 2 players "
          "but also player against computer 🔵")
    while True:
        try:
            value = int(input("Type number of players (1, 2):"))
            if value not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Wrong value!!")
        else:
            return value


def start_new_game(game):
    print('\033c', end='')
    number_of_players = get_num_of_players()
    if number_of_players == 1:
        game.new_game(is_one_player=True)
    else:
        game.new_game()
    display_matrix(game.get_matrix())


game = GameEngine()
start_new_game(game)

while not game.is_end_game():
    print(f"Next player is {game.get_current_player()}")

    while not game.is_computer_current_player():
        row = get_row()
        column = get_column()
        if game.is_cell_occupied(row, column):
            print(f"Cell [{row}][{column}] is occupied")
        else:
            break

    if game.is_computer_current_player():
        game.set_cell()
    else:
        game.set_cell(row=row, column=column)
    display_matrix(game.get_matrix())

    if game.is_end_game():
        if game.is_winner():
            print(f"🟢 💪 Winner is player {game.get_current_player()} 💪 🟢")
        else:
            print("🟡 No winners in this game 🟡")

        play_again = input("Type 'Y' if you want to play again "
                           "or anything else to exit the game: ")

        if play_again in ['Y', 'y']:
            start_new_game(game)

print("🔴 GAME END 🔴")
