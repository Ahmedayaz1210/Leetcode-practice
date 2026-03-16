'''
Understand:
- Given an array of ints nums and an int var target
- Have to find a contig subarray where all elements in the subarray add to to the target
- But we have to find the minimal length one, so shorted subarray which satisfies the condition
- We return the size of that subarray, else return 0
-Check constraints

Match:
- Contig sequence or subarray tells that we can use sliding window to kind of expand the subarray if our curr sum is < target and shrink if it is > target
- I don't think we need any other data structure because we can use two pointers to keep track of the sum, for example as r keeps moving we increase and then we can decrease sum using l pointer

Plan:
- l = 0
- 
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        min_len = float('inf')
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                min_len = min(min_len, r - l + 1)
                currSum -= nums[l]
                l += 1
            

        return min_len if min_len != float('inf') else 0
    