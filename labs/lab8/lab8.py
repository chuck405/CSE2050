class CustomSet:
    def __init__(self):
        """Initializes an empty CustomSet"""
        self._min_buckets = 8            # We never want to rehash down below this many buckets.
        self._n_buckets = 8              # initial size. Good to use a power of 2 here.
        self._len = 0                   # Number of items in custom set
        self._L = [[] for i in range(self._n_buckets)]   # List of empty buckets

    # TODO: Implement methods below
    def __len__(self):
        """Returns the number of items in CustomSet"""
        return self._len

    def _find_bucket(self, item):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self.n_buckets"""
        # hash(item) returns a nice "random" integer using item.__hash__()
        bucket_index = hash(item)
        # Use % to scale that hash to a number between 0 and n_buckets
        return bucket_index % self._n_buckets

    def __contains__(self, item):
        """Returns True (False) if item is (is not) in the CustomSet"""
        # Find index of bucket `item` should be in, if it is here (self._find_bucket())
        bucket_index = self._find_bucket(item)

        # return True if item is in bucket, false otherwise
        if item in self._L[bucket_index]: return True
        else: return False

    def add(self, item):
        """Adds a new item to CustomSet. Duplicate adds are ignored - they do not increase the length, but they do not raise an error."""
        # Check if item already here (`item in self`, since we already implemented self.__contains__()).
        if self.__contains__(item) == True:

        # Return early if it's already here - we don't need to do anything
            return
        else:

        # Find index of bucket `item` should go in (self._find_bucket())
            bucket_index = self._find_bucket(item)

        # Add item to end of bucket
            self._L[bucket_index].append(item)

        # update length
            self._len += 1

        # rehash if necessary (items >= 2*buckets)
        if (self._len >= 2*self._n_buckets): self._rehash(2*self._n_buckets)



    def remove(self, item):
        """Removes item from CustomSet. Removing an item not in CustomSet should raise a KeyError."""
        # Check if item is in the CustomSet (`item in self`, since we already implemented self.__contains__()).
        if self.__contains__(item) == False:

        # Raise a KeyError if it is not (and include a helpful message)
            raise KeyError("Attempt to remove non-extant item " + str(item))

        # Find index of bucket `item` is in (self._find_bucket())
        bucket_index = self._find_bucket(item)

        # Remove item from bucket
        self._L[bucket_index].remove(item)

        # update length
        self._len -= 1

        # rehash if necessary (items <= 1/2*buckets, and 1/2*buckets >= min_buckets)
        if (self._len <= 0.5*self._n_buckets) and (0.5*self._min_buckets >= self._min_buckets): self._rehash(0.5*self._n_buckets)


    def _rehash(self, new_buckets):
        """Rehashes every item from a hash table with n_buckets to one with new_buckets. new_buckets will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are reahshing up or down."""
        # Make a new list of `new_buckets` empty lists
        new_list = [[] for i in range(new_buckets//1)]
        self._n_buckets *= 2

        # Using a for loop, iterate over every bucket in self._L
        for i in self._L:

            # using a for loop, iterate over every item in this bucket
            for j in i:

                # Find the index of the new bucket for that item
                new_bucket_index = self._find_bucket(j)

                # add that item to the correct bucket
                new_list[new_bucket_index].append(j)

        # Update self._L to point to the new list
        self._L = new_list