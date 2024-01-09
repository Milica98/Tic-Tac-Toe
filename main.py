import random


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
            return value - 1


def get_column():
    while True:
        try:
            value = int(input("Type column number (1, 2, 3):"))
            if value not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Wrong value!!")
        else:
            return value - 1


def is_winner(matrix, player):
    same_d1, same_d2 = True, True
    for i in range(0, 3):
        if [player, player, player] in [matrix[i], matrix[:][i]]:
            return True

        if matrix[i][i] != player:
            same_d1 = False

        if matrix[i][2-i] != player:
            same_d2 = False
    if same_d1 or same_d2:
        return True
    return False


def get_empty_matrix():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


def is_matrix_full(matrix):
    if any(' ' in array for array in matrix):
        return False
    else:
        return True


players = ['X', 'O']

current_player = players[random.randint(0, 1)]
game_matrix = get_empty_matrix()

display_matrix(game_matrix)

end_game = False
while not end_game:
    print(f"Next player is {current_player}")

    while True:
        row = get_row()
        column = get_column()
        if game_matrix[row][column] != ' ':
            print(f"Cell [{row+1}][{column+1}] is occupied")
        else:
            break

    game_matrix[row][column] = current_player
    display_matrix(game_matrix)

    if is_winner(game_matrix, current_player) or is_matrix_full(game_matrix):
        if is_winner(game_matrix, current_player):
            print(f"##### Winner is player {current_player} #####")
        else:
            print("##### No winners in this game #####")

        play_again = input("Type 'Y' if you want to play again"
                           "or anything else to exit the game: ")

        if play_again != 'Y':
            end_game = True
        else:
            current_player = players[random.randint(0, 1)]
            game_matrix = get_empty_matrix()
            display_matrix(game_matrix)
    else:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
