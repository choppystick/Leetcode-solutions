# R solution for 1277. Count Square Submatrices with All Ones

count_submatrices <- function(matrix){
  if (length(matrix) == 0 || length(matrix[[1]]) == 0) {
    return(0)
  }
  
  m <- length(matrix)
  n <- length(matrix[[1]])
  count <- 0
  
  for (i in 1:m) {
    for (j in 1:n) {
      if (matrix[[i]][j] == 1 && i > 1 && j > 1) {
        matrix[[i]][j] <- min(matrix[[i - 1]][j], matrix[[i]][j - 1], matrix[[i - 1]][j - 1]) + 1
      }
      count <- count + matrix[[i]][j]
    }
  }
  
  return(count)
}


#testcases
test1 <-list(c(0,1,1,1),
             c(1,1,1,1),
             c(0,1,1,1))
             
print(count_submatrices(test1))