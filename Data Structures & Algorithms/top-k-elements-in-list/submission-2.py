class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        for i in range(len(nums)):
            temp[nums[i]] += 1
        
        res = []
        for i in range(k):
            top = max(temp, key=temp.get)
            res.append(top)
            temp.pop(top)

        return res