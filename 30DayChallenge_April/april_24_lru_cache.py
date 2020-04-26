class DLL:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv_map = {}

        self.head = DLL("head", "head")
        self.tail = DLL("tail", "tail")

        self.tail.next = self.head
        self.head.prev = self.tail


    def get(self, key: int) -> int:
        # print("GET:", key)
        if key not in self.kv_map:
            return -1

        self.remove_node(self.kv_map[key])
        self.add_to_head(self.kv_map[key])
        # print(self.kv_map)
        return self.kv_map[key].val


    def put(self, key: int, value: int) -> None:
        # print("PUT:",key, value)
        new_node = DLL(key, value)

        if key in self.kv_map:
            self.remove_node(self.kv_map[key])
            self.add_to_head(new_node)
        elif len(self.kv_map)<self.cap:
            self.add_to_head(new_node)
        else:
            least_recent = self.tail.next
            del self.kv_map[least_recent.key]
            self.remove_node(least_recent)
            self.add_to_head(new_node)

        self.kv_map[key] = new_node
        # print(self.kv_map)
        return


    def add_to_head(self, node):
        # print("Added node val", node.val)
        prev = self.head.prev
        self.head.prev = node
        node.next = self.head
        node.prev = prev
        prev.next = node

        return

    def remove_node(self, node):
        # print("removed node val", node.val)
        node.prev.next = node.next
        node.next.prev = node.prev

        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
