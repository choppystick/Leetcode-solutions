# Python solution for 2684. Maximum Number of Moves in a Grid

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] represents the maximum moves possible starting from cell (i,j)
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(row: int, col: int) -> int:
            # If we've already computed this cell, return the cached result
            if dp[row][col] != -1:
                return dp[row][col]
            
            max_moves = 0
            # Check all possible next moves
            for next_row in [row-1, row, row+1]:
                next_col = col + 1
                
                # Check if move is valid
                if (0 <= next_row < m and 
                    next_col < n and 
                    grid[next_row][next_col] > grid[row][col]):
                    
                    max_moves = max(max_moves, 1 + dfs(next_row, next_col))
            
            #caching results
            dp[row][col] = max_moves
            return max_moves
        
        max_possible_moves = 0
        for i in range(m):
            max_possible_moves = max(max_possible_moves, dfs(i, 0))
            
        return max_possible_moves