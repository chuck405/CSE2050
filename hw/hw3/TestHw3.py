import unittest
from hw3 import find_pairs_naive, find_pairs_optimized, measure_min_time 

class Testhw3(unittest.TestCase):
    def test_find_pairs_naive(self):
        # Initializes lists and targets to be used for testing
        test_list1 = [0, 20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10, 10, 11, 9, 12, 8, 13, 7, 14, 6, 15, 5, 16, 4, 17, 3, 18, 2, 19, 1, 20, 0]
        test_list2 = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10, 10, 11, 9, 12, 8, 13, 7, 14, 6, 15, 5, 16, 4, 17, 3, 18, 2, 19, 1, 20]
        test_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_list4 = []
        test_target1 = 20
        test_target2 = 0
        test_target3 = 10
        # Standard test case
        self.assertSetEqual(find_pairs_naive(test_list1, test_target1), {(0, 20), (1, 19), (2, 18), (3, 17), (4, 16), (5, 15), (6, 14), (7, 13), (8, 12), (9, 11), (10, 10)})
        # Test case with target = 0
        self.assertSetEqual(find_pairs_naive(test_list2, test_target2), set())
        # Test case with expected duplicate values as the target
        self.assertSetEqual(find_pairs_naive(test_list3, test_target1), set())
        # Test case with empty list
        self.assertSetEqual(find_pairs_naive(test_list4, test_target1), set())
        # Test case with target that equals to double number
        self.assertSetEqual(find_pairs_naive(test_list3, test_target3), {(1, 9), (2, 8), (3, 7), (4, 6)})


    def test_find_pairs_optimized(self):
        # Initializes lists and targets to be used for testing
        test_list1 = [0, 20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10, 10, 11, 9, 12, 8, 13, 7, 14, 6, 15, 5, 16, 4, 17, 3, 18, 2, 19, 1, 20, 0]
        test_list2 = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10, 10, 11, 9, 12, 8, 13, 7, 14, 6, 15, 5, 16, 4, 17, 3, 18, 2, 19, 1, 20]
        test_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_list4 = []
        test_target1 = 20
        test_target2 = 0
        test_target3 = 10
        # Standard test case
        self.assertSetEqual(find_pairs_optimized(test_list1, test_target1), {(0, 20), (1, 19), (2, 18), (3, 17), (4, 16), (5, 15), (6, 14), (7, 13), (8, 12), (9, 11), (10, 10)})
        # Test case with target = 0
        self.assertSetEqual(find_pairs_optimized(test_list2, test_target2), set())
        # Test case with expected duplicate values as the target
        self.assertSetEqual(find_pairs_optimized(test_list3, test_target1), set())
        # Test case with empty list
        self.assertSetEqual(find_pairs_optimized(test_list4, test_target1), set())
        # Test case with target that equals to double number
        self.assertSetEqual(find_pairs_optimized(test_list3, test_target3), {(1, 9), (2, 8), (3, 7), (4, 6)})


    def test_measure_min_time(self):
        # Test case asserting that find_pairs_naive takes more time to run than find_pairs_optimized
        self.assertGreater(measure_min_time(find_pairs_naive, (list(range(100)), 1)), measure_min_time(find_pairs_optimized, (list(range(100)), 1)))
        # Test case asserting that measure_min_time(find_pairs_naive) returns a float
        self.assertIsInstance(measure_min_time(find_pairs_naive, (list(range(10)), 1)), float)
        # Test case asserting that measure_min_time(find_pairs_optimized) returns a float
        self.assertIsInstance(measure_min_time(find_pairs_optimized, (list(range(10)), 1)), float)


if __name__ == "__main__":
    unittest.main()