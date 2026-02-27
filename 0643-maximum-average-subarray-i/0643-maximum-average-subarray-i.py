'''
Understand:
- Have to find a contig subarray where k amounts of elements have the highest average.
- What happens if we have less than k elements

Match:
- Since we know this is contig array we are finding and the length of that array is given k
- We can use fixed sliding window to solve this

Plan:
- l = 0

'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        maxAvg = float('-inf')
        currSum = 0
        
        for r in range(len(nums)):
            currSum += nums[r]
            if r - l + 1 == k:
                currAvg = currSum / k
                maxAvg = max(maxAvg, currAvg)
                currSum -= nums[l]
                l += 1
                
        return maxAvg