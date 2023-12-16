import unittest
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort, magic_sort 

# also imports the global algorithms set
from MagicSort import algorithms

class Test_linear_scan(unittest.TestCase):
    def test_linear_scan(self):
        """Test case for linear_scan"""
        L1, L2 = [], []
        # test case for empty list
        self.assertEqual(linear_scan(L1), None)
        L3 = [0, 2, 1, 4, 3, 5, 4, 7, 6]
        L4 = [0, 2, 1, 4, 3, 5, 4, 7, 6, 9, 8, 11, 10]
        for i in range(100):
            L1.append(i)
            L2.append(-i)
        # test cases for sorted list, reverse list, list with 5 errors, list with over 5 errors
        self.assertEqual(linear_scan(L1), None)
        self.assertEqual(linear_scan(L2), "reverse_list")
        self.assertEqual(linear_scan(L3), "insertionsort")
        self.assertEqual(linear_scan(L4), "quicksort")

class Test_reverse_list(unittest.TestCase):
    def test_reverse_list(self):
        """Test case for reverse_list"""
        L1, L2 = [], []
        for i in range(100): 
            L1.append(-i)
            L2.append(-i)
        reverse_list(L1)
        # tests that the list has been sorted successfully
        self.assertEqual(L1, sorted(L1))
        # tests that the list contains the same elements before and after sorting
        self.assertCountEqual(L1, L2)

class Test_insertionsort(unittest.TestCase):
    def test_insertionsort(self):
        """Test case for insertionsort"""
        L1 = [0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13, 13, 12, 14, 11, 15, 10, 16, 9, 17, 8, 18, 7, 19, 6, 20, 5, 21, 4, 22, 3, 23, 2, 24, 1, 25, 0]
        L2 = L1[:]
        insertionsort(L1)
        # tests that the list has been sorted successfully
        self.assertEqual(L1, sorted(L1))
        # tests that the list contains the same elements before and after sorting
        self.assertCountEqual(L1, L2)

class Test_quicksort(unittest.TestCase):
    def test_quicksort(self):
        """Test case for quicksort"""
        L1 = [0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13, 13, 12, 14, 11, 15, 10, 16, 9, 17, 8, 18, 7, 19, 6, 20, 5, 21, 4, 22, 3, 23, 2, 24, 1, 25, 0]
        L2 = L1[:]
        quicksort(L1)
        # tests that the list has been sorted successfully
        self.assertEqual(L1, sorted(L1))
        # tests that the list contains the same elements before and after sorting
        self.assertCountEqual(L1, L2)

class Test_mergesort(unittest.TestCase):
    def test_mergesort(self):
        """Test case for mergesort"""
        L1 = [0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13, 13, 12, 14, 11, 15, 10, 16, 9, 17, 8, 18, 7, 19, 6, 20, 5, 21, 4, 22, 3, 23, 2, 24, 1, 25, 0]
        L2 = L1[:]
        mergesort(L1)
        # tests that the list has been sorted successfully
        self.assertEqual(L1, sorted(L1))
        # tests that the list contains the same elements before and after sorting
        self.assertCountEqual(L1, L2)

class Test_magicsort(unittest.TestCase):
    def test_magic_sort(self):
        """Test case for magic_sort"""
        L1 = [0, 25, 1, 24, 2, 23, 3, 22, 4, 21, 5, 20, 6, 19, 7, 18, 8, 17, 9, 16, 10, 15, 11, 14, 12, 13, 13, 12, 14, 11, 15, 10, 16, 9, 17, 8, 18, 7, 19, 6, 20, 5, 21, 4, 22, 3, 23, 2, 24, 1, 25, 0]
        L2, L3 = [], L1[:]
        # test case for empty list
        self.assertEqual(magic_sort(L2), {"None"})
        for i in range(100): L2.append(-i)
        L4 = L2[:]
        L5 = [0, 2, 1]
        # test case for complex list that ensures 3 different sorting algorithms were used
        self.assertSetEqual(magic_sort(L1), {"quicksort", "mergesort", "insertionsort"})
        # tests that the list contains the same elements before and after sorting
        self.assertCountEqual(L1, L3)
        # test case for simple list that ensures only 1 sorting algorithm was used
        self.assertSetEqual(magic_sort(L5), {"insertionsort"})
        # tests that the list contains the same elements before and after sorting
        self.assertCountEqual(L5, [0, 2, 1])
        # test case for reversed list
        self.assertSetEqual(magic_sort(L2), {"reverse_list"})
        # tests that the list contains the same elements before and after sorting
        self.assertCountEqual(L2, L4)
        
unittest.main()