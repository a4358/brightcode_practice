from abc import ABC


class BoardView(ABC):

    def draw_board(board):
        header = "  |"
        for _ in range(board.size):
            header += f' {_+1} |'
        print(header)
        spaceline = "--+" + "---+"*board.size
        print(spaceline)
        for _1 in range(board.size):
            nextline = f" {_1+1}|"
            for _2 in range(board.size):
                piece = " "
                if board.board[_1][_2] < 0:
                    piece = "X"
                elif board.board[_1][_2] > 0:
                    piece = "O"               
                nextline += f" {piece} |"
            print(nextline)
            print(spaceline)
