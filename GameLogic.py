from Board import Board
from BoardView import BoardView
from Player import Player
from AiPlayerEasy import AiPlayerEasy
from AiPlayerComplicated import AiPlayerComplicated
class GameLogic:
    def __init__(self) -> None:
        pass
    def initialise(self,size):
        if (type(size)!= int or size <=0):
            raise ValueError
        self.game_field = Board(size)
        self.player_white = Player(1)
        self.player_black = Player(-1)
    
    def initialise_ai(self,size):
        if (type(size)!= int or size <=0):
            raise ValueError
        self.game_field = Board(size)
        self.player_white = AiPlayerEasy(1)
        self.player_black = Player(-1)
    
    def initialise_ai_minimax(self,size):
        if (type(size)!= int or size <=0):
            raise ValueError
        self.game_field = Board(size)
        self.player_white = AiPlayerComplicated(1)
        self.player_black = Player(-1)


    def begin_game(self):

        BoardView.draw_board(self.game_field)

        skipflag = 0
        while (skipflag < 2):
            if (self.game_field.moves_exist()):
                skipflag = 0
                try:
                    if self.game_field.nextplayer < 0:
                        self.game_field.make_move(self.player_black.prompt_move(self.game_field))
                    else:
                        self.game_field.make_move(self.player_white.prompt_move(self.game_field))
                except: 
                    BoardView.invalid_move_comment()
                    continue
                BoardView.draw_board(self.game_field)
            else:
                self.game_field.skip_move()
                skipflag += 1

        BoardView.end_screen(self.game_field.report_pieces(),self.game_field)
