#! /usr/bin/env python2.7
import sys, ast
from board import *
from player import *

def main(argv):
    ENDC = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    if len(argv) > 0:
        tf = open(argv[0], 'r')
        lc = 0
        tb = []
        pnext = '1'
        pnext = raw_input("Who's going to be next on the test board? 1 - X, 2 - O ")
        for line in tf:
            row = line.strip().split()
            if len(row) == 3:
               tb.append(row)
               lc = lc + 1
            if lc == 3:
                b = Board(test_board = tb)
                print "Testing Board: "
                print b
                if b.is_game_over:
                    print b.winner_msg
                else:
                    if pnext == '2':
                        adv, adv_str = b.get_advantage(False)
                        print "{0} : Test Value Of: {1}".format(adv_str, adv)
                    elif pnext == '1':
                        adv, adv_str = b.get_advantage(True)
                        print "{0} : Test Value Of: {1}".format(adv_str, adv)
                lc = 0
                tb = []
                raw_input("Press Enter To See Next Test")
        print "Exit, pursued by a Bear"
        return 1

    try:
        test_board = ast.literal_eval(argv[0])
        board = Board(test_board = test_board)
    except:
        board = Board(test_board = [['.','.','.'],
                                    ['.','.','.'],
                                    ['.','.','.']])
    board = Board()
    print GREEN + "\t =-= Tic Tac Toe =-=" + ENDC
    print board
    x = Player(chip = 'X')
    o = Player(chip = 'O')
    print RED + "Select an option" + ENDC
    option = raw_input("1 - PC vs PC, 2 - PC vs Hooman: ")
    if option == "1":

        while not board.is_game_over:
            print "Possible Moves: {0}".format(board.empty_cells)
            x.make_best_move(board)
            print "X Moves"
            print board
            raw_input("Press Enter to see next move")
            print "Possible Moves: {0}".format(board.empty_cells)
            o.make_best_move(board)
            print "O Moves"
            print board
            raw_input("Press Enter to see next move")
        print GREEN + board.winner_msg + ENDC
    elif option == "2":
        option = raw_input("1 - Petty Human starts, 2 - Awesome PC starts: ")
        if option == "1":
            board.next_player = 'O'
        else:
            print "X Moves"
            x.make_best_move(board)
            print(board) 
        while not board.is_game_over:
            print "Possible Moves: {0}".format(board.empty_cells)
            got_move = False
            while not got_move:
                move_str = raw_input("What's your move? ")
                try:
                    move = ast.literal_eval(move_str)
                    if move in board.empty_cells:
                        got_move = True
                    else:
                        print "Invalid move"
                except:
                    print "Not a valid input"
            o.make_move(board, move)
            print board
            print "X Moves"
            x.make_best_move(board)
            print board
        print GREEN + board.winner_msg + ENDC
    else:
        print RED + "Invalid option \n Exiting, pursued by a Bear" + ENDC
if __name__ == "__main__":
    main(sys.argv[1:])
