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
        if (self.board[x][y] == 0) and affected:
            self.board[x][y] = self.nextplayer
            for _ in affected:
                ax, ay = _
                self.board[ax][ay] = self.nextplayer
            self.nextplayer *= -1
        else:
            raise ValueError(x,y)
    def skip_move(self):
        self.nextplayer *= -1

    def list_affected(self,coords,player): 
        #this method returns all pieces that would have to be flipped in case of a move by (player) at (coords)
        x, y = coords
        player = int(player)
        affected = set()
        #check straight lines
        #check vertical first (x always is the input x)
        #as above
        node_y = False
        for node_candidate_y in range (0, y):
            if self.board[x][node_candidate_y] == player:
                node_y = node_candidate_y
        if type(node_y) == int:
            valid = True
            potential_victims=set()
            for victim_y in range (node_y+1,y):
                if self.board[x][victim_y] != player*(-1):
                    valid = False
                    break
                potential_victims.add((x,victim_y))
            if valid:
                affected.update(potential_victims)
        #so below
        node_y = False
        for node_candidate_y in range (y+1,self.size):
            if self.board[x][node_candidate_y] == player:
                node_y = node_candidate_y
                break
        if type(node_y) == int:
            valid = True
            potential_victims=set()
            for victim_y in range (y+1,node_y):
                if self.board[x][victim_y] != player*(-1):
                    valid = False
                    break
                potential_victims.add((x,victim_y))
            if valid:
                affected.update(potential_victims)
        #now the same sideways (y is const)
        #to the left
        node_x = False
        for node_candidate_x in range (0, x):
            if self.board[node_candidate_x][y] == player:
                node_x = node_candidate_x
        if type(node_x) == int:
            valid = True
            potential_victims=set()
            for victim_x in range (node_x+1,x):
                if self.board[victim_x][y] != player*(-1):
                    valid = False
                    break
                potential_victims.add((victim_x,y))
            if valid:
                affected.update(potential_victims)
        #to the right
        node_x = False
        for node_candidate_x in range (x+1,self.size):
            if self.board[node_candidate_x][y] == player:
                node_x = node_candidate_x
                break
        if type(node_x) == int:
            valid = True
            potential_victims=set()
            for victim_x in range (x+1,node_x):
                if self.board[victim_x][y] != player*(-1):
                    valid = False
                    break
                potential_victims.add((victim_x,y))
            if valid:
                affected.update(potential_victims)

        #check diagonals (todo)
        #first the \ diagonal (x any y are both increasing/decreasing)
        #checking to the up/left
        node_ldiag = False
        node_x = x-1
        node_y = y-1
        while (node_x >= 0 and node_y >= 0):
            if self.board[node_x][node_y] == player:
                node_ldiag = True
                break
            if self.board[node_x][node_y] == 0:
                break
            node_x -= 1
            node_y -= 1
        if node_ldiag:
            while node_x != x-1:
                node_x += 1
                node_y += 1
                affected.add((node_x,node_y))
        #checking the down/right
        node_ldiag = False
        node_x = x+1
        node_y = y+1
        while (node_x < self.size and node_y< self.size):
            if self.board[node_x][node_y] == player:
                node_ldiag = True
                break
            if self.board[node_x][node_y] == 0:
                break
            node_x += 1
            node_y += 1
        if node_ldiag:
            while node_x != x+1:
                node_x -= 1
                node_y -= 1
                affected.add((node_x,node_y))
        #now the \ diagonal
        #checking to the up/right
        node_rdiag = False
        node_x = x+1
        node_y = y-1
        while (node_x < self.size and node_y >= 0):
            if self.board[node_x][node_y] == player:
                node_rdiag = True
                break
            if self.board[node_x][node_y] == 0:
                break
            node_x += 1
            node_y -= 1
        if node_rdiag:
            while node_x != x+1:
                node_x -= 1
                node_y += 1
                affected.add((node_x,node_y))
        #now the down/left
        node_rdiag = False
        node_x = x-1
        node_y = y+1
        while ( node_x >= 0 and node_y < self.size):
            if self.board[node_x][node_y] == player:
                node_rdiag = True
                break
            if self.board[node_x][node_y] == 0:
                break
            node_x -= 1
            node_y += 1
        if node_rdiag:
            while node_x != x-1:
                node_x += 1
                node_y -= 1
                affected.add((node_x,node_y))


        return affected
    
    def moves_exist(self):
        for x in range (self.size):
            for y in range (self.size):
                if self.board[x][y] == 0:
                    if( self.list_affected((x,y), self.nextplayer)):
                        return True
        return False
    
    def report_pieces(self):
        black = 0
        white = 0
        for x in range (self.size):
            for y in range (self.size):
                if self.board[x][y] == -1:
                    black += 1
                elif self.board[x][y] == 1:
                    white += 1
        return (black, white)


        
    
