class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (right + left) // 2
            n = len(matrix[0])
            row = mid // n
            column = mid % n
            value = matrix[row][column]
            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else: 
                left = mid + 1
        
        return False