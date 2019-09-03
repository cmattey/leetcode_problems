# Time: O(n), n = # of nodes
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        temp_start = head
        match_node = head

        slow = head
        fast = head.next

        loop_found = False

        while slow and fast:
            if slow==fast:
                match_node = slow
                loop_found = True
                break

            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break

        if loop_found:
            """
            Similar to finding intersection of two linked-lists:
            1. head-> intersection
            2. intersection.next -> intersection
            """

            len1 = 0
            temp = head
            while temp:
                if temp==match_node:
                    len1+=1
                    break
                else:
                    len1+=1
                temp = temp.next

            len2 = 0
            temp = match_node.next
            while temp:
                if temp==match_node:
                    len2+=1
                    break
                else:
                    len2+=1
                temp = temp.next

            longer_head = None
            shorter_head = None
            if len1>len2:
                longer_head = head
                shorter_head = match_node.next
            else:
                longer_head = match_node.next
                shorter_head = head

            diff = abs(len2-len1)

            while diff>0:
                longer_head = longer_head.next
                diff-=1

            while longer_head!=shorter_head:
                longer_head = longer_head.next
                shorter_head = shorter_head.next

            return longer_head

        else:
            return None




        
