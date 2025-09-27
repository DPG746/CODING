class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        if n < k:
            return 0

        current =0
        for i in range(k):
            current+=nums[i]

        result=current

        for right in range(k,n):
            current += nums[right]
            current -= nums[right-k]
            result=max(result,current)

        return result/k