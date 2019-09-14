# Time: O(m+n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        len1 = 0

        tempA = headA

        while tempA:
            tempA = tempA.next
            len1+=1

        len2 = 0
        tempB = headB

        while tempB:
            tempB = tempB.next
            len2+=1


        diff = abs(len1-len2)

        shorter = headA if len1<=len2 else headB
        longer = headA if len1>len2 else headB

        while diff>0:
            longer = longer.next
            diff-=1

        while shorter and longer:
            if shorter==longer:
                return shorter
            shorter = shorter.next
            longer = longer.next

        return None



        
