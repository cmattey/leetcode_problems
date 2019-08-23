# Time: O(size(tree))
# Space: O(size(tree))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        Can be solved using a typical BFS and reversing at the end.
        Trying to solve using DFS with depth information, without the need to reverse.
        """

        depth = self.getDepth(root)

        bot_arr = [[] for _ in range(depth)]

        self.recTrav(root, bot_arr, depth-1)

        return bot_arr

    def recTrav(self, root, bot_arr, depth):
        if not root:
            return

        if depth==0:
            bot_arr[0].append(root.val)
            return

        bot_arr[depth].append(root.val)

        self.recTrav(root.left, bot_arr, depth-1)
        self.recTrav(root.right, bot_arr, depth-1)

        return

    def getDepth(self, root):
        if not root:
            return 0

        return 1+max(self.getDepth(root.left),self.getDepth(root.right))

        
