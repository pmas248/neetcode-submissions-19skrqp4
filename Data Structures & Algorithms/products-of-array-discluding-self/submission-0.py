class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        temp = 1
        z_count = 0
        for num in nums:
            if num == 0:
                z_count += 1
                continue
            temp *= num
        
        if z_count > 1: return [0] * len(nums)
        
        for i,v in enumerate(nums):
            if z_count:
                if v == 0:
                    res[i] = temp
                else:
                    res[i] = 0
            else: res[i] = temp // v
        return res