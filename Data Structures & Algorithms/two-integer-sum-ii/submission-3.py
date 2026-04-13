class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            for j in numbers:
                if i!=j and i+j == target:
                    return [numbers.index(i)+1,numbers.index(j)+1]
