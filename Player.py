class Player:
    currentplayer = -1
    def __init__(self, playertype:int) -> None:
        if  playertype < 0 :
            self.symbol = "X"
        if  playertype > 0 :
            self.symbol = "O"
        self.playertype = playertype


    def prompt_move(self,board):
        
        
        if self.playertype < 0:
            in_line = input(f"Black player's turn ({self.symbol}): enter coloumn and row of target cell, separated by a space  \n")
        else:
            in_line = input(f"White player's turn ({self.symbol}): enter coloumn and row of target cell, separated by a space  \n")
        
        try:
            xy = in_line.split()
            if (len(xy) == 2 and int(xy[0]) > 0 and int(xy[0]) <= board.size and int(xy[1]) > 0 and int(xy[1]) <= board.size):
                Player.currentplayer *= -1
                return (int(xy[0])-1,int(xy[1])-1)
            else: raise ValueError
        except:
            print ("invalid input, try again please")
            return (self.prompt_move(board))