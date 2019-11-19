# 17th Nov '19
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        dummy_head = ListNode(0)
        dummy_head.next = head

        non_zero = None # stores node reference to last non-9 node

        temp = dummy_head

        while temp:
            if temp.val!=9:
                non_zero = temp
            temp = temp.next

        non_zero.val+=1
        start = non_zero.next

        while start:
            start.val = 0
            start = start.next

        if dummy_head.val ==0:
            return dummy_head.next
        else:
            return dummy_head

# Time: O(n), where n is the length of the list
# Space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        -> if tail<9, add 1 to tail and return.
        -> if tail==9, need references to nodes whose value we need to increment.
            -> can store reference related to position in number in a hashmep: {key: position, value: Node}. Takes extra log(n)[base10] memory.
        """

        node_map = {}

        temp = head

        index = 0
        prev = None
        while temp:
            node_map[index] = temp
            prev = temp
            temp = temp.next
            index+=1

        last_val = prev.val
        len_list = index

        if last_val<9:
            node_map[len_list-1].val+=1
            return head
        else:
            node_map[len_list-1].val = 0
            carry = 1
            index = len_list-2
            while carry and index>=0:

                if node_map[index].val==9:
                    node_map[index].val = 0
                    carry = 1
                    index-=1
                else:
                    node_map[index].val+=1
                    carry = 0
                    index-=1

            if carry:
                newNode = ListNode(1)
                newNode.next = head
                head = newNode
                return head
            else:
                return head
