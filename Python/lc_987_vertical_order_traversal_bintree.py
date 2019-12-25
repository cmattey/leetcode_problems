# Time: O(nlogn), n=size(Tree)
# Space: O(size(tree))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        hmap = collections.defaultdict(list)

        self.util(root, 0, 0, hmap)

        rows = [[k,v] for k,v in hmap.items()]
        rows.sort(key = lambda kv:(kv[0][0],-kv[0][1]))
        # print(rows)

        output = []
        for (x,y),val in rows:
            if not output:
                prev_x = x
                output.append(val)
            elif x==prev_x:
                output[-1].extend(val)
            else:
                prev_x = x
                output.append(val)

        return output


    def util(self, root, x, y, hmap):
        if not root:
            return

        hmap[(x,y)].append(root.val)
        hmap[(x,y)].sort()

        self.util(root.left, x-1, y-1, hmap)
        self.util(root.right, x+1, y-1, hmap)
        
