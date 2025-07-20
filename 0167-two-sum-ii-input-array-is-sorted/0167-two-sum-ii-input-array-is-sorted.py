class Solution(object):
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            curr = nums[left] + nums[right]
            if curr == target:
             return [left+1, right+1]  # ✅ Make sure this line is inside the function
            if curr > target:
                right -= 1
            else:
             left += 1

        return None  # ✅ Also properly indented


  