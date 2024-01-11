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


game = GameEngine()

display_matrix(game.matrix)

while not game.end_game:
    print(f"Next player is {game.current_player}")

    while True:
        row = get_row()
        column = get_column()
        if game.is_cell_occupied(row, column):
            print(f"Cell [{row}][{column}] is occupied")
        else:
            break

    game.set_cell(row=row, column=column)
    display_matrix(game.matrix)

    if game.end_game:
        if game.is_winner():
            print(f"##### Winner is player {game.current_player} #####")
        else:
            print("##### No winners in this game #####")

        play_again = input("Type 'Y' if you want to play again "
                           "or anything else to exit the game: ")

        if play_again == 'Y':
            game.initialize()
            display_matrix(game.matrix)
    else:
        game.set_next_player()
