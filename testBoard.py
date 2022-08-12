# test Board.py
from typing_extensions import assert_type
import unittest
from Board import Board


class TestBoard(unittest.TestCase):
    def test_affected(self):
        startboard = Board(4)
        self.assertEqual(startboard.list_affected((1, 0), -1), {(1, 1)})
        self.assertEqual(startboard.list_affected((0, 1), -1), {(1, 1)})
        self.assertEqual(startboard.list_affected((2, 3), -1), {(2, 2)})
        self.assertEqual(startboard.list_affected((3, 2), -1), {(2, 2)})
        startboard.make_move((1, 0))
        self.assertEqual(startboard.list_affected((0, 0), 1), {(1, 1)})
        startboard = Board(4)
        startboard.make_move((2, 3))
        self.assertEqual(startboard.list_affected((3, 3), 1), {(2, 2)})
        startboard = Board(4)
        startboard.board = [[0, 0, 0, -1],
                            [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(startboard.list_affected(
            (3, 0), -1), {(1, 2), (2, 1)})
        startboard.board = [[0, 0, 0, 0], [
            0, 1, 1, 0], [0, 1, 1, 0], [-1, 0, 0, 0]]
        self.assertEqual(startboard.list_affected(
            (0, 3), -1), {(1, 2), (2, 1)})

    def test_moves(self):
        startboard = Board(4)
        player = startboard.nextplayer
        self.assertEqual(Board.return_board(startboard), [
                         [0, 0, 0, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, 0, 0, 0]])
        startboard.make_move((1, 0))
        self.assertEqual(int(startboard.nextplayer), player*-1)
        startboard.make_move((0, 0))
        self.assertEqual(Board.return_board(startboard), [
                         [1, 0, 0, 0], [-1, 1, -1, 0], [0, -1, 1, 0], [0, 0, 0, 0]])
        self.assertEqual(startboard.nextplayer, player)
        startboard.skip_move()
        self.assertEqual(startboard.nextplayer, player*-1)

    def test_illegal_move(self):
        startboard = Board(4)
        with self.assertRaises(ValueError):
            startboard.make_move((0, 0))
        with self.assertRaises(IndexError):
            startboard.make_move((999999, 99999))

    def test_utility_counters(self):
        startboard = Board(4)
        startboard.board = [[1, 1, 1, -1],
                            [1, 1, -1, 1], [1, -1, 1, 0], [0, 0, -1, 1]]
        self.assert_type(startboard.evaluation(startboard.nextplayer), int)
        self.assertEqual(startboard.report_pieces(), (4, 9))

    def test_moves_exist(self):
        startboard = Board(4)
        startboard.board = [[1, 1, 1, -1],
                            [1, 1, -1, 1], [1, -1, 1, 0], [0, 0, -1, 1]]
        self.assertTrue(startboard.moves_exist())
        startboard.board = [[1, 1, 1, -1], [1, 1, -1, -1],
                            [1, -1, -1, -1], [-1, 1, 1, 1]]
        self.assertFalse(startboard.moves_exist())
