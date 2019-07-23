# 1104. Path In Zigzag Labelled Binary Tree
# Weekly Contest 143
# To be Refactored
# Time: O(label)
# Space:O(label)
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        cur_pow = 2
        tree = [[1]]
        cur_max = 1
        while cur_max<label:
            cur_row = []
            for i in range (int(math.pow(2,cur_pow-1)),int(math.pow(2,cur_pow))):
                cur_max=i
                cur_row.append(i)

            cur_pow+=1
            tree.append(cur_row)

        for index,row in enumerate(tree):
            if index%2==1:
                row.reverse()

        new_tree = []
        for row in tree:
            for el in row:
                new_tree.append(el)


        old_tree = list(range(1,max(new_tree)+1))

        index = new_tree.index(label)

        path = [label]
        while index>0:
            value = old_tree[index]//2
            index = old_tree.index(value)
            path.append(new_tree[index])

        return path[::-1]
