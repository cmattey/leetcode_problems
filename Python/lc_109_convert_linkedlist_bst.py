# Time: O(n)
# Space: O(logn)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        start = 0
        temp_head = head
        len = 0
        while temp_head:
            len+=1
            temp_head = temp_head.next
        end = len-1

        return self.util([head], 0, end)

    def util(self, head, left, right):

        if left>right:
            return None

        mid = (left+right)//2

        # TLE is we recurse for mid every time
        # temp = 0
        # temp_head = head
        # while temp<mid:
        #     temp_head = temp_head.next
        #     temp+=1

        # Try sort of a inorder approach
        left_tree = self.util(head, left, mid-1)
        temp_root = TreeNode(head[0].val)
        temp_root.left = left_tree

        head[0] = head[0].next

        temp_root.right = self.util(head, mid+1, right)

        return temp_root
