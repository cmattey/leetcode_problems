# Time: O(N**2), for each node, taking linear time to find split_index
# Space: O(N**2), for each node, splicing which takes linear time.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        if not pre or not post:
            return None

        root = TreeNode(pre[0])
        if len(pre)==1:
            return root

        split_index = post.index(pre[1])+1

        root.left = self.constructFromPrePost(pre[1:split_index+1], post[:split_index])
        root.right = self.constructFromPrePost(pre[split_index+1:], post[split_index:-1])

        return root
        
