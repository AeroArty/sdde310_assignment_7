from MyHashTable import MyHashTable
class HashTable_LP(MyHashTable):
    class ListNode():
        def __init__(self, curr_key=None, curr_value=None):
            self.key = curr_key
            self.value = curr_value
            self.next = None

    def __init__(self,size=10):
        self.table_size = size
        self.table = [self.ListNode() for i in range(self.table_size)]

    
    def get_value(self,key):
        index = self.get_index(self.gen_hash(key), self.table_size)
        curr_node = self.table[index]

        while curr_node and index < len(self.table):
            if curr_node.key == key:
                return curr_node.value
            index += 1
            curr_node = self.table[index]
        return None

    def add(self, key, value):
        index = self.get_index(self.gen_hash(key), self.table_size)
        curr_node = self.table[index]

        if curr_node.value is None:
            curr_node.key = key
            curr_node.value = value

        else:
            while curr_node.value is not None and index < len(self.table):
                index += 1
                curr_node = self.table[index]
            curr_node.key = key
            curr_node.value = value


if __name__ == "__main__":
    my_table_chain = HashTable_LP()
    print(HashTable_LP.gen_hash("12"))
    my_table_chain.add("12", 0)
    print(my_table_chain.get_value("12"))
    my_table_chain.add("22", 1)
    print(my_table_chain.get_value("12"))
    print(my_table_chain.get_value("22"))
