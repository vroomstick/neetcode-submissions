class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []

        for row in matrix:
            for num in row:
                flat.append(num)
        
        l = 0 
        r = len(flat) - 1

        while l <= r:
            median = (l + r) // 2

            if target < flat[median]:
                r = median - 1
            elif target > flat[median]:
                l = median + 1
            else:
                return True

        return False

