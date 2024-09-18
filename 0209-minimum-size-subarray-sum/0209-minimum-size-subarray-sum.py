'''
UNDERSTAND:
- Input: integer target and a list of integers nums
- Have to find the smallest length of a subarray within nums array such that that subarray's sum = target
- There can be alot of subarrays which add up to target
- Have to return one with the smallest length
- output: integer which is length of the smallest subarray 
- how big int target can be? >= 1 and <= 10^9
- how big can nums be? >= 1 and <= 10^5
- how big can each int be inside num? >= 1 and <= 10^4
- What if all of nums can't add up to target? return 0
- what if all of the ints in nums are greater than our target? return 0
- Time complexity? O(n)
- Space Complexity? 

MATCH:
- Find a window in nums which add up to target
- Sliding window technique

PLAN:
- Create a min_subarray counter to keep track of shortest subarray with the sum
- Create your two left and right window pointers
- Create a list to keep track of ints inside our window
- Run a loop over nums with the r pointer:
- if sum of window < target:
- keep moving right
- if sum of window == target:
- update min_subarray accordingly
- update left pointer
- if sum of window > target:
- keep shrinking from left until window's sum goes < target
- return min_subarray

EVALUATE:
- I shouldn't have created a list for window, it would've been much easier to create an integer for it, creating a window takes too much space and even exceeded time limit
- Other than that solution was good, slight logic error
- Time Complexity: O(n)
- Space Complexity: O(1)
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_subarray = float('inf')
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while curr_sum >= target:
                min_subarray = min(min_subarray, r-l+1)
                curr_sum -= nums[l]
                l += 1
                

        return min_subarray