# 1108. Defanging an IP Address
# Weekly Contest 144
# Time: O(len(address))
# Space: O(1)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
