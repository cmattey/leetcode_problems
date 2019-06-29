# 6. ZigZag Conversion
# Time: O(len(s))
# Space: O(len(s))

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows==1:
            return s

        store = [[]for i in range(min(numRows,len(s)))]

        going_down = True
        cur_row = 0

        for ch in s:
            store[cur_row].append(ch)

            if cur_row == numRows-1 and going_down:
                going_down = False
                cur_row-=1
            elif cur_row == 0 and not going_down:
                going_down = True
                cur_row+=1
            elif cur_row < numRows-1 and going_down:
                cur_row+=1
            else:
                cur_row-=1

        zigzag = "".join(item for innerList in store for item in innerList)


        return zigzag
