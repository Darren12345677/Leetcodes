class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = len(nums)
        result = set()
        nums.sort()
        for i in range(x-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            mapping = {} #complement:index
            for j in range(i+1, x):
                if nums[j] in mapping:
                    result.add(tuple([nums[i], nums[mapping[nums[j]]], nums[j]]))
                else:
                    complement = -(nums[i] + nums[j])
                    mapping[complement] = j
        return result