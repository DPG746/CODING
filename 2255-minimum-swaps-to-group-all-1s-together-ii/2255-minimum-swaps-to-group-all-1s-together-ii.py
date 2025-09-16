from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)   # total number of 1's
        if k == 0 or k == len(nums):
            return 0    # already grouped (all 0s or all 1s)

        # Extend the array to handle circular case
        nums_extended = nums + nums  

        # Sliding window of size k
        current_ones = sum(nums_extended[:k])
        max_ones = current_ones

        for i in range(k, len(nums_extended)):
            current_ones += nums_extended[i] - nums_extended[i - k]
            max_ones = max(max_ones, current_ones)

        # Minimum swaps needed
        return k - max_ones
