# Time: O(n) where n = len(gas)
# Space: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        cur_gas = 0

        index = 0
        while index<len(cost):
            cur_gas = gas[index]

            if cost[index]>cur_gas:
                index+=1
                continue

            else:
                found_path, start_index = self.try_round(index, cost, gas)
                if found_path:
                    return index
                else:
                    if start_index>index:
                        index = start_index
                    else:
                        return -1

        return -1

    def try_round(self, index, cost, gas):

        start_index = index

        l = len(cost)
        cur_gas = 0

        while l>0:
            cur_gas+=gas[index]

            if cur_gas<cost[index]:
                return (False, index)

            cur_gas -=cost[(index)%len(cost)]

            index = (index+1)%len(cost)

            l-=1

        return (l==0,index)

        
