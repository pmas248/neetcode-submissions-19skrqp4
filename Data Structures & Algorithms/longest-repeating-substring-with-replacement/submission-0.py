class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = maxf = res = 0
        for i,r in enumerate(s):
            count[r] = 1 + count.get(r, 0)
            maxf = max(maxf, count[r])

            while (i - l + 1) - maxf > k:
                print(i,l,maxf,k,r)
                count[s[l]] -= 1
                l += 1
            
            res = max(res, i-l + 1)

        return res