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