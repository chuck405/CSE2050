import unittest
from BET import BETNode, create_trees, find_solutions

class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        r"""String representation
               *
             /   \
            +     -
           / \   / \
          6   3 7   9
        """
        root = BETNode("*")
        root.add_left(BETNode('+'))
        root.add_right(BETNode('-'))
        root.left.add_left(BETNode('6'))
        root.left.add_right(BETNode('3'))
        root.right.add_left(BETNode('7'))
        root.right.add_right(BETNode('9'))
        self.assertEqual(root.evaluate(), -18)

    def test_evaluate_tree2(self): 
        r"""String representation
               +
              / \
             /   5
            / \
           2   -   
              / \
             4   4
           
        """
        root = BETNode("+")
        root.add_left(BETNode('/'))
        root.add_right(BETNode('5'))
        root.left.add_left(BETNode('2'))
        root.left.add_right(BETNode('-'))
        root.left.right.add_left(BETNode('4'))
        root.left.right.add_right(BETNode('4'))
        self.assertEqual(root.evaluate(), -9994)

class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        """test case for a normal hand"""
        hand = ["J", "7", "3", "K"]
        self.assertEqual(len(create_trees(hand)), 7680)

    def test_hand2(self):
        """test case for a hand with a duplicate"""
        hand = ["Q", "2", "2", "A"]
        self.assertEqual(len(create_trees(hand)), 3840)

class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        """test case for a hand with no solutions"""
        hand = ["A", "2", "2", "A"]
        self.assertEqual(len(find_solutions(hand)), 0)

    def test_A23Q(self):
        """test case for the A23Q hand"""
        hand = ["A", "2", "3", "Q"]
        self.assertEqual(len(find_solutions(hand)), 33)
        
unittest.main()