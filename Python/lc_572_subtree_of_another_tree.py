# Time: O(s*t) # for every node in s, you traverse every node in t.
# Space: O(s) # number of nodes in s

# Mar 30th '20

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if (s and not t) or (t and not s):
            return False

        if not s and not t:
            return True

        if s.val == t.val:
            return self.helper(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def helper(self, s, t):

        if not s and not t:
            return True

        if (s and not t) or (t and not s):
            return False

        if s.val!=t.val:
            return False

        return self.helper(s.left, t.left) and self.helper(s.right, t.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        return self.traverse(s, t)

    def traverse(self, s, t):

        if s:
            return self.equal_verify(s, t) or self.traverse(s.left,t) or self.traverse(s.right, t)
        else:
            return False

    def equal_verify(self, s, t):

        if not s and not t:
            return True

        if not s or not t:
            return False

        if s.val==t.val:
            return self.equal_verify(s.left, t.left) and self.equal_verify(s.right, t.right)

        return False
