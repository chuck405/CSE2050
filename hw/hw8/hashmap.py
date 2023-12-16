class Hashmap():
    def __init__(self):
        """Initializes the hashmap class"""
        self._min_buckets = 8  
        self._n_buckets = 8       
        self._len = 0 
        self._L = [{} for i in range(self._n_buckets)]

    def _find_bucket(self, user):
        """Returns the index of the bucket for user, based on hash(user) and self.n_buckets"""
        bucket_index = hash(user)
        return bucket_index % self._n_buckets

    def get(self, user):
        """Returns a specific user's balance"""
        bucket_index = self._find_bucket(user)
        bucket = self._L[bucket_index]
        return bucket[user]

    def __contains__(self, user):
        """Returns True/False depending on whether or not the user is listed in the hashmap"""
        bucket_index = self._find_bucket(user)
        if user in self._L[bucket_index].keys(): return True
        else: return False

    def add(self, user, balance):
        """Adds a new user to the hashmap"""
        # ignores duplicate users
        if self.__contains__(user) == True: return
        
        else:
            bucket_index = self._find_bucket(user)
            bucket = self._L[bucket_index]
            bucket[user] = balance

        # updates length
            self._len += 1

        # rehash if necessary (items >= 2*buckets)
        if (self._len >= 2*self._n_buckets): self._rehash(2*self._n_buckets)

    def remove(self, user):
        """Removes user from hashmap"""
        # raises KeyError for non-existent users
        if self.__contains__(user) == False: raise KeyError("Attempt to remove non-existent user " + str(user))

        bucket_index = self._find_bucket(user)
        bucket = self._L[bucket_index]
        del bucket[user]

        # updates length
        self._len -= 1

        # rehash if necessary (items <= 1/2*buckets, and 1/2*buckets >= min_buckets)
        if (self._len <= 0.5*self._n_buckets) and (0.5*self._n_buckets >= self._min_buckets): self._rehash(0.5*self._n_buckets)

    def _rehash(self, new_buckets):
        """Rehashes every item from a hashmap with n_buckets to one with new_buckets - new_buckets will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are rehashing up or down"""
        # makes a new list of "new_buckets" empty lists
        new_list = [{} for i in range(int(new_buckets))]
        self._n_buckets = int(new_buckets)

        # iterates over ever item in every bucket
        for i in self._L:
            for j in i:
                # find the new index of the new bucket for each user
                new_bucket_index = self._find_bucket(j)
                new_bucket = new_list[new_bucket_index]
                # add that item to the correct bucket
                new_bucket[j] = i[j]

        # updates self._L to point to the new list
        self._L = new_list
    