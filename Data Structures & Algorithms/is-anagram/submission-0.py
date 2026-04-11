class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp_count = {}

        for char in s:
            temp_count[char] = temp_count.get(char, 0) + 1

        for char in t:
            if char not in temp_count or temp_count[char] == 0:
                return False
            temp_count[char] -= 1
        return True 
        