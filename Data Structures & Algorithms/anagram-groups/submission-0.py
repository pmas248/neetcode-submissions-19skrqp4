class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for curr_str in strs:
            alpha = [0] * 26
            for char in curr_str:
                alpha[ord(char) - ord('a')] += 1
            res[tuple(alpha)].append(curr_str)
        print(res)

        return list(res.values())