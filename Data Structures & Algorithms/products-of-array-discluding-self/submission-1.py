class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = False
        zeropos = []
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zero = True
                zeropos.append(i)

        res = []
        if zero == False:
            for i in range(len(nums)):
                res.append(int(prod/nums[i]))

        else:
            if len(zeropos) > 1: 
                for i in range(len(nums)):
                    res.append(0)
            else:
                for i in range(len(nums)):
                    if i not in zeropos:
                        res.append(0)
                    else:
                        res.append(prod)
        
        return res
                

