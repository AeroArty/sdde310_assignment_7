from MyHashTable import MyHashTable
class HashTable_Chain(MyHashTable):
    class ListNode():
        def __init__(self, curr_key=None, curr_value=None):
            self.key = curr_key
            self.value = curr_value
            self.next = None
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.next is None:
                raise StopIteration
            return self.next
        
        @staticmethod
        def str_list(node):
            if node is None:
                return ""
            else:
                return "[key: " + str(node.key) + " | value: " + str(node.value) + "] " + HashTable_Chain.ListNode.str_list(node.next)

    def __init__(self,size=10, threshold_load_fac=1.5):
        self.table_size = size
        self.table = [self.ListNode() for i in range(self.table_size)]
        self.threshold_load_factor = threshold_load_fac
        self.load_factor = 0
    
    def get_value(self,key):
        index = self.get_index(self.gen_hash(key), self.table_size)
        curr_node = self.table[index]

        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return None

    def add_basic(self, key, value):
        index = self.get_index(self.gen_hash(key), self.table_size)
        curr_node = self.table[index]

        if curr_node.value is None:
            curr_node.key = key
            curr_node.value = value
            self.load_factor += 1/self.table_size

        else:
            while curr_node.next and curr_node.key != key:
                curr_node = curr_node.next
            if curr_node.key == key:
                curr_node.value = value
            else:
                curr_node.next = self.ListNode(key, value)
                self.load_factor += 1/self.table_size

    def _rehash(self, new_size=None):
        old_table = self.table
        if new_size is None:
            new_size = self.table_size * 2
        self.__init__(new_size, self.threshold_load_factor)
        for i in old_table:
            curr_node = i
            while curr_node is not None and curr_node.value is not None:
                self.add_basic(curr_node.key, curr_node.value)
                curr_node = curr_node.next

    def print_hash_table(self):
        [print(i, ": ", self.ListNode.str_list(ii)) for (i,ii) in enumerate(self.table)]
        print()


if __name__ == "__main__":
    my_table = HashTable_Chain(threshold_load_fac=0.25)
    my_table.print_hash_table()
    my_table.add("12", 12)
    my_table.print_hash_table()
    my_table.add("12", 120)
    my_table.print_hash_table()
    my_table.add("32", 32)
    my_table.print_hash_table()

    print(my_table.get_value("12"))
    my_table.add("22", 22)
    my_table.print_hash_table()
    my_table.add("56", 56)
    my_table.print_hash_table()
    my_table.add("58", 58)
    my_table.print_hash_table()
    my_table.add("9", 9)
    my_table.print_hash_table()
    my_table.add("0", 0)
    my_table.print_hash_table()
    my_table.add("1", 1)
    my_table.print_hash_table()
    my_table.add("134", 12)
    my_table.print_hash_table()
    my_table.add("1343", 13)
    my_table.print_hash_table()
    my_table.add("1335", 14)
    my_table.add("1343", 15)
    my_table.add("234343", 25)
    my_table.add("23433", 26)
    my_table.print_hash_table()

    print(my_table.get_value("12"))
    print(my_table.get_value("22"))
    print(my_table.get_value("32"))
    print(my_table.get_value("52"))
