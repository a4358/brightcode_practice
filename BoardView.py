from abc import ABC


class BoardView(ABC):
    

    def draw_board(board):
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
        print ("this move is not allowed by the game rules, please try something else")
    
    def end_screen(scores,board):
        symbol_black = "X"
        symbol_white = "O"
        if scores[0] > scores [1]:
            print (f"black player ({symbol_black}) won with the score of {scores[0]} to {scores[1]}")
        elif scores[0] < scores [1]:
            print (f"white player ({symbol_white}) won with the score of {scores[1]} to {scores[0]}")
        else:
            print (f"a draw happened! both players scored {scores[0]} points.")