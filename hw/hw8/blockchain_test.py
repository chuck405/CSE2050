import unittest
from blockchain import Transaction, Block, Ledger, Blockchain
from hashmap import Hashmap

class TestTransaction(unittest.TestCase):
    def test_repr(self):
        """Tests that transactions can be printed properly"""
        # test cases for different transactions
        for i in range(25):
            T1 = Transaction(i, i*10, i*100)
            self.assertEqual(T1.__repr__(), str(i) + " paid " + str(i*100) + " to " + str(i*10))

    def test_eq(self): 
        """Tests that transactions can be compared properly"""
        # tests cases for equal and nonequal transactions
        for i in range(25):
            T1 = Transaction(i, i*10, i*100)
            T2 = Transaction(i, i*10, i*100)
            T3 = Transaction(i, i+10, i+100)
            self.assertTrue(T1 == T2)
            self.assertFalse(T1 == T3)


class TestBlock(unittest.TestCase):
    def test_add_transaction(self):
        """Tests that transactions can be added to the blocks properly"""
        B1 = Block()
        for i in range(25):
            T1 = Transaction(i, i*10, i*100)
            B1.add_transaction(T1)
        # test case to ensure the length has changed
        self.assertEqual(len(B1.transactions), 25)

    def test_hash(self):
        """Tests that blocks can be hashed properly"""
        # test case to ensure the hashing formula is correct
        for i in range(25):
            B1 = Block([Transaction(i*1, i*10, i*100)])
            self.assertEqual(hash(B1), hash(tuple([(i*1, i*10, i*100)])))

    def test_eq(self):
        """Tests that blocks can be compared properly"""
        B1, B2, B3 = Block(), Block(), Block()
        # test cases for equal and nonequal blocks
        for i in range(25):
            T1 = Transaction(i, i*10, i*100)
            B1.add_transaction(T1)
            B2.add_transaction(T1)
            self.assertTrue(B1 == B2)
            self.assertFalse(B1 == B3)


class TestLedger(unittest.TestCase):
    def test_has_funds(self):
        """Tests that user funds can be compared properly"""
        L1 = Ledger()
        # test case for non-existent user
        self.assertFalse(L1.has_funds(0, 100))
        # test cases for users with insufficient funds
        for i in range(100):
            L1._hashmap.add(i, i)
            self.assertFalse(L1.has_funds(i, 100))
        # test cases for users with sufficient funds
        for i in range(100, 200):
            L1._hashmap.add(i, i)
            self.assertTrue(L1.has_funds(i, 100))

    def test_deposit(self):
        """Tests that funds can be deposited to users properly"""
        L1 = Ledger()
        # test case for non-existent user
        self.assertFalse(L1.deposit("Bob", 100))
        L1._hashmap.add("Bob", 100)
        L1.deposit("Bob", 100)
        # test case to ensure funds were added
        self.assertEqual(L1._hashmap.get("Bob"), 200)

    def test_transfer(self):
        """Tests that funds can be transferred from users properly"""
        L1 = Ledger()
        # test case for non-existent user
        self.assertFalse(L1.deposit("Bob", 100))
        L1._hashmap.add("Bob", 100)
        L1.transfer("Bob", 100)
        # test case to ensure funds were subtracted
        self.assertEqual(L1._hashmap.get("Bob"), 0)

    def test_repr(self):
        """Tests that ledgers can be printed properly"""
        L1 = Ledger()
        L1._hashmap.add("Bob", 100)
        L1._hashmap.add("John", 1000)
        L1._hashmap.add("Tim", 10000)
        # test cases to ensure important information was included in the string
        self.assertTrue("User Bob's balance is: 100" in L1.__repr__())
        self.assertTrue("User John's balance is: 1000" in L1.__repr__())
        self.assertTrue("User Tim's balance is: 10000" in L1.__repr__())


class TestBlockchain(unittest.TestCase):   
    def test_add_block(self):
        """Tests that blocks can be added to the blockchains properly"""
        BC1 = Blockchain()
        # test cases for successfully added blocks that also ensure transactions were carried out
        for i in range(1, 25):
            BC1._bc_ledger._hashmap.add(i, 99999)
            BC1._bc_ledger._hashmap.add(i*10, 99999)
            B1 = Block([Transaction(i, i*10, i*100)])
            self.assertTrue(BC1.add_block(B1))
            self.assertNotEqual(BC1._bc_ledger._hashmap.get(i), 99999)
        BC2 = Blockchain()
        # test cases for unsuccessfully added blocks that also ensure transactions were not carried out
        for i in range(1, 25):
            BC2._bc_ledger._hashmap.add(i, 1)
            BC2._bc_ledger._hashmap.add(i*10, 1)
            B2 = Block([Transaction(i, i*10, i*100)])
            self.assertFalse(BC2.add_block(B2))
            self.assertEqual(BC2._bc_ledger._hashmap.get(i), 1)
        # test cases that ensure the blocks' previous hashes point to the hash of the previous block
        for i in range(len(BC1._blockchain)-1):
            self.assertEqual(BC1._blockchain[i].block_hash, BC1._blockchain[i+1].previous_block_hash)

    def test_validate_chain(self):
        BC1 = Blockchain()
        for i in range(1, 25):
            BC1._bc_ledger._hashmap.add(i, 99999)
            BC1._bc_ledger._hashmap.add(i*10, 99999)
            B1 = Block([Transaction(i, i*10, i*100)])
            BC1.add_block(B1)
        # test case for a blockchain with no tampered blocks
        self.assertEqual(BC1.validate_chain(), [])
        BC1._blockchain[3].block_hash, BC1._blockchain[13].block_hash, BC1._blockchain[23].block_hash = 123, 456, 789
        # test case for a blockchain with 3 tampered blocks
        self.assertEqual(BC1.validate_chain(), [BC1._blockchain[3], BC1._blockchain[13], BC1._blockchain[23]])

    def test_repr(self):
        BC1 = Blockchain()
        for i in range(1, 8):
            BC1._bc_ledger._hashmap.add(i, 99999)
            BC1._bc_ledger._hashmap.add(i*10, 99999)
            B1 = Block([Transaction(i, i*10, i*100)])
            BC1.add_block(B1)
        # test cases to ensure important information was included in the string
        for i in range(1, 8):
            self.assertTrue("Block " + str(i) in BC1.__repr__())
            self.assertTrue(str(i) + " paid " + str(i*100) + " to " + str(i*10) in BC1.__repr__())
            self.assertTrue("Block Hash: " + str(BC1._blockchain[i].block_hash) in BC1.__repr__())
            self.assertTrue("Previous Block Hash: " + str(BC1._blockchain[i-1].block_hash) in BC1.__repr__())
        

class TestHashmap(unittest.TestCase):
    def test_find_bucket(self):
        """Tests that hashing is done properly"""
        H1 = Hashmap()
        H1._n_buckets = 8
        # test cases for a hashmap with 8 buckets
        for i in range(64):
            self.assertEqual(H1._find_bucket(i), i%8)
        H1._n_buckets = 5
        # test cases for a hashmap with 5 buckets
        for i in range(40):
            self.assertEqual(H1._find_bucket(i), i%5)

    def test_get(self):
        """Tests that user balances can be accessed properly"""
        H1 = Hashmap()
        # test cases for finding the balance of different users
        for i in range(8):
            H1.add(i, i*10)
            self.assertEqual(H1.get(i), i*10)

    def test_contains(self):
        """Tests that user membership can be checked properly"""
        H1 = Hashmap()
        # test cases for existent users
        for i in range(8):
            H1.add(i, i*10)
            self.assertTrue(i in H1)
        # test cases for non-existent users
        for i in range(9, 16):
            self.assertFalse(i in H1)

    def test_add_remove(self):
        """Tests that users and their balances are added/removed properly"""
        H1 = Hashmap()
        # test cases for adding 8 users
        for i in range(8):
            H1.add(i, i*10)
        self.assertEqual(H1._L, [{0: 0}, {1: 10}, {2: 20}, {3: 30}, {4: 40}, {5: 50}, {6: 60}, {7: 70}])
        # test cases for removing the previous 8 users
        for i in range(8):
            H1.remove(i)
        self.assertEqual(H1._L, [{}, {}, {}, {}, {}, {}, {}, {}])

    def test_rehash(self): 
        """Tests that the number of buckets in the hashmap will change based on number of users"""
        H1 = Hashmap()
        for i in range(64):
            H1.add(i, i*10)
        # test case that ensures the number of buckets increases as the hashmap fills
        self.assertEqual(H1._n_buckets, 64)
        for i in range(64):
            H1.remove(i)
        # test case that ensures the number of buckets decreases as the hashmap empties
        self.assertEqual(H1._n_buckets, 8)

if __name__ == "__main__":
    unittest.main()