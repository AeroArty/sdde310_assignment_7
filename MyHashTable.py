# Used lab solutions as template/starting point

class MyHashTable:
    def __init__(self, size=10, threshold_load_fac=1):
        self.table_size = size
        self.table = [None for i in range(self.table_size)]
        self.load_factor = 0
        self.threshold_load_factor = threshold_load_fac


    # Precondition: tableSize > 0
    def get_index(self, hash_value, table_size):
        return hash_value % table_size


    # Precondition: key is not null(None)
    def has_value(self, key):
        return self.get_value(key) is not None

    # Precondition: key is not null(None)
    def get_value(self, key):
        index = self.get_index(self.gen_hash(key), self.table_size)

        # call is_name_equal to make sure we have the exact same key, and not just another entry
        # that happened to either have the same hash value, or happened to the resolve to the same index
        if self.table[index] and self.table[index] == key:
            return self.table[index]

    def print_hash_table(self):
        [print(i[0], ": ", i[1].value) for i in enumerate(self.table)]
        print()

    @staticmethod
    def gen_hash(string):
        if not string:
            return 0

        hash_value = 0
        for ii in range(len(string)):
            hash_value += ord(string[ii]) * ii

    def add_basic(self, key, value):
        index = self.get_index(self.gen_hash(key), self.table_size)
        if self.table[index] is not None:
            self.load_factor += 1/self.table_size
        self.table[index] = value # will overwrite any existing value. Does not handle collisions. BAD
        
    def _rehash(self, new_size=None):
        pass

    def add(self, key, value):
        self.add_basic(key, value)
        if(self.load_factor > self.threshold_load_factor):
            self._rehash()

if __name__ == "__main__":
    my_table = MyHashTable()
    print(MyHashTable.gen_hash("abc"))
    