from xmlrpc.client import Boolean
from Player import Player
from Board import Board
from copy import deepcopy


class AiPlayerComplicated(Player):
    def __init__(self, playertype: int) -> None:
        super().__init__(playertype)

    def prompt_move(self, board: Board):
        """decides which move to make in the current situation

        Args:
            board (Board): current game state

        Returns:
            Tuple: coordinates of the piece placed
        """
        depth = 5  # decides how many layers in to look
        max_utility = -2000
        for x in range(board.size):
            for y in range(board.size):
                if board.board[x][y] == 0 and board.list_affected((x, y), self.playertype):
                    result_board = deepcopy(board)
                    result_board.make_move((x, y))
                    move_utility = self.minimax(result_board, False, depth)
                    if move_utility > max_utility:
                        max_utility = move_utility
                        bestmove = (x, y)

        Player.currentplayer *= -1
        print(
            f'The AI makes a move! {bestmove[0]+1, bestmove[1]+1} expected value: {max_utility}')

        return (int(bestmove[0]), int(bestmove[1]))

    def minimax(self, hyp_board: Board, is_max_players_turn, depth) -> int:
        """recursive function to find the maximum utility that can result from a board state

        Args:
            hyp_board (Board): the hypothetical board the current layer is considering for utility
            is_max_players_turn (bool): whether the turn on this layer is made by the for or the optimizing player
            depth (int): how many layers in should the algorithm look
        Returns:
            int: predicted utility resulting from the move (not absolute due to likely early cutoff, assumes opponent plays naively)
        """
        if not (hyp_board.moves_exist()):
            result_board: Board = deepcopy(hyp_board)
            result_board.skip_move()
            if not (result_board.moves_exist()):  # true endgame state, neither player can move
                # get count of pieces (not utility) in an endgame state
                pieces_count = hyp_board.report_pieces(self.playertype)
                if pieces_count > 0:
                    return 1000  # total victory
                if pieces_count < 0:
                    return -1000  # irrecoverable loss
            else:  # a player can not make a move right now, but the game is not over
                # these branches warrant deeper examination, so depth is not reduced
                return self.minimax(result_board, not is_max_players_turn, depth)

        if depth == 0:
            return hyp_board.evaluation(self.playertype)

        if is_max_players_turn == True:
            max_utility = -2000
            for x in range(hyp_board.size):
                for y in range(hyp_board.size):
                    if hyp_board.board[x][y] == 0 and hyp_board.list_affected((x, y), self.playertype):
                        result_board = deepcopy(hyp_board)
                        result_board.make_move((x, y))
                        move_utility = self.minimax(
                            result_board, False, depth - 1)
                        max_utility = max(max_utility, move_utility)
            return max_utility

        if is_max_players_turn == False:
            min_utility = 2000
            for x in range(hyp_board.size):
                for y in range(hyp_board.size):
                    if hyp_board.board[x][y] == 0 and hyp_board.list_affected((x, y), self.playertype*-1):
                        result_board = deepcopy(hyp_board)
                        result_board.make_move((x, y))
                        move_utility = self.minimax(
                            result_board, True, depth - 1)
                        min_utility = min(min_utility, move_utility)
            return min_utility
