# Time: O(n), where n=size(tree)
# Space: O(logn), stack space ~height of  tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Created util function with left, and right indices,
        to avoid re-creating sub arrays using nums[:mid],nums[mid+1:]
        """

        return self.util(nums, 0, len(nums)-1)

    def util(self, nums, left, right):

        if left>right:
            return None

        mid = (left+right)//2
        root = TreeNode(nums[mid])

        root.left = self.util(nums, left,mid-1)
        root.right = self.util(nums, mid+1, right)

        return root
