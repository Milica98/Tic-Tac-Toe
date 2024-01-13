import random


class GameEngine:
    def __init__(self):
        super().__init__()
        self.__players = ['X', 'O']

    def new_game(self, is_one_player=False):
        self.__matrix = self.__get_empty_matrix()
        self.__current_player = self.__players[random.randint(0, 1)]
        self.__end_game = False
        self.__is_one_player_mode = is_one_player
        self.__is_computer_current_player = False

    def get_matrix(self):
        return self.__matrix

    def is_computer_current_player(self):
        return self.__is_computer_current_player

    def get_current_player(self):
        return self.__current_player

    def is_cell_occupied(self, row, column):
        return self.__matrix[row - 1][column - 1] != ' '

    def is_end_game(self):
        return self.__end_game

    def set_cell(self, row=-1, column=-1):
        if row < 0 or column < 0:
            row, column = self.__get_rand_cell()

        self.__matrix[row - 1][column - 1] = self.__current_player

        if self.is_winner() or self.__is_matrix_full():
            self.__end_game = True
        else:
            self.__set_next_player()

    def is_winner(self):
        same_d1, same_d2 = True, True
        for i in range(0, 3):
            player_array = 3*[self.__current_player]

            if player_array in [self.__matrix[i], self.__get_matrix_col(i)]:
                return True

            if self.__matrix[i][i] != self.__current_player:
                same_d1 = False

            if self.__matrix[i][2-i] != self.__current_player:
                same_d2 = False
        if same_d1 or same_d2:
            return True
        return False

    def __get_empty_matrix(self):
        return [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def __is_matrix_full(self):
        return not any(' ' in array for array in self.__matrix)

    def __get_matrix_col(self, col):
        return [item[col] for item in self.__matrix]

    def __set_next_player(self):
        if self.__current_player == self.__players[0]:
            self.__current_player = self.__players[1]
        else:
            self.__current_player = self.__players[0]

        if self.__is_computer_current_player:
            self.__is_computer_current_player = False
        elif self.__is_one_player_mode:
            self.__is_computer_current_player = True

    def __get_rand_cell(self):
        free_cells = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.__matrix[i][j] == ' ':
                    free_cells.append((i + 1, j + 1))
        return random.choice(free_cells)
