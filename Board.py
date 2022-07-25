class Board:
    # 0 is empty, -1 is black, 1 is white
    def __init__(self,size) -> None:
        self.board = [[0 for _ in range(0, size)] for _a in range (0, size)]
        self.board[size//2][size//2] = 1
        self.board[size//2 - 1][size//2] = -1
        self.board[size//2][size//2 - 1] = -1
        self.board[size//2 - 1][size //2 - 1] = 1
        self.size = size
        self.nextplayer = -1
    
    def return_board(self):
        return self.board
    
    def make_move(self,coords):
        x, y = coords
        affected = Board.list_affected(self,coords,self.nextplayer)
        if (self.board[x-1][y-1] == 0) and affected:
            self.board[x-1][y-1] = self.nextplayer
            for _ in affected:
                ax, ay = _
                self.board[ax][ay] = self.nextplayer
            self.nextplayer *= -1
        else:
            raise ValueError(x,y)

    def list_affected(self,coords,player): 
        #this method returns all pieces that would have to be flipped in case of a move by (player) at (coords)
        x, y = coords
        x, y = x-1, y-1
        #print (f"x = {x+1}, y = {y+1},player = {player}")
        affected = set()
        #check straight lines
        for piece in range (0,x-1):
            #print (f"{x+1,piece+1}: {self.board[x][piece]}")
            if self.board[x][piece] == player:
                for victim in range (piece, x+1):
                    #print(f"iterating: {self.board[x][victim]}")
                    if self.board[x][victim] == player * -1:
                        affected.add ((x,victim))
        #print ("------")
        for piece in range (x,self.size):
            #print (f"{x+1,piece+1}: {self.board[x][piece]}")
            if self.board[x][piece] == player:
                for victim in range (x, piece+1):
                    #print(f"iterating: {self.board[x][victim]}")
                    if self.board[x][victim] == player * -1:
                        affected.add ((x,victim))
        #print ("-----------------")
        
        
        for piece in range (0,y-1):
            if self.board[piece][y] == player:
                for victim in range (piece, y+1):
                    if self.board[victim][y] == player * -1:
                        affected.add ((victim,y))
        for piece in range (y,self.size):
            if self.board[piece][y] == player:
                for victim in range (y, piece+1):
                    if self.board[victim][y] == player * -1:
                        affected.add ((victim,y))

        #check diagonals (todo)

        return affected

        

        
    
