class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if curr == nums[j]:
                    return True
        return False