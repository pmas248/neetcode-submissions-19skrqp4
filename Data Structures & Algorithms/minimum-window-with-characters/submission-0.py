class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        countT = defaultdict(int)
        for i in t:
            countT[i] += 1
        
        res, resLen = [-1, -1], float("infinity")
        
        for i in range(len(s)):
            countS = defaultdict(int)
            for j in range(i, len(s)):
                countS[s[j]] += 1

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break

                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""
    