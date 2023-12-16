import unittest
from waitlist import Waitlist, Time, Entry

class TestWaitlist(unittest.TestCase):
    def test_add_customer(self):
        """Tests that customers are added properly"""
        WL = Waitlist()
        for i in reversed(range(0,50)):
            WL.add_customer(i, Time(i, 00))
        # asserts that only valid times are added
        self.assertEqual(len(WL._entries), 24)
        # asserts the highest priority makes its way to the top of the heap
        self.assertEqual(WL._entries[0].name, 0)
            
    def test_peek(self):
        """Tests that customers can be peeked properly"""
        WL = Waitlist()
        for i in range(0, 24):
            WL.add_customer(i, Time(i, 00))
            # asserts the peeked customer has the highest priority
            self.assertEqual(WL.peek(), (0, Time(0, 00)))
        WL = Waitlist()
        for i in reversed(range(0,24)):
            WL.add_customer(i, Time(i, 00))
            # asserts the peeked customer has the highest priority
            self.assertEqual(WL.peek(), (i, Time(i, 00)))

    def test_seat_customer(self):
        """Tests that customers can be seated properly"""
        WL = Waitlist()
        for i in reversed(range(0, 24)):
            WL.add_customer(i, Time(i, 00))
        for i in range(0, 24):
            # asserts that the customer with the highest priority is always seated first
            self.assertEqual(WL.seat_customer(), (i, Time(i, 00)))

    def test_change_reservation(self):
        """Tests that customers' reservation times can be changed properly"""
        WL = Waitlist()
        for i in range(0, 24):
            WL.add_customer(i, Time(i, 1))
        WL.change_reservation(1, Time(00, 00))
        # asserts that the customer's position is moved forward
        self.assertEqual(WL._entries[0].name, 1)
        WL.change_reservation(1, Time(1, 1))
        # asserts that the customer's position is moved backwards
        self.assertEqual(WL._entries[1].name, 1)

unittest.main()