# 173. Binary Search Tree Iterator
# Time: hasNext()->O(1), next()->average O(1)
# Space: O(h), where h is the height of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack= []
        self.semi_inorder(root)

    def semi_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur_node = self.stack.pop()

        if cur_node.right:
            self.semi_inorder(cur_node.right)

        return cur_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
