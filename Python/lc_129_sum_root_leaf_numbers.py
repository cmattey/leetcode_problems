# 129. Sum Root to Leaf Numbers
# Time: O(size(tree))
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.result = 0

    def sumNumbers(self, root: TreeNode) -> int:

        if not root:
            return 0

        self.dfs(root, 0)
        return self.result


    def dfs(self, root, cur_sum):
        if not root:
            return

        if not root.left and not root.right:
            cur_sum = 10*cur_sum + root.val
            self.result+=cur_sum
            return

        self.dfs(root.left, 10*cur_sum+root.val)
        self.dfs(root.right, 10*cur_sum+root.val)



"""
Using str stack, and joining to get final number
class Solution:

    def __init__(self):
        self.result = 0

    def sumNumbers(self, root: TreeNode) -> int:

        if not root:
            return 0

        self.dfs(root, [])
        return self.result


    def dfs(self, root, cur_stack):
        if not root:
            return

        if not root.left and not root.right:
            cur_stack.append(str(root.val))
            cur_sum = int("".join(cur_stack))  # Can also use function to find num using powers of 10
            cur_stack.pop()
            self.result+=cur_sum
            return

        cur_stack.append(str(root.val))
        self.dfs(root.left, cur_stack)
        self.dfs(root.right, cur_stack)
        cur_stack.pop()
"""
