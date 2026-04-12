class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sort = sorted(set(nums))
        count = 0
        max = 0
        print(sort)
        for i in range(0, len(sort)-1):
            print(sort[i], sort[i+1])
            if (sort[i]+1) != (sort[i+1]):
                if sort[i+1] == 0:
                    count+=1
                    max = count
                if max < count:
                    max = count
                count = 0
            else:
                count+=1
                if max < count:
                    max = count
            print(max+1)

        return max+1
