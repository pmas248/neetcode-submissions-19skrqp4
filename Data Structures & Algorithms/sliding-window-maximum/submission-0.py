class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s_wind = []
        res = []

        for i in range(k):
            s_wind.append(nums[i]) 

        res.append(max(s_wind))
        for i in range(k, len(nums)):

            s_wind.pop(0)
            s_wind.append(nums[i])
            res.append(max(s_wind))

        return res
