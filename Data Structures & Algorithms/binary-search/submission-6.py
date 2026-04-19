class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid_int = l + (r - l) // 2
            mid = nums[mid_int]
            print(mid, l, r)
            if mid < target:
                l = mid_int + 1
            elif mid > target:
                r = mid_int - 1
            else:
                return mid_int
        return -1