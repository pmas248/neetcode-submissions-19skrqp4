class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in nums and nums.index(dif) != i:
                return sorted([i, nums.index(dif)])
