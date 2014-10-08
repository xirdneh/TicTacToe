import sys

class Board(object):

    def  __init__(self, size=3, test_board = False):
        self.empty_cells = []
        self.next_player = 'X'
        self.winner_msg = ''
        if test_board:
            self.size = len(test_board)
        else:
            self.size = size
        self.fields = []
        for y in range(self.size):
            row = []
            for x in range(self.size):
                if test_board and len(test_board) - 1 >= y:
                    if test_board and len(test_board[y]) - 1 >= x:
                        row.append(test_board[x][y])
                    else:
                        row.append('.') 
                else:
                    row.append('.')
            self.fields.append(row)
        self.get_empty_cells()

    def get_empty_cells(self):
        self.empty_cells = []
        for y in range(self.size):
            for x in range(self.size):
                if self.fields[x][y] != 'X' and self.fields[x][y] != 'O':
                    self.empty_cells.append((x,y))
        return self.empty_cells

    def __str__(self):
        count_y = 0
        count_x = 0
        ret = ''
        for y in range(self.size):
            for x in range(self.size):
                if count_x != self.size - 1:
                    ret += "{0} | ".format(self.fields[x][y])
                else:
                    ret += "{0} ".format(self.fields[x][y]) + "\n"
                    if count_y != self.size - 1:
                        ret += "------------" + "\n"
                count_x = count_x + 1
            count_y = count_y + 1
            count_x = 0
        return ret
    
    def get_count(self):
        results_rows = []
        results_cols = []
        results_diag = [[0,0],[0,0]]
        for y in range(self.size):
            if len(results_rows) - 1 < y:
                results_rows.append([0,0])
            for x in range(self.size):
                if len(results_cols) - 1 < x:
                    results_cols.append([0,0])
                if self.fields[x][y] == 'X':
                    results_cols[x][0] = results_cols[x][0] + 1
                    results_rows[y][0] = results_rows[y][0] + 1
                    if x == y:
                        results_diag[0][0] = results_diag[0][0] + 1
                    if x == ((self.size - 1)- y):
                        results_diag[1][0] = results_diag[1][0] + 1
                elif self.fields[x][y] == 'O':
                    results_cols[x][1] = results_cols[x][1] + 1
                    results_rows[y][1] = results_rows[y][1] + 1
                    if x == y:
                        results_diag[0][1] = results_diag[0][1] + 1
                    if x == ((self.size - 1) - y):
                        results_diag[1][1] = results_diag[1][1] + 1
        return [results_rows, results_cols, results_diag]

    @property
    def winner(self):
        results = self.get_count()
        for x in range(len(results)):
            for y in range(len(results[x])):
                if results[x][y][0] == self.size:
                    if x == 0:
                        self.winner_msg = "X is winner on row {0}".format(y)
                    elif x == 1:
                        self.winner_msg = "X is winner on col {0}".format(y)
                    elif x == 2 and y == 0:
                        self.winner_msg = "X is winner on main diagonal"
                    elif x == 2 and y == 1:
                        self.winner_msg = "X is winner on reverse diagonal"
                    return 1
                elif results[x][y][1] == self.size: 
                    if x == 0:
                        self.winner_msg = "O is winner on row {0}".format(y)
                    elif x == 1:
                        self.winner_msg = "O is winner on col {0}".format(y)
                    elif x == 2 and y == 0:
                        self.winner_msg = "O is winner on main diagonal"
                    elif x == 2 and y == 1:
                        self.winner_msg = "O is winner on reverse diagonal"
                    return -1

        self.winner_msg = "This game was a tie, bummer."
        return 0

    @property
    def is_game_over(self):
        if (self.winner == -1 or self.winner == 1) or (self.winner == 0 and len(self.empty_cells) == 0):
            return True
        else:
            return False

    def make_move(self, chip, cell):
        if self.fields[cell[0]][cell[1]] != 'X' and self.fields[cell[0]][cell[1]] != 'O':
            cnt = 0
            self.fields[cell[0]][cell[1]] = chip
            for e in self.empty_cells:
                if e[0] == cell[0] and e[1] == cell[1]:
                    self.empty_cells.pop(cnt)
                    break
                cnt = cnt + 1
        if self.next_player == 'X':
            self.next_player = 'O'
        else:
            self.next_player = 'X'

    def clear_cell(self, chip, cell):
        if self.fields[cell[0]][cell[1]] == 'X' or self.fields[cell[0]][cell[1]] == 'O':
            self.fields[cell[0]][cell[1]] = chip
            self.empty_cells.append((cell[0], cell[1]))
        if self.next_player == 'X':
            self.next_player = 'O'
        else:
            self.next_player = 'X'
            
    def get_advantage(self, isXNext):
        results = self.get_count()
        x_adv = 0
        o_adv = 0
        ret = ''
        for x in range(len(results)):
            for y in range(len(results[x])):
                if (results[x][y][0] >= 0 and results[x][y][1] == 0) or (results[x][y][0] == 0 and results[x][y][1] == 0):
                    if x == 0:
                        ret += "X can win on row {0} \n".format(y)
                    elif x == 1:
                        ret += "X can win on col {0} \n".format(y)
                    elif x == 2 and y == 0:
                        ret += "X can win on main diagonal \n"
                    elif x == 2 and y == 1:
                        ret += "X can win on reverse diagonal \n"
                    x_adv = x_adv + 1
                if (results[x][y][1] >= 0 and results[x][y][0] == 0) or (results[x][y][0] == 0 and results[x][y][1] == 0):
                    if x == 0:
                        ret += "O can win on row {0} \n".format(y)
                    elif x == 1:
                        ret += "O can win on col {0} \n".format(y)
                    elif x == 2 and y == 0:
                        ret += "O can win on main diagonal \n"
                    elif x == 2 and y == 1:
                        ret += "O can win on reverse diagonal \n"
                    o_adv = o_adv + 1
        adv = x_adv - o_adv
        if adv > 1 or (adv == 0 and isXNext) or (adv == 1 and isXNext):
            ret += "X has better chance to win E(n) of {0} \n".format(str(adv))
        elif adv < -1  or (adv == 0 and not isXNext) or (adv == -1 and not isXNext):
            ret += "O has better chance to win E(n) of {0} \n".format(str(adv))
        else:
            ret += "Both have same advantage E(n) of {0} \n".format(str(adv))

        return (adv, ret)

