# Time: O(n)
# Space: O(1), O(26)

class Solution:

    def __init__(self):

        chars = "abcdefghijklmnopqrstuvwxyz"
        counter = 0

        self.char_map = {}

        for ch in chars:
            self.char_map[ch] = [counter//5, counter%5]
            counter+=1


    def alphabetBoardPath(self, target: str) -> str:

        output = []

        cur_pos = [0,0]
        for ch in target:

            x,y = self.char_map[ch]

            if y<cur_pos[1]:
                output.append('L'*(cur_pos[1]-y))
            if x>cur_pos[0]:
                output.append('D'*(x-cur_pos[0]))
            if x<cur_pos[0]:
                output.append('U'*(cur_pos[0]-x))
            if y>cur_pos[1]:
                output.append('R'*(y-cur_pos[1]))

            output.append('!')
            cur_pos = [x,y]

        return "".join(output)
