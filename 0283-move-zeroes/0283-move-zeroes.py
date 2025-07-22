from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Moves all 0s to the end while keeping the order of non-zero elements.
        """
        pos = 0  # Position to place the next non-zero

        # Move non-zero values to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Fill the remaining elements with 0
        for i in range(pos, len(nums)):
            nums[i] = 0
