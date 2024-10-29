# R solution for 344. Reverse String

reverse_string <- function(s){
  left = 1
  right = length(s)
  
  while (left < right){
    temp <- s[left]
    s[left] <- s[right]
    s[right] <- temp
    
    left = left + 1
    right = right - 1
  }
  
  return(s)
}

test1 <- c("h", "e", "l", "l", "o")
test2 <- c("H", "a", "n", "n", "a", "h")

reverse_string(test1)
reverse_string(test2)