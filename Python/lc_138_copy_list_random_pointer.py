# Time: O(|E|)
# Space: O(|V|)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        node_map = {}
        temp_head = head

        while temp_head:

            if temp_head not in node_map:
                dup_node = Node(temp_head.val,None,None)

                node_map[temp_head] = dup_node

            if temp_head.random:

                if temp_head.random not in node_map:
                    node_map[temp_head.random] = Node(temp_head.random.val,None,None)

                node_map[temp_head].random = node_map[temp_head.random]

            if temp_head.next:

                if temp_head.next not in node_map:
                    node_map[temp_head.next] = Node(temp_head.next.val,None,None)

                node_map[temp_head].next = node_map[temp_head.next]

            temp_head = temp_head.next

        return node_map[head]

        
