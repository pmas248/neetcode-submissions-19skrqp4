class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights)-1
        dist = len(heights)-1

        while l < r:
            l_val, r_val = heights[l], heights[r]
            smaller = min(l_val, r_val)
            container_vol = smaller * dist
            if container_vol > res: res = container_vol

            if l_val <  r_val: l+=1
            elif l_val >  r_val: r-=1
            elif heights[l+1] < heights[r-1]:  l+=1
            else: r-=1
            dist -=1
                


        return res

