from MyHashTable import MyHashTable
class HashTable_LP(MyHashTable):
    class ListNode():
        def __init__(self, curr_key=None, curr_value=None):
            self.key = curr_key
            self.value = curr_value
            self.next = None

    def __init__(self,size=10, threshold_load_fac=0.75):
        self.table_size = size
        self.table = [self.ListNode() for i in range(self.table_size)]
        self.threshold_load_factor = threshold_load_fac
        self.load_factor = 0

    
    def get_value(self,key):
        index = self.get_index(self.gen_hash(key), self.table_size)
        curr_node = self.table[index]

        while curr_node and index < len(self.table):
            curr_node = self.table[index]
            if curr_node.key == key:
                return curr_node.value
            index += 1
        return None

    def add_basic(self, key, value):
        index = self.get_index(self.gen_hash(key), self.table_size)
        curr_node = self.table[index]

        if curr_node.value is None:
            curr_node.key = key
            curr_node.value = value
            self.load_factor += 1/self.table_size

        else:
            while curr_node.value is not None and curr_node.key != key and index < len(self.table):
                index += 1
                curr_node = self.table[index]
            if curr_node.key != key:
                self.load_factor += 1/self.table_size
            curr_node.key = key
            curr_node.value = value

    def rehash(self, new_size=None):
        old_table = self.table
        if new_size is None:
            new_size = self.table_size * 2
        self.__init__(new_size, self.threshold_load_factor)
        new_list = [self.add_basic(i.key, i.value) for i in old_table if i.value is not None]
        self.load_factor = len(new_list)/self.table_size

if __name__ == "__main__":
    my_table = HashTable_LP()
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

    print(my_table.get_value("12"))
    print(my_table.get_value("22"))
    print(my_table.get_value("32"))
    print(my_table.get_value("52"))


