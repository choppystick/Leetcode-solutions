from bisect import *

class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Calculate LIS from the left side
        left_lis = [0] * n
        temp = []
        for i in range(n):
            pos = bisect_left(temp, nums[i])
            if pos == len(temp):
                temp.append(nums[i])
            else:
                temp[pos] = nums[i]
            left_lis[i] = pos + 1
        
        # Calculate LIS from the right side (for LDS)
        right_lis = [0] * n
        temp = []
        for i in range(n - 1, -1, -1):
            pos = bisect_left(temp, nums[i])
            if pos == len(temp):
                temp.append(nums[i])
            else:
                temp[pos] = nums[i]
            right_lis[i] = pos + 1
        
        # Calculate the maximum mountain length
        max_mountain = 0
        for i in range(1, n - 1):
            if left_lis[i] >= 2 and right_lis[i] >= 2:
                max_mountain = max(max_mountain, left_lis[i] + right_lis[i] - 1)
        
        # Return minimum elements to remove
        return n - max_mountain if max_mountain > 0 else n