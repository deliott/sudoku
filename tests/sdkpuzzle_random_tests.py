"""
sdksolver_stress_unit_tests.py
"stress tests" sdk solver with 10's of thousand valid solved and unsolved puzzles
read from file
:created on: 20160616
__author__ = 'Frederic Dupont'
:License: GPL3
"""

import random
import unittest

from sudoku.sdkpuzzle import make_grid_from_string
from tests import test_data


class TestFromDataPuzzlesRandomized(unittest.TestCase):
    """stress tests of Puzzle with a large number of solved and unsolved puzzles
    """

    # TODO: add stress tests for invalid solved and unsolved puzzles

    def setUp(self):
        self.path = 'resources/'
        self.picked_tests = list(range(10000))
        random.shuffle(self.picked_tests)
        self.picked_tests = self.picked_tests[:1000]

    def test_valid_solved_puzzle(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_solved_data = test_data.get_data_from(self.path + 'solved_10000_grids_startwith_123456789.txt')
        num_tests = len(valid_solved_data)
        for idx in self.picked_tests:
            if idx >= num_tests:
                continue
            else:
                puzzle = make_grid_from_string(valid_solved_data[idx])
                result = puzzle.is_valid_grid()
                self.assertTrue(result)

    def test_valid_unsolved_puzzle_45_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = test_data.get_data_from(self.path + 'unsolved_10000_grids_45_numbers.txt')
        num_tests = len(valid_unsolved_data)
        for idx in self.picked_tests:
            if idx >= num_tests:
                continue
            else:
                puzzle = make_grid_from_string(valid_unsolved_data[idx])
                result = puzzle.is_valid_grid()
                self.assertTrue(result)

    def test_valid_unsolved_puzzle_40_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = test_data.get_data_from(self.path + 'unsolved_10000_grids_40_numbers.txt')
        num_tests = len(valid_unsolved_data)
        for idx in self.picked_tests:
            if idx >= num_tests:
                continue
            else:
                puzzle = make_grid_from_string(valid_unsolved_data[idx])
                result = puzzle.is_valid_grid()
                self.assertTrue(result)

    def test_valid_unsolved_puzzle_35_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = test_data.get_data_from(self.path + 'unsolved_10000_grids_35_numbers.txt')
        num_tests = len(valid_unsolved_data)
        for idx in self.picked_tests:
            if idx >= num_tests:
                continue
            else:
                puzzle = make_grid_from_string(valid_unsolved_data[idx])
                result = puzzle.is_valid_grid()
                self.assertTrue(result)

    def test_valid_unsolved_puzzle_30_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = test_data.get_data_from(self.path + 'unsolved_10000_grids_30_numbers.txt')
        num_tests = len(valid_unsolved_data)
        for idx in self.picked_tests:
            if idx >= num_tests:
                continue
            else:
                puzzle = make_grid_from_string(valid_unsolved_data[idx])
                result = puzzle.is_valid_grid()
                self.assertTrue(result)

    def test_valid_unsolved_puzzle_25_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = test_data.get_data_from(self.path + 'unsolved_10000_grids_25_numbers.txt')
        num_tests = len(valid_unsolved_data)
        for idx in self.picked_tests:
            if idx >= num_tests:
                continue
            else:
                puzzle = make_grid_from_string(valid_unsolved_data[idx])
                result = puzzle.is_valid_grid()
                self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()