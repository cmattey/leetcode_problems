class FirstUnique:
    from collections import Counter
    def __init__(self, nums: List[int]):
        self.head = DLL("#")
        self.tail = DLL("#")

        self.head.right = self.tail
        self.tail.left = self.head

        self.discarded = set()
        counter = Counter(nums)
        self.imap = {}
        for num, count in counter.items():
            if count==1:
                new_node = DLL(num)
                self.add_to_queue(new_node)
                self.imap[num] = new_node
            else:
                self.discarded.add(num)

    def showFirstUnique(self) -> int:
        if self.head.right == self.tail:
            return -1

        return self.head.right.val

    def add(self, value: int) -> None:
        if value in self.discarded:
            return
        elif value in self.imap and value not in self.discarded: # dont need to check for discarded here
            self.remove_node(self.imap[value])
            self.discarded.add(value)
        else:
            new_node = DLL(value)
            self.add_to_queue(new_node)
            self.imap[value] = new_node

    def add_to_queue(self, node):
        last = self.tail.left
        last.right = node
        node.left = last
        node.right = self.tail
        self.tail.left = node

    def remove_node(self, node):
        left = node.left
        right = node.right

        left.right = right
        right.left = left

class DLL:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
