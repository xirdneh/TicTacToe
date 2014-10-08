import copy, random

class Player(object):

    def __init__(self, chip = 'X'):
        self.chip = chip
        self.best_moves = []

    def __str__(self):
        return "Player: " + self.chip

    def make_move(self, board, cell):
        board.make_move(chip = self.chip, cell=cell)

    def make_best_move(self, board):
        if len(board.empty_cells) == board.size * board.size:
            #self.make_move(board, [board.size / 2, board.size / 2])
            self.make_move(board, random.choice(board.empty_cells))
            #print board.empty_cells
            return True
        elif board.is_game_over:
            return False
        else:
            bound = board.size * 2 + 2
            a = -100
            self.best_moves = []
            #print board.empty_cells
            possible_moves = copy.deepcopy(board.empty_cells)
            base_depth = len(board.empty_cells)
            for move in possible_moves:
                #print "Tree: \n"
                #print board
                #raw_input(" wait... \n")
                board.make_move(board.next_player, move)
                #print "'{0}'".format(board)
                best_move_val = self.__minmax(copy.deepcopy(board), 0, bound * -1,bound, base_depth)
                board.clear_cell('.', move)
                #print ("========================")
                #print move
                #raw_input(" wait... \n")

                #print "best_move_val: {0} move {1}".format(best_move_val, move)
                #print "move {0} results in  {1}".format(move, board.winner)
                if best_move_val > a:
                    a = best_move_val
                    self.best_moves.append((best_move_val, move))
                elif best_move_val == a:
                    self.best_moves.append((best_move_val, move))

            #print "Best Move: {0}".format(self.best_moves)
            move_to_make = self.best_moves[0]
            #print self.best_moves
            for m in self.best_moves:
                if m[0] >= move_to_make[0]:
                    move_to_make = m
            print "selected {0}".format(move_to_make)
            self.make_move(board, move_to_make[1])
            return True

    def __minmax(self, b, depth, alfa, beta, base_depth):
        is_over = b.is_game_over
        if is_over or depth == base_depth:
            #print "is over"
            #print b
            #print b.winner
            if b.winner == 1:
                if self.chip == 'X':
                    return base_depth - depth
                else:
                    return depth - base_depth
            elif b.winner == -1:
                if self.chip == 'O':
                    return base_depth - depth
                else:
                    return depth - base_depth
            else:
                return 0
        possible_moves = copy.deepcopy(b.empty_cells)
        for move in possible_moves:
            b.make_move(b.next_player, move)
            #print b
            #print str(depth)
            #raw_input(" wait... \n")
            val = self.__minmax(b, depth + 1, alfa, beta, base_depth)
            #print "val: {0} \n".format(val)
            #raw_input(" wait... \n")
            b.clear_cell('.', move)
            if b.next_player == self.chip:
                #print "Move: {0} with an alfa: {1} and a beta: {2} and adv: {3}".format(move, alfa, beta, val)
                #print b
                if val > alfa:
                    alfa = val
                if alfa >= beta:
                    return alfa
            else:
                #print "Move: {0} with an alfa: {1} and a beta: {2} and adv: {3}".format(move, alfa, beta, val)
                #print b
                if val < beta:
                    beta = val
                if beta <= alfa:
                    return beta
        if b.next_player == self.chip:
            return alfa
        else:
            return beta

