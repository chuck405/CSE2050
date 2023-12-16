from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase):
    """
    Test cases specific to the Card class
    """
    def test_init(self):
        """
        Test cases specific to the __init__ method
        """
        # Asserts that c1's value and c2's suit are equal to what was expected
        self.assertEqual(c1.value, 3)
        self.assertEqual(c2.suit, "spades")

    def test_repr(self):
        """
        Test cases specific to the __repr__ method
        """
        # Asserts that repr(c1) and repr(c2) return what was expected
        self.assertEqual(repr(c1), "'Card(3 of hearts)'")
        self.assertEqual(repr(c2), "'Card(4 of spades)'")

    def test_lt(self):
        """
        Test cases specific to the __lt__ method
        """
        # Asserts that c1 < c2 returns what was expected (True) and c3 < c1 returns what was expected (False)
        self.assertTrue(c1 < c2)
        self.assertFalse(c3 < c1)

    def test_eq(self):
        """
        Test cases specific to the __eq__ method
        """
        # Asserts that c1 == c3 returns what was expected (True) and c1 == c2 returns what was expected (False)
        self.assertTrue(c1 == c3)
        self.assertFalse(c1 == c2)


class TestDeck(unittest.TestCase):
    """
    Test cases specific to the Deck class
    """
    def test_init(self):
        """
        Test cases specific to the __init__ method
        """
        # Asserts that d1's values and suits and d2's values and suits are equal to what was expected
        self.assertEqual(d1.values, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEqual(d2.values, [2,1])
        self.assertEqual(d1.suits, ["clubs", "diamonds", "hearts", "spades"])
        self.assertEqual(d2.suits, ["triangles", "dots"])

    def test_len(self):
        """
        Test cases specific to the __len__ method
        """
        # Asserts that len(d1) and len(d2) return what was expected
        self.assertEqual(len(d1), 52)
        self.assertEqual(len(d2), 4)

    def test_repr(self):
        """
        Test cases specific to the __repr__ method
        """
        # Asserts that repr(d1) and repr(d2) return what was expected
        self.assertEqual(repr(d1), '"Deck: ' + str(d1.card_list) + '"')
        self.assertEqual(repr(d2), '"Deck: ' + str(d2.card_list) + '"')

    def test_sort(self):
        """
        Test cases specific to the sort method
        """
        # Asserts that d1.sort() and d2.sort() return what was expected
        self.assertEqual(d1.sort(), ['Card(1 of clubs)', 'Card(1 of diamonds)', 'Card(1 of hearts)', 'Card(1 of spades)', 'Card(10 of clubs)', 'Card(10 of diamonds)', 'Card(10 of hearts)', 'Card(10 of spades)', 'Card(11 of clubs)', 'Card(11 of diamonds)', 'Card(11 of hearts)', 'Card(11 of spades)', 'Card(12 of clubs)', 'Card(12 of diamonds)', 'Card(12 of hearts)', 'Card(12 of spades)', 'Card(13 of clubs)', 'Card(13 of diamonds)', 'Card(13 of hearts)', 'Card(13 of spades)', 'Card(2 of clubs)', 'Card(2 of diamonds)', 'Card(2 of hearts)', 'Card(2 of spades)', 'Card(3 of clubs)', 'Card(3 of diamonds)', 'Card(3 of hearts)', 'Card(3 of spades)', 'Card(4 of clubs)', 'Card(4 of diamonds)', 'Card(4 of hearts)', 'Card(4 of spades)', 'Card(5 of clubs)', 'Card(5 of diamonds)', 'Card(5 of hearts)', 'Card(5 of spades)', 'Card(6 of clubs)', 'Card(6 of diamonds)', 'Card(6 of hearts)', 'Card(6 of spades)', 'Card(7 of clubs)', 'Card(7 of diamonds)', 'Card(7 of hearts)', 'Card(7 of spades)', 'Card(8 of clubs)', 'Card(8 of diamonds)', 'Card(8 of hearts)', 'Card(8 of spades)', 'Card(9 of clubs)', 'Card(9 of diamonds)', 'Card(9 of hearts)', 'Card(9 of spades)'])
        self.assertEqual(d2.sort(), ['Card(1 of dots)', 'Card(1 of triangles)', 'Card(2 of dots)', 'Card(2 of triangles)'])

    def test_shuffle(self):
        """
        Test cases specific to the shuffle method
        """
        # Asserts that d1.shuffle() and d2.shuffle() return a new order of cards that is not equal to the original
        self.assertNotEqual(d1.shuffle(), ['Card(1 of clubs)', 'Card(1 of diamonds)', 'Card(1 of hearts)', 'Card(1 of spades)', 'Card(2 of clubs)', 'Card(2 of diamonds)', 'Card(2 of hearts)', 'Card(2 of spades)', 'Card(3 of clubs)', 'Card(3 of diamonds)', 'Card(3 of hearts)', 'Card(3 of spades)', 'Card(4 of clubs)', 'Card(4 of diamonds)', 'Card(4 of hearts)', 'Card(4 of spades)', 'Card(5 of clubs)', 'Card(5 of diamonds)', 'Card(5 of hearts)', 'Card(5 of spades)', 'Card(6 of clubs)', 'Card(6 of diamonds)', 'Card(6 of hearts)', 'Card(6 of spades)', 'Card(7 of clubs)', 'Card(7 of diamonds)', 'Card(7 of hearts)', 'Card(7 of spades)', 'Card(8 of clubs)', 'Card(8 of diamonds)', 'Card(8 of hearts)', 'Card(8 of spades)', 'Card(9 of clubs)', 'Card(9 of diamonds)', 'Card(9 of hearts)', 'Card(9 of spades)', 'Card(10 of clubs)', 'Card(10 of diamonds)', 'Card(10 of hearts)', 'Card(10 of spades)', 'Card(11 of clubs)', 'Card(11 of diamonds)', 'Card(11 of hearts)', 'Card(11 of spades)', 'Card(12 of clubs)', 'Card(12 of diamonds)', 'Card(12 of hearts)', 'Card(12 of spades)', 'Card(13 of clubs)', 'Card(13 of diamonds)', 'Card(13 of hearts)', 'Card(13 of spades)'])
        self.assertNotEqual(d2.shuffle(), ['Card(2 of triangles)', 'Card(2 of dots)', 'Card(1 of triangles)', 'Card(1 of dots)'])

    def test_draw_top(self):
        """
        Test cases specific to the draw_top method
        """
        # Defines instance variables so that d1 and d2 are not affected in other test functions
        d1 = Deck()
        d2 = Deck([2, 1], ["triangles", "dots"])
        # Asserts that drawing too many cards from d1 will raise a RuntimeError because d1 will run out of cards
        with self.assertRaisesRegex(RuntimeError, "Cannot draw from an empty deck"):
            for i in range(0, len(d1.card_list) + 1):
                d1.draw_top()
        # Asserts that d2.draw_top() returns what was expected
        self.assertEqual(d2.draw_top(), "Card(1 of dots)")


class TestHand(unittest.TestCase):
    """
    Test cases specific to the Hand class
    """
    def test_init(self):
        """
        Test cases specific to the __init__ method
        """
        # Asserts that h_clubs' card_list is equal to what was expected
        self.assertEqual(h_clubs.card_list, [Card(5, 'clubs'), Card(4, 'clubs'), Card(3, 'clubs'), Card(2, 'clubs'), Card(1, 'clubs')])

    def test_repr(self):
        """
        Test cases specific to the __repr__ method
        """
        # Asserts that repr(h_clubs) returns what was expected
        self.assertEqual(repr(h_clubs), '"Hand: ' + str(h_clubs.card_list) + '"')

    def test_play(self):
        """
        Test cases specific to the play method
        """
        # Asserts that playing a card not in the hand raises a RuntimeError
        with self.assertRaises(RuntimeError):
            h_clubs.play(Card(1, "spades"))
        # Asserts that playing a card in the hand returns what was expected
        self.assertEqual(h_clubs.play(Card(1, "clubs")), Card(1, "clubs"))

# Ensures that the code in TestCards.py is being run as a script
if __name__ == "__main__":
    # Defines variables c1, c2, c3, d1, d2, and h_clubs to be used for unittests
    c1 = Card(3, "hearts")
    c2 = Card(4, "spades")
    c3 = Card(3, "hearts")
    d1 = Deck()
    d2 = Deck([2, 1], ["triangles", "dots"])
    h_clubs = Hand([Card(value, 'clubs') for value in range(5, 0, -1)])
    # Provides a command-line interface to the test script
    unittest.main()