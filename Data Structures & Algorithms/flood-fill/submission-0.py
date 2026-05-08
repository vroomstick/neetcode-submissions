class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image


        def dfs(grid, r, c):
            row = len(grid)
            col = len(grid[0])

            if min(r, c) < 0 or r == row or c == col or grid[r][c] != original:
                return

            grid[r][c] = color

            dfs(grid, r + 1, c)
            dfs(grid, r - 1 , c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

            return grid

        return dfs(image, sr, sc)