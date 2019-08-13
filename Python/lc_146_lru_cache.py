# 146. LRU Cache
# get: O(1)
# set: O(1)
# Memeory = O(capacity)

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Using Doubly Linked List, can be solved using OrderedDict as well
    """
    def __init__(self, capacity: int):

        self.cap = capacity
        self.kv_map = {}
        self.head = Node('#','#')
        self.tail = Node('#','#')
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.kv_map:
            return -1

        kv_node = self.kv_map[key]

        self.del_node(kv_node)
        self.add_node(kv_node)

        return kv_node.value


    def put(self, key: int, value: int) -> None:

        n = Node(key, value)

        if key in self.kv_map:
            self.del_node(self.kv_map[key])
            self.add_node(n)
            self.kv_map[key] = n

        elif len(self.kv_map)<self.cap:
            self.add_node(n)
            self.kv_map[key] = n

        else:
            last_node = self.tail.prev
            del self.kv_map[last_node.key]

            self.del_node(last_node)
            self.add_node(n)
            self.kv_map[key] = n



    def add_node(self, kv_node):
        """
        add to head
        """
        first = self.head.next
        self.head.next = kv_node
        kv_node.next = first
        kv_node.prev = self.head
        first.prev = kv_node

    def del_node(self, kv_node):
        """
        remove
        """
        before = kv_node.prev
        after = kv_node.next

        before.next = after
        after.prev = before


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
