import random


class GameEngine:
    def __init__(self):
        super().__init__()
        self.players = ['X', 'O']
        self.initialize()

    def __get_empty_matrix(self):
        return [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def __is_matrix_full(self):
        if any(' ' in array for array in self.matrix):
            return False
        else:
            return True

    def __get_matrix_col(self, col):
        return [item[col] for item in self.matrix]

    def initialize(self):
        self.matrix = self.__get_empty_matrix()
        self.current_player = self.players[random.randint(0, 1)]
        self.end_game = False

    def is_cell_occupied(self, row, column):
        return self.matrix[row - 1][column - 1] != ' '

    def set_cell(self, row, column):
        self.matrix[row - 1][column - 1] = self.current_player
        if self.is_winner() or self.__is_matrix_full():
            self.end_game = True

    def set_next_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def is_winner(self):
        same_d1, same_d2 = True, True
        for i in range(0, 3):
            player_array = [
                self.current_player,
                self.current_player,
                self.current_player]

            if player_array in [self.matrix[i], self.__get_matrix_col(i)]:
                return True

            if self.matrix[i][i] != self.current_player:
                same_d1 = False

            if self.matrix[i][2-i] != self.current_player:
                same_d2 = False
        if same_d1 or same_d2:
            return True
        return False
