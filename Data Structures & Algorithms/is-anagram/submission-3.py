class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sum1 = sum2 = 0
        # if len(s) == len(t): 
        #     for i in range(len(s)):
        #         sum1 = sum1 + int(ord(s[i]))
        #         sum2 = sum2 + int(ord(t[i]))
        #     if sum1 == sum2:
        #         return True
        # return False

        if len(s) == len(t): 
            t1 = defaultdict(int)
            t2 = defaultdict(int)
            
            for i in range(len(s)):
                t1[s[i]] += 1
                t2[t[i]] += 1

            return t1 == t2
        return False