from Board import Board
from BoardView import BoardView
from Player import Player
from AiPlayerEasy import AiPlayerEasy
from AiPlayerComplicated import AiPlayerComplicated
class GameLogic:
    def __init__(self) -> None:
        pass
    def initialise_pvp(self,size):
        """sets up the board for a two-player game

        Args:
            size (int): size of the board desired

        Raises:
            ValueError: rasied if size is not supported
        """
        if (type(size)!= int or size <=0):
            raise ValueError
        self.game_field = Board(size)
        self.player_white = Player(1)
        self.player_black = Player(-1)
    
    def initialise_ai(self,size):
        """sets up the board for a one-player game against a simple ai
           the ai plays as white

        Args:
            size (int): size of the board desired

        Raises:
            ValueError: rasied if size is not supported
        """
        if (type(size)!= int or size <=0):
            raise ValueError
        self.game_field = Board(size)
        self.player_white = AiPlayerEasy(1)
        self.player_black = Player(-1)
    
    def initialise_ai_minimax(self,size):
        """sets up the board for a one-player game against an ai based on the minimax algorithm
           the ai plays as white

        Args:
            size (int): size of the board desired

        Raises:
            ValueError: rasied if size is not supported
        """
        if (type(size)!= int or size <=0):
            raise ValueError
        self.game_field = Board(size)
        self.player_white = AiPlayerComplicated(1)
        self.player_black = Player(-1)


    def begin_game(self):
        """initiates the game and runs it's core loop
        """

        BoardView.draw_board(self.game_field)

        skipcount = 0
        while (skipcount < 2):
            if (self.game_field.moves_exist()):
                skipcount = 0
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
                skipcount += 1

        BoardView.end_screen(self.game_field.report_pieces(),self.game_field)
