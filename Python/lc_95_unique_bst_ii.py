# Time: O(n^2 +(?)) <--Review (Catalan number)
# Space: O((n^2)*n + (?))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        if n==0:
            return []
        start = 1
        end = n
        return self.util(start, end)


    def util(self,start, end):

        if start>end:
            return [None]

        if start==end:
            return [TreeNode(start)]

        temp = []
        for i in range(start, end+1):
            # print(cur_node.val)
            left_trees = self.util(start, i-1)
            right_trees = self.util(i+1,end)
            for left_root in left_trees:
                for right_root in right_trees:
                    cur_node = TreeNode(i)
                    cur_node.right = right_root
                    cur_node.left = left_root
                    temp.append(cur_node)

        return temp
