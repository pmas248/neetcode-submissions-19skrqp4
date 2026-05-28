class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if not matrix[i][-1] < target:
                l,r = 0, len(matrix[i])-1
                while l <= r:
                    mid = (l + r)//2
                    midval = matrix[i][mid]
                    if target > midval:
                        l = mid + 1
                    elif target < midval:
                        r = mid - 1
                    else:
                        return True
        return False
