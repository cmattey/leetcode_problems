# O(log(min(m,n))), m= len(nums1), n = len(nums2)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        left1 = elements to the left, for shorter array
        left2 = elements to the left for longer array

        total elements in left half = (m+n)//2
        if len(left1) = x
        len(left2) = ((m+n)//2)-x

        if left1<=right2 and left2<=right1, found middle partition

        else if left1>right2: move num1 left
        else: move nums1 right

        """
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        isEven = True if ((m+n)%2==0) else False

        while left<=right:

            part_pos_1 = (left+right)//2    # Partition position in array1
            part_pos_2 = (m+n+1)//2-part_pos_1

            maxLeft1 = float('-inf') if part_pos_1==0 else nums1[part_pos_1-1]
            minRight1 = float('inf') if part_pos_1==len(nums1) else nums1[part_pos_1]

            maxLeft2 = float('-inf') if part_pos_2==0 else nums2[part_pos_2-1]
            minRight2 = float('inf') if part_pos_2==len(nums2) else nums2[part_pos_2]

            if maxLeft1<=minRight2 and maxLeft2<=minRight1:
                if isEven:
                    return (max(maxLeft1,maxLeft2)+min(minRight1, minRight2))/2
                else:
                    return max(maxLeft1,maxLeft2)

            elif maxLeft1>minRight2:
                right = part_pos_1-1
            else:
                left = part_pos_1+1
