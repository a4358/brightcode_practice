class Board:
    # 0 is empty, -1 is black, 1 is white
    def __init__(self,size) -> None:
        self.board = [[0 for _ in range(0, size)] for _a in range (0, size)]
        self.size = size
    
    def return_board(self):
        return self.board