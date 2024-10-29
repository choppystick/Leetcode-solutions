# R solution for 2501. Longest Square Streak in an Array

longestSquareStreak <- function(nums) {
  unique_nums <- unique(nums)
  nums_set <- as.character(unique_nums)
  max_len <- -1
  
  for (num in unique_nums) {
    streak <- 1
    n <- num
    while (as.character(n * n) %in% nums_set && n * n <= 10^5) {
      streak <- streak + 1
      n <- n * n
    }
    if (streak >= 2) {
      max_len <- max(max_len, streak)
    }
  }
  
  return(max_len)
}