class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for i in range(len(nums)):
            if(nums[i] in temp):
                return True
            else:
                temp.add(nums[i])
        return False