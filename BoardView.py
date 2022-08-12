from abc import ABC
from datetime import datetime


class BoardView(ABC):
    

    def draw_board(board):
        """displays the game board

        Args:
            board (Board): board to display
        """
        symbol_black = "X"
        symbol_white = "O"
        header = "  x"
        for _ in range(board.size):
            header += f' {_+1} |'
        print(header)
        spaceline = "--+" + "---+"*board.size
        print(" y+"+spaceline[3:])
        for _1 in range(board.size):
            nextline = f" {_1+1}|"
            for _2 in range(board.size):
                piece = " "
                if board.board[_2][_1] < 0:
                    piece = f"{symbol_black}"
                elif board.board[_2][_1] > 0:
                    piece = f"{symbol_white}"              
                nextline += f" {piece} |"
            print(nextline)
            print(spaceline)

    def invalid_move_comment():
        """tells the player that their move has been rejected by the game rules
        """
        print ("this move is not allowed by the game rules, please try something else")
    
    def end_screen(scores,board):
        """diplays a final tally of the pieces and the winner

        Args:
            scores (Tuple): piece counts, black first
            board (Board): the board the game took place on (not used in current iteration)
        """
        symbol_black = "X"
        symbol_white = "O"
        if scores[0] > scores [1]:
            ret = (f"black player ({symbol_black}) won with the score of {scores[0]} to {scores[1]}")
        elif scores[0] < scores [1]:
            ret = (f"white player ({symbol_white}) won with the score of {scores[1]} to {scores[0]}")
        else:
            ret = (f"a draw happened! both players scored {scores[0]} points.")
        curr_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
        filename = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        filename = f"{filename}.txt"
        print(f"at {curr_time}, {ret}")
        with open(filename,"w") as f:
            f.write(f"at {curr_time}, {ret}")
        