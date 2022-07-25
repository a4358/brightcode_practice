from Board import Board
from BoardView import BoardView
class GameLogic:
    def __init__(self) -> None:
        pass
    def initialise(self,size):
        if (type(size)!= int or size <=0):
            raise ValueError
        self.field = Board(size)

    def begin_game(self):

        BoardView.draw_board(self.field)

        skipflag = 0
        while (skipflag < 2):
            if (self.field.moves_exist()):
                skipflag = 0
                try:
                    self.field.make_move(BoardView.prompt_move(self.field))
                except: 
                    BoardView.invalid_move_comment()
                    continue
                BoardView.draw_board(self.field)
            else:
                self.field.skip_move()
                skipflag += 1

        BoardView.end_screen(self.field.report_pieces())
