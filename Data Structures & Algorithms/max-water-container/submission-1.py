class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_vol = 0
        while l < r:
            lbar, rbar = heights[l], heights[r]
            curr_vol = min(lbar, rbar) * (r-l)
            max_vol = max(max_vol, curr_vol)
            if lbar < rbar:
                l += 1
            else:
                r -= 1
        return max_vol