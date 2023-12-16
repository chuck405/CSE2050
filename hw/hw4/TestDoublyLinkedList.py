from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    def test_contains(self):
        'checks if the __contains__() method works properly'
        # initializes DLL with values 1-9 for testing
        dll = DLL(range(10))

        # asserts that DLL contains values 1-9
        for i in range(10):
            self.assertTrue(i in dll)

        # asserts that DLL does not contain values 10-19
        for i in range(10, 20):
            self.assertFalse(i in dll)

        # asserts that DLL contains newly added values
        dll.add_first(20)
        dll.add_last(21)
        for i in range(20, 22):
            self.assertTrue(i in dll)

    def test_neighbors(self):
        'checks if the neighbors() method works properly'
        # initializes DLL with values 1-9 for testing
        dll = DLL(range(10))

        # asserts that neighbors for items not in the DLL will raise RuntimeError
        with self.assertRaises(RuntimeError):
            for i in range(10,20):
                dll.neighbors(i)

        # asserts that neighbors for the DLL's head return "None" and the next node's item
        self.assertEqual(dll.neighbors(0), (None, 1))

        # asserts that neighbors for the DLL's tail return the previous node's item and "None"
        self.assertEqual(dll.neighbors(9), (8, None))
        
        # asserts that neighbors for every DLL item from 1-8 returns the previous node's item and the next node's item
        for i in range(1,9):
            self.assertEqual(dll.neighbors(i), (i-1, i+1))

    def test_remove_item(self):
        'checks if the remove_node() method works properly'
        # initializes DLL with values 1-9 for testing
        dll = DLL(range(10))

        # asserts that removing nodes not in the DLL will raise RuntimeError
        with self.assertRaises(RuntimeError):
            for i in range(10,20):
                dll.remove_node(i)

        # asserts that removing the head returns the head's item and sets the new head to the next node
        self.assertEqual(dll.remove_node(0), 0)
        self.assertEqual(dll._head.item, 1)

        # asserts that removing the tail returns the tail's item and sets the new tail to the previous node
        self.assertEqual(dll.remove_node(9), 9)
        self.assertEqual(dll._tail.item, 8)

        # asserts that removing any DLL node 1-8 returns the node's item and attaches the adjacent nodes to each other
        for i in range(1,9):
            dll = DLL(range(10))
            self.assertEqual(dll.remove_node(i), i)
            self.assertEqual(dll._nodes[i-1]._next.item, i+1)
            self.assertEqual(dll._nodes[i+1]._prev.item, i-1)

unittest.main()
