class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
            if hashmap[nums[i]] > 1:
                return nums[i]'''

        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow