# Time: bfs(tree)
# Space: num_nodes in tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        q = [root]
        op = []

        while q:

            cur_node = q.pop(0)
            if not cur_node:
                op.append('None')
                continue
            else:
                op.append(str(cur_node.val))

            q.append(cur_node.left)
            q.append(cur_node.right)

        # print(op)
        return ",".join(op)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = list(data.split(','))

        if data[0]=="None":
            return None

        node_map = {}
        root = TreeNode(data[0])

        q = [root]
        index = 1

        while q and index<len(data):

            cur_node = q.pop(0)

            if data[index]!='None':
                left = TreeNode(data[index])
                cur_node.left = left
                q.append(left)
            index+=1

            if data[index]!='None':
                right = TreeNode(data[index])
                cur_node.right = right
                q.append(right)

            index+=1

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
