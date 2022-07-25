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

    def prompt_move(board):
        symbol_black = "X"
        symbol_white = "O"
        if board.nextplayer < 0:
            in_line = input(f"Black player's turn ({symbol_black}): enter coloumn and row of target cell, separated by a space  \n")
        else:
            in_line = input(f"White player's turn ({symbol_white}): enter coloumn and row of target cell, separated by a space  \n")
        
        try:
            xy = in_line.split()
            if (len(xy) == 2 and int(xy[0]) > 0 and int(xy[0]) <= board.size and int(xy[1]) > 0 and int(xy[1]) <= board.size):
                return (int(xy[0]),int(xy[1]))
            else: raise ValueError
        except:
            print ("invalid input, try again please")
            return (BoardView.prompt_move(board))