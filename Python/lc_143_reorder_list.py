# Time: O(n), n=len(list)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head:
            return None

        slow = head
        fast = head

        prev = None
        while fast:
            prev = slow
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break

        prev.next = None


        temp_slow = slow

        # Using a stack to store reversed nodes
        # while temp_slow:
        #     second_half_stack.append(temp_slow)
        #     temp_slow = temp_slow.next

#         Reverse linkedlist starting from temp_slow

        cur_node = temp_slow
        prev = None
        while temp_slow:
            n = temp_slow.next
            temp_slow.next = prev
            # n.next = temp_slow
            prev = temp_slow
            temp_slow = n


#       Combine first half and reversed list
        reverse_head = prev
        temp_head = head
        while temp_head:
            n = temp_head.next

            if prev:
                # temp_head.next = second_half_stack.pop()
                temp_head.next = prev
                prev = prev.next
            else:
                temp_head.next = None
                break
            temp_head.next.next = n
            temp_head = n

        return head



        
