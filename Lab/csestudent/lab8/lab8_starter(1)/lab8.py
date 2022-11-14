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
        # Use % to scale that hash to a number between 0 and n_buckets
        i = hash(item) % self._n_buckets
        return i

    def __contains__(self, item):
        """Returns True (False) if item is (is not) in the CustomSet"""
        # Find index of bucket `item` should be in, if it is here (self._find_bucket())
        
        # return True if item is in bucket, false otherwise
        i = self._find_bucket(item)
        if item in self._L[i]:
            return True
        return False

    def add(self, item):
        """Adds a new item to CustomSet. Duplicate adds are ignored - they do not increase the length, but they do not raise an error."""
        # Check if item already here (`item in self`, since we already implemented self.__contains__()).
        # Return early if it's already here - we don't need to do anything

        # Find index of bucket `item` should go in (self._find_bucket())

        # Add item to end of bucket
        if item not in self:
            i = self._find_bucket(item)
            self._L[i].append(item)
            self._len += 1
        else:
            return

        if self._len >= 2 * self._n_buckets:
            self._n_buckets *= 2
            self._rehash(self._n_buckets)
        # update length

        # rehash if necessary (items >= 2*buckets)

    def remove(self, item):
        """Removes item from CustomSet. Removing an item not in CustomSet should raise a KeyError."""
        # Check if item is in the CustomSet (`item in self`, since we already implemented self.__contains__()).
        # Raise a KeyError if it is not (and include a helpful message)

        # Find index of bucket `item` is in (self._find_bucket())
        if item not in self:
            raise ValueError("Item is not in set")
        else:
            i = self._find_bucket(item)
            self._L[i].remove(item)
            self._len -= 1

        if (self._len <= self._n_buckets / 2) and (self._n_buckets / 2 >= self._min_buckets):
            self._n_buckets //= 2
            self._rehash(self._n_buckets)
        # Remove item from bucket

        # update length

        # rehash if necessary (items <= 1/2*buckets, and 1/2*buckets >= min_buckets)

    def _rehash(self, new_buckets):
        """Rehashes every item from a hash table with n_buckets to one with new_buckets. new_buckets will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are rehashing up or down."""
        # Make a new list of `new_buckets` empty lists

        # Using a for loop, iterate over every bucket in self._L
            # using a for loop, iterate over every item in this bucket
                # Find the index of the new bucket for that item
                # add that item to the correct bucket

        # Update self._L to point to the new list
        L = self._L[:]
        self._L = [[] for i in range(self._n_buckets)]
        for bucket in L:
            for item in bucket:
                i = self._find_bucket(item)
                self._L[i].append(item)