class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            
        res = []
        for i in range(k):
            highest = max(dict, key=dict.get)
            res.append(highest)
            dict.pop(highest)
        
        return res