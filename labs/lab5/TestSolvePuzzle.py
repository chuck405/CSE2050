from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                self.assertTrue(puzzle([2,0,4,0,0,0,1,2,0,7,0,0,0,0,0,0,0]))

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                self.assertTrue(puzzle([2,0,0,0,0,0,0,8,0,0,3,0,0,0,0,5,0]))

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                self.assertTrue(puzzle([4,0,6,0,2,0,0,9,5,0,3,0,0,3,0,0,0]))

        def testUnsolveable(self):
                """Tests an unsolveable board"""
                self.assertFalse(puzzle([2,0,4,0,0,0,5,8,0,0,0,2,0,0,0,2,0]))

unittest.main()