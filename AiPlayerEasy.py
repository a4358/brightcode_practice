from Player import Player


class AiPlayerEasy(Player):
    def __init__(self, playertype: int) -> None:
        super().__init__(playertype)

    def prompt_move(self, board):
        """decides which move to make in the current situation

        Args:
            board (Board): current game state

        Returns:
            Tuple: coordinates of the piece placed
        """
        moves = dict()
        for x in range(board.size):
            for y in range(board.size):
                if board.board[x][y] == 0:
                    move_weight = len(board.list_affected(
                        (x, y), board.nextplayer))
                    if(move_weight):
                        xy = (x, y)
                        moves[xy] = move_weight
        bestmove = max(moves, key=moves.get)
        Player.currentplayer *= -1
        print(f'The AI makes a move! expected value: {moves.get(bestmove)}')
        return (int(bestmove[0]), int(bestmove[1]))
