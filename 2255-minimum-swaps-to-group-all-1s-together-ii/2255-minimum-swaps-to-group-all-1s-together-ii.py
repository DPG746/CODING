from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #window size - count of 1
        windowSize=0
        for i in range(len(nums)):
            if nums[i]==1:
                windowSize+=1

        #find zeros in first window
        curZeros=0
        for i in range(windowSize):
            if nums[i]==0:
                curZeros+=1
        #solve for remaining window
        minZeros=curZeros
        start=0
        end=windowSize-1
        n=len(nums)

        while start<n:
            #if removed element was 0, decrement 0 counter
            if nums[start]==0:
                curZeros-=1
            start+=1
            #if included element is 0, increment 0 counter
            end+=1
            if nums[end%n]==0:
                curZeros+=1

            minZeros=min(minZeros,curZeros)
        return minZeros
