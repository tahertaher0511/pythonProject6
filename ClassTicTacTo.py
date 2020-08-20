class TicTacToe:
    def __init__(self):
        self.board = []
        self.state = 'Game not finished'

    def start(self):
        self.get_initial_board()
        self.print_board()
        self.get_move()
        self.game_state()

    def get_initial_board(self):
        cells = list(input('Enter cells: '))
        c = [' ' if x == ' ' else x for x in cells]
        self.board = [[c[0], c[1], c[2]],
                      [c[3], c[4], c[5]],
                      [c[6], c[7], c[8]]]

    def print_board(self):
        print('-' * 9)
        print(f'| {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} |')
        print(f'| {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} |')
        print(f'| {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} |')
        print('_' * 9)

    def get_move(self):
        while True:
            coords = input('Enter the coordinates: ')
            if len(coords.split()) < 2:
                print('You should enter numbers!')
                continue
            a, b = coords.split()
            if a.isdigit() and b.isdigit():
                a, b = int(a), int(b)
                if not (1 <= a <= 3) or not (1 <= b <= 3):
                    print('Coordinates should be from 1 to 3!')
                    continue
                else:
                    i, j = self.transpose_coordinates(a, b)
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.next_move()
                        self.print_board()
                        break
                    else:
                        print('This cell is occupied! choose  another one!')
            else:
                print('You should enter numbers!')
                continue

    def game_state(self):
        if self.count_char('X') + self.count_char('O') >= 9:
            self.state = 'Draw'
        self.check_win()
        print(self.state)

    def transpose_coordinates(self, x, y):
        return 3 - y, x - 1

    def count_char(self, c):
        return self.board[0].count(c) + self.board[1].count(c) + self.board[2].count(c)

    def next_move(self):
        return 'O' if self.count_char('X') > self.count_char('O') else 'X'

    def check_row(self, row):
        if all(i == 'X' for i in row):
            self.state = 'X wins'
        elif all(i == 'O' for i in row):
            self.state = 'O wins'

    def check_win(self):
        b = self.board
        c = [[self.board[i][j] for j in range(3)] for i in range(3)]
        for row in [b[0], b[1], b[2], c[0], c[1], c[2],
                    [b[0][0], b[1][1], b[2][2]],
                    [b[0][2], b[1][1], b[2][0]]]:
            self.check_row(row)


if __name__ == '__main__':
    game = TicTacToe()
    game.start()
