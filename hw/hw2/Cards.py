import random

class Card:
    def __init__(self, value, suit):
        """
        Initializer method for the Card class
        """
        # Defines instance variables for value and suit
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Magic method for the repr() function
        """
        # Returns information regarding a specific card's value and suit
        return repr("Card(" + str(self.value) + " of " + str(self.suit) + ")")

    def __lt__(self, other):
        """
        Magic method for the "<" operator
        """
        # If 2 cards have the same suit, compares the values and returns True or False
        if self.suit == other.suit:
            return self.value < other.value
        # If 2 cards have different suits, compares the suits alphabetically instead and returns True or False
        else:
            return self.suit < other.suit

    def __eq__(self, other):
        """
        Magic method for the "==" operator
        """
        # Checks that both the suit and value of 2 cards are equal to return True; otherwise returns False
        if self.value == other.value:
            return self.suit == other.suit
        else:
            return False


class Deck:
    def __init__(self, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], suits=["clubs", "diamonds", "hearts", "spades"]):
        """
        Initializer method for the Deck class with default values and suits parameters
        """
        # Defines instance variables for values, suits, and card_list
        self.values = values
        self.suits = suits
        self.card_list = []
        # Creates the deck's card_list based on the given parameters of values and suits
        for i in self.values:
            for j in self.suits:
                self.card_list.append("Card(" + str(i) + " of " + str(j) + ")")

    def __len__(self):
        """
        Magic method for the len() function
        """
        # Returns information regarding the deck's length
        return len(self.card_list)

    def __repr__(self):
        """
        Magic method for the repr() function
        """
        # Returns information showing all of the cards in the deck
        return repr("Deck: " + str(self.card_list))

    def sort(self):
        """
        Method for sorting the deck's card_list
        """
        # Sorts the order of the cards in the deck based on value then by suit
        self.card_list.sort()
        # Returns the newly sorted deck
        return self.card_list

    def shuffle(self):
        """
        Method for shuffling the deck's card_list
        """
        # Randomizes the order of the cards in the deck
        random.shuffle(self.card_list)
        # Returns the newly shuffled deck
        return self.card_list

    def draw_top(self):
        """
        Method for drawing the top card in the deck's card_list
        """
        # Raises a RuntimeError if the deck has no cards
        if len(self.card_list) == 0:
            raise RuntimeError("Cannot draw from an empty deck")
        # Returns the card at the top of the deck if the deck has at least 1 card
        else:
            return self.card_list.pop(-1)


class Hand(Deck):
    def __init__(self, card_list=[]):
        """
        Initalizer method for the Hand class
        """
        # Defines instance variable for card_list
        self.card_list = card_list

    def __repr__(self):
        """
        Magic method for the repr() function
        """
        # Returns information showing all of the cards in the hand
        return repr("Hand: " + str(self.card_list))

    def play(self, Card):
        """
        Method for playing a card in the hand's card_list
        """
        # Raises a RuntimeError if the card is not in the hand and shows which cards are in the hand
        if Card not in self.card_list:
            raise RuntimeError("Attempt to play " + str(Card) + " that is not in Hand: " + str(self.card_list))
        # Returns the card if the card is in the hand and removes the card from the hand
        else:
            self.card_list.remove(Card)
            return Card