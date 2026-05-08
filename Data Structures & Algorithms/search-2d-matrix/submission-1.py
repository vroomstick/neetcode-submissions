class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        flat = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                flat.append(matrix[i][j])

        left = 0
        right = len(flat) - 1

        while left <= right:
            median = left + (right - left) // 2
            if target > flat[median]:
                left = median + 1
            if target < flat[median]:
                right = median - 1
            if target == flat[median]:
                return True

        return False
        
        