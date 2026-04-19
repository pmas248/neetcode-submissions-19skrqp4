class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        submat = len(matrix) - 1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                submat = i-1
                break
        
        if submat < 0:
            return False
            
        for i in range(len(matrix[submat])):
            print(matrix[submat][i])
            if matrix[submat][i] == target:
                return True
        return False