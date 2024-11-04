compressString <- function(word) {
  if (nchar(word) == 0) return("")
  
  result <- character(0)
  i <- 1
  n <- nchar(word)
  
  while (i <= n) {
    char <- substr(word, i, i)
    count <- 1
    
    # Count consecutive occurrences of the current character
    while ((i + count) <= n && 
           count < 9 && 
           char == substr(word, i + count, i + count)) {
      count <- count + 1
    }
    
    # Add the compressed representation to result
    result <- c(result, paste0(count, char))
    i <- i + count
  }
  
  # Join all parts together
  return(paste(result, collapse=""))
}

# Test cases from the provided example
test_cases <- c(
  "o",
  "vvv",
  "xxlaa",
  "xbbbbjj",
  "yyyyyyyyfffccccqqwwffffffffrrrrrrrrraaaaayyyyyyyyy",
  "uuuuuuuuuuccccccvvvvvvvyyyyyyyylyyyqqqqqqqqqoaqqqq",
  "yyyyyyyyyyyyyttttttttttttttttttttttttttttttttttttttttttttttttttvvvvvvvvvvvvvvvvvvvvvvvvvaaaaaaaaaajj"
)

# Run test cases
cat("Test Results:\n")
for (i in seq_along(test_cases)) {
  result <- compressString(test_cases[i])
  cat(sprintf("Test Case %d:\n", i))
  cat(sprintf("Input:  %s\n", test_cases[i]))
  cat(sprintf("Output: %s\n\n", result))
}