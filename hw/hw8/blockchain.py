from hashmap import Hashmap

class Transaction():
    def __init__(self, from_user, to_user, amount):
        """Initializes the transaction class"""
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount

    def __repr__(self):
        """Returns a string representation of the transaction"""
        return str(self.from_user) + " paid " + str(self.amount) + " to " + str(self.to_user)

    def __eq__(self, other):
        """Compares the from_user, the to_user, and the amount of 2 different transactions"""
        return (self.from_user == other.from_user) and (self.to_user == other.to_user) and (self.amount == other.amount)
    

class Block():
    def __init__(self, transactions=None):
        """Initializes the block class"""
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions
        
        self.block_hash = self.__hash__()
        self.previous_block_hash = None

    def add_transaction(self, transaction):
        """Adds a transaction to the block"""
        self.transactions.append(transaction)
        # updates the block's hash
        self.block_hash = self.__hash__()
    
    def __hash__(self):
        """Returns the block's hash"""
        # converts the list of transactions to a tuple so that it is hashable
        return hash(tuple((i.from_user, i.to_user, i.amount) for i in self.transactions))

    def __eq__(self, other):
        """Compares the list of transactions and the hashes of 2 different blocks"""
        return (self.transactions == other.transactions) and (self.block_hash == other.block_hash)


class Ledger():
    def __init__(self):
        """Initializes the ledger class"""
        self._hashmap = Hashmap()
    
    def has_funds(self, user, amount):
        """Checks if the sending user has enough HuskyCoin to send the amount they are trying to transfer"""
        # returns False if user is non-existent
        if user not in self._hashmap:
            return False
        # finds user's balance and compares with the amount they are sending
        balance = self._hashmap.get(user)
        return balance >= amount

    def deposit(self, user, amount):
        """Adds an amount of HuskyCoin to the given user"""
        # returns False if user is non-existent
        if user not in self._hashmap:
            return False
        # finds user's balance and adds it with the amount they are receiving
        new_balance = self._hashmap.get(user) + amount
        # updates user's balance in the hashmap
        self._hashmap.remove(user)
        self._hashmap.add(user, new_balance)

    def transfer(self, user, amount):
        """Subtracts an amount of HuskyCoin from the given user"""
        # returns False if user is non-existent
        if user not in self._hashmap:
            return False
        # returns False if user does not have sufficient funds
        if self.has_funds(user, amount) is False:
            return False
        # finds user's balance and subtracts it with the amount they are sending
        new_balance = self._hashmap.get(user) - amount
        # updates user's balance in the hashmap
        self._hashmap.remove(user)
        self._hashmap.add(user, new_balance)

    def __repr__(self):
        """Returns a string representation of the ledger"""
        ledger_string = ""
        for i in self._hashmap._L:
            for j in i:
                ledger_string += "User " + str(j) + "'s balance is: " + str(i[j]) + "\n"
        return ledger_string



class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    def add_block(self, block):
        """Adds a single block to the blockchain"""
        # Stores the hash of the previous block in the block being added
        if len(self._blockchain) >= 1:
            block.previous_block_hash = self._blockchain[len(self._blockchain)-1].block_hash
        
        # Makes sure users transferring HuskyCoin have the required balance - does not allow the block to be added if any given transaction does not have required user funds
        valid_block = True
        for i in block.transactions:
            if (i.from_user not in self._bc_ledger._hashmap) or (i.to_user not in self._bc_ledger._hashmap): valid_block = False
            balance = self._bc_ledger._hashmap.get(i.from_user)
            if i.amount > balance: valid_block = False
        
        if valid_block == True:
            self._blockchain.append(block)
            # updates the ledger of balances
            for i in block.transactions:
                from_user_old_balance, to_user_old_balance = self._bc_ledger._hashmap.get(i.from_user), self._bc_ledger._hashmap.get(i.to_user)
                self._bc_ledger._hashmap.remove(i.from_user)
                self._bc_ledger._hashmap.add(i.from_user, from_user_old_balance - i.amount)
                self._bc_ledger._hashmap.remove(i.to_user)
                self._bc_ledger._hashmap.add(i.to_user, to_user_old_balance + i.amount)

        # returns True/False value indicating whether the block was successfully added to the chain
        return valid_block
        
    def validate_chain(self):
        """Checks to see if any of the blocks have been tampered with"""
        tampered_blocks = []
        # compares the hashes of each block in the chain
        for i in range(len(self._blockchain)-1):
            if self._blockchain[i].block_hash != self._blockchain[i+1].previous_block_hash: tampered_blocks.append(self._blockchain[i])
        # returns a list of blocks that have been tampered with
        return tampered_blocks

    def __repr__(self):
        """Returns a string representation of the blockchain"""
        blockchain_string = ""
        for i in self._blockchain:
            blockchain_string += "Block " + str(self._blockchain.index(i)) + ":\nTransactions:\n"
            for j in i.transactions:
                blockchain_string += j.__repr__() + "\n"
            blockchain_string += "Block Hash: " + str(i.block_hash) + "\nPrevious Block Hash: " + str(i.previous_block_hash)+"\n\n"       
        return blockchain_string