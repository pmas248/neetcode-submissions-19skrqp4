from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        # 1. Initialize both counts for the first window
        for i in range(n1):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        # 2. Slide the window across s2
        # We start from n1 because we already processed 0 to n1-1
        for i in range(n1, n2):
            if s1_count == s2_count:
                return True
            
            # Add the NEW character (right side)
            s2_count[s2[i]] += 1
            
            # Remove the OLD character (left side)
            left_char = s2[i - n1]
            s2_count[left_char] -= 1
            
            # Clean up zeros so the dictionary comparison works
            if s2_count[left_char] == 0:
                del s2_count[left_char]

        # 3. Check the very last window after the loop finishes
        return s1_count == s2_count