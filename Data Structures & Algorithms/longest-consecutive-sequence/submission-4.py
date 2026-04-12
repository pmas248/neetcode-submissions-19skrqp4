class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        long = 0

        for n in numset:
            if (n-1) not in numset:
                curr = n
                curr_streak = 1

                while (curr+1) in numset:
                    curr += 1
                    curr_streak += 1
                
                long = max(curr_streak, long)

        return long
        
