class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = defaultdict(int)
        for i in range(len(nums)):
            temp[nums[i]] = (temp[nums[i]] + 1)
            if temp[nums[i]] > 1:
                return True
        return False