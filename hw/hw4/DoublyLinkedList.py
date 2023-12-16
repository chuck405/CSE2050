# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        
        # adds item:node pair to dictionary
        self._nodes[item] = self._head

        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head

    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1

        # adds item:node pair to dictionary
        self._nodes[item] = self._tail
        
        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail

    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item
        
        # removes item:node pair from dictionary
        del self._nodes[item]

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None

        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item
        
        # removes item:node pair from dictionary
        del self._nodes[item]

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        return item
        
    def __contains__(self, item):
        'checks if the DLL contains the item'
        # checks if the item can be found in the dictionary's keys; if yes, returns True
        if item in self._nodes.keys(): return True

        # if no, returns False
        else: return False

    def neighbors(self, item):
        'returns the items immediately before and after the node with item'
        # raise a RuntimeError if searching for an item not in the DLL
        if self.__contains__(item) == False: raise RuntimeError
        
        # accesses the item's node and stores for later
        current_node = self._nodes[item]
        
        # if node is the DLL's head, returns only "None" along with the next node's item
        if current_node == self._head: return (None, current_node._next.item)
        
        # if node is the DLL's tail, returns only the previous node's item along with "None"
        elif current_node == self._tail: return (current_node._prev.item, None)
        
        # if node is neither, returns the items in the node immediately before and after
        else: return (current_node._prev.item, current_node._next.item)

    def remove_node(self, item):
        'removes the node containing an item from the DLL'
        # raise a RuntimeError if removing an item not in the DLL
        if self.__contains__(item) == False: raise RuntimeError
        
        # accesses the item's node and stores for later
        current_node = self._nodes[item]
        
        # if node is the DLL's head, simply calls remove_first()
        if current_node == self._head: return self.remove_first()

        # if node is the DLL's tail, simply calls remove_last()
        elif current_node == self._tail: return self.remove_last()

        # if node is neither, attaches the adjacent nodes, deletes the node from the dictionary, changes the DLL's length, and returns the item
        else: 
            current_node._prev._next = current_node._next
            current_node._next._prev = current_node._prev
            del self._nodes[item]
            self._len -= 1
            return item