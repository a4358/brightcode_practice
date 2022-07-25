from Board import Board
from BoardView import BoardView

field = Board(8)
#field.make_move((4,3))
#field.make_move((5,3))
BoardView.draw_board(field)
print(field.list_affected((4,3),-1))
