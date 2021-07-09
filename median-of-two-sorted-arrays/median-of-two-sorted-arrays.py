class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine = nums1 + nums2
        combine.sort()
        x = len(combine)
        if x%2 == 0:
            return (combine[x//2-1] + combine[x//2])/2
        return combine[x//2]