# Python solution for 2501. Longest Square Streak in an Array

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = -1
        
        for num in nums:
            streak = 1
            n = num
            while n * n in nums_set and n * n <= 10**5:
                streak += 1
                n = n * n
            if streak >= 2:
                max_len = max(max_len, streak)
                
        return max_len