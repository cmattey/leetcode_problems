# Time: O(N), n=nodes in tree
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        self.dfs(root, None)

        output = []
        q = [(target, 0)]

        seen = set()

        while q:

            cur_node, cur_dist = q.pop(0)

            if cur_node in seen:
                continue

            seen.add(cur_node)

            if cur_dist==K:
                output.append(cur_node.val)
            if cur_dist>K:
                continue

            for node in (cur_node.left, cur_node.right, cur_node.par):
                if node:
                    q.append((node, cur_dist+1))

        return output


    def dfs(self, node, par):

        if node:
            node.par = par
            self.dfs(node.left, node)
            self.dfs(node.right, node)

        return
        
