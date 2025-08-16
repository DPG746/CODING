class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        n = len(nums)

        # Find all positions of `key` in nums
        key_indices = [i for i in range(n) if nums[i] == key]

        # For each index in nums, check if it's within k distance from any key index
        for i in range(n):
            for j in key_indices:
                if abs(i - j) <= k:
                    result.append(i)
                    break   # No need to check further if condition is satisfied

        return result
