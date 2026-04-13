class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        for i in numbers:
            for j in numbers:
                if i!=j and i+j == target:
                    return [numbers.index(i)+1,numbers.index(j)+1]
                    '''
    
        #Hashmap:
        '''
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in mp:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []
        '''

        #two-pointer:
        l,r = 0, len(numbers)-1

        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum > target: r-=1
            elif curSum < target: l+=1
            else: return [l+1,r+1]
        return []

        
