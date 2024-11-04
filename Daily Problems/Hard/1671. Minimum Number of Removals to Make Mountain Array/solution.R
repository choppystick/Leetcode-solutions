minimumMountainRemovals <- function(nums) {
  n <- length(nums)

  # Calculate LIS from the left side
  left_lis <- integer(n)
  temp <- c()
  for (i in 1:n) {
    pos <- findInterval(nums[i], temp, left.open = TRUE) + 1
    if (pos > length(temp)) {
      temp <- c(temp, nums[i])
    } else {
      temp[pos] <- nums[i]
    }
    left_lis[i] <- pos
  }

  # Calculate LIS from the right side (for LDS)
  right_lis <- integer(n)
  temp <- c()
  for (i in n:1) {
    pos <- findInterval(nums[i], temp, left.open = TRUE) + 1
    if (pos > length(temp)) {
      temp <- c(temp, nums[i])
    } else {
      temp[pos] <- nums[i]
    }
    right_lis[i] <- pos
  }

  # Calculate the maximum mountain length
  max_mountain <- 0
  for (i in 2:(n - 1)) {
    if (left_lis[i] >= 2 && right_lis[i] >= 2) {
      max_mountain <- max(max_mountain, left_lis[i] + right_lis[i] - 1)
    }
  }

  # Return minimum elements to remove
  if (max_mountain > 0) {
    return(n - max_mountain)
  } else {
    return(n)
  }
}

# Example usage
nums1 <- c(1, 3, 1)
nums2 <- c(2,1,1,5,6,2,3,1)
nums3 <- c(100,92,89,77,74,66,64,66,64)
print(minimumMountainRemovals(nums1))  # Output: 0
print(minimumMountainRemovals(nums2))
print(minimumMountainRemovals(nums3))