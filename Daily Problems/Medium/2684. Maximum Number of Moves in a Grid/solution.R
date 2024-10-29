# R solution for 2684. Maximum Number of Moves in a Grid

maxMoves <- function(grid) {
  m <- nrow(grid)
  n <- ncol(grid)
  
  # Initialize dp matrix with -1
  dp <- matrix(-1, nrow = m, ncol = n)
  
  dfs <- function(row, col) {
    # If already computed, return cached result
    if (dp[row, col] != -1) {
      return(dp[row, col])
    }
    
    max_moves <- 0
    next_col <- col + 1
    
    # Check all possible next moves
    for (next_row in (row-1):(row+1)) {
      # Check if move is valid
      if (next_row >= 1 && next_row <= m &&
          next_col <= n &&
          grid[next_row, next_col] > grid[row, col]) {
        
        max_moves <- max(max_moves, 1 + dfs(next_row, next_col))
      }
    }
    
    # Cache and return result
    dp[row, col] <<- max_moves
    return(max_moves)
  }
  
  # Try starting from each cell in first column
  max_possible_moves <- 0
  for (i in 1:m) {
    max_possible_moves <- max(max_possible_moves, dfs(i, 1))
  }
  
  return(max_possible_moves)
}

# Testcases
grid <- matrix(c(2,4,3,5,
                 5,4,9,3,
                 3,4,2,11,
                 10,9,13,15), 
               nrow=4, byrow=TRUE)
grid2 <- matrix(c(3,2,4,2,1,9,1,1,7), nrow=3, byrow=TRUE)

grid3 <- matrix(c(
  139, 122, 184, 109, 109, 77,
  159, 36, 122, 218, 239, 4,
  18, 293, 137, 54, 254, 80,
  13, 199, 175, 10, 90, 147,
  170, 109, 210, 27, 256, 263,
  153, 156, 192, 153, 35, 107,
  179, 193, 229, 222, 263, 282,
  40, 191, 30, 187, 139, 223,
  276, 90, 300, 224, 27, 222,
  95, 201, 248, 112, 124, 138,
  10, 7, 266, 104, 190, 68
), nrow=11, ncol=6, byrow=TRUE)


result <- maxMoves(grid3)
print(result)  # Should output 3