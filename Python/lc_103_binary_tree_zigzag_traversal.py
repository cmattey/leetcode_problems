# Time: O(size(tree))
# Space: O(size(tree)) cur_row contains all elements in row, can be of order O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        q = [root]

        zz = []


        while q:

            cur_len = len(q)
            cur_row = []
            while cur_len>0:
                cur = q.pop(0)
                cur_row.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

                cur_len-=1

            zz.append(cur_row)

        for i in range(len(zz)):

            if i%2!=0:
                zz[i] = zz[i][::-1]

        return zz


        
