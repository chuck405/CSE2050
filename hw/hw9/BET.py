from itertools import permutations, product

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def pre_order(self):
        """Pre-Order generator used for evaluate() and __repr__()"""
        yield self.value
        if self.left is not None: yield from self.left.pre_order()
        if self.right is not None: yield from self.right.pre_order()

    def add_left(self, node):
        """Adds node as the left child"""
        self.left = node

    def add_right(self, node):
        """Adds node as the right child"""
        self.right = node

    def evaluate(self):
        """Recursively evaluates the subtree rooted at this BETNode"""
        for node in self.pre_order():
            # if the element is a card value, then simply returns that value
            if node in BETNode.CARD_VAL_DICT: return BETNode.CARD_VAL_DICT[node]
            # if the element is an operator, calls the evaluate method for the left and right child nodes
            elif node == "+": return self.left.evaluate() + self.right.evaluate()
            elif node == "-": return self.left.evaluate() - self.right.evaluate()
            elif node == "*": return self.left.evaluate() * self.right.evaluate()
            elif node == "/": 
                if self.right.evaluate() != 0: return self.left.evaluate() / self.right.evaluate()
                # if dividing by 0, returns a large negative number
                else: return -9999
                

    def __repr__(self):
        """Displays the expression stored in the BET using infix notation"""
        for node in self.pre_order():
            # if the element is a card value, then simply returns the element
            if node in BETNode.CARD_VAL_DICT: return node
            # if the element is an operator, calls the __repr__ method for the left and right child nodes
            elif node in BETNode.OPERATORS: return "(" + str(self.left.__repr__()) + str(node) + str(self.right.__repr__()) + ")"

def create_trees(cards):
    """Returns a set of every valid tree for a given collection of 4 cards"""
    tree_set = set()
    # iterates over every permutation of card orders
    for i in permutations(cards):
        # iterates over every permutation of 3-operator possibilities
        for j in product(["+", "-", "*", "/"], repeat=3):
            # adds a tree using the "CCXCCXX" shape
            root = BETNode(str(j[0]))
            root.add_left(BETNode(str(j[1])))
            root.add_right(BETNode(str(j[2])))
            root.left.add_left(BETNode(str(i[0])))
            root.left.add_right(BETNode(str(i[1])))
            root.right.add_left(BETNode(str(i[2])))
            root.right.add_right(BETNode(str(i[3])))
            tree_set.add(root)
            # adds a tree using the "CCXCXCX" shape
            root = BETNode(str(j[0]))
            root.add_left(BETNode(str(j[1])))
            root.add_right(BETNode(str(i[0])))
            root.left.add_left(BETNode(str(j[2])))
            root.left.add_right(BETNode(str(i[1])))
            root.left.left.add_left(BETNode(str(i[2])))
            root.left.left.add_right(BETNode(str(i[3])))
            tree_set.add(root)
            # adds a tree using the "CCCXXCX" shape
            root = BETNode(str(j[0]))
            root.add_left(BETNode(str(j[1])))
            root.add_right(BETNode(str(i[0])))
            root.left.add_left(BETNode(str(i[1])))
            root.left.add_right(BETNode(str(j[2])))
            root.left.right.add_left(BETNode(str(i[2])))
            root.left.right.add_right(BETNode(str(i[3])))
            tree_set.add(root)
            # adds a tree using the "CCCXCXX" shape
            root = BETNode(str(j[0]))
            root.add_left(BETNode(str(i[0])))
            root.add_right(BETNode(str(j[1])))
            root.right.add_left(BETNode(str(j[2])))
            root.right.add_right(BETNode(str(i[1])))
            root.right.left.add_left(BETNode(str(i[2])))
            root.right.left.add_right(BETNode(str(i[3])))
            tree_set.add(root)
            # adds a tree using the "CCCCXXX" shape
            root = BETNode(str(j[0]))
            root.add_left(BETNode(str(i[0])))
            root.add_right(BETNode(str(j[1])))
            root.right.add_left(BETNode(str(i[1])))
            root.right.add_right(BETNode(str(j[2])))
            root.right.right.add_left(BETNode(str(i[2])))
            root.right.right.add_right(BETNode(str(i[3])))
            tree_set.add(root)
    return tree_set


def find_solutions(cards):
    """Returns a set of all the ways to get 24"""
    solution_set = set()
    # calls create_trees(cards) to get all valid trees for a passed in 4-card hand
    for i in create_trees(cards):
        # evaluates each tree and stores the string representation
        if i.evaluate() == 24: solution_set.add(i.__repr__())
    return solution_set