class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_wind = []
        max_l = 0
        for i in range(len(s)):
            if s[i] not in curr_wind:
                curr_wind.append(s[i])
                max_l = max(len(curr_wind), max_l)
            else:
                max_l = max(len(curr_wind), max_l)
                while curr_wind[0] != s[i]:
                    curr_wind.pop(0)
                curr_wind.pop(0)
                curr_wind.append(s[i])
                print(curr_wind)
        return max_l
