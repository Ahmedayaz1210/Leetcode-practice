class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray = float('inf')
        current_sum = 0
        l = 0

        for r in range(len(nums)):
            current_sum += nums[r]
            
            while current_sum >= target:
                min_subarray = min(min_subarray, r - l + 1)
                current_sum -= nums[l]
                l += 1

        return min_subarray if min_subarray != float('inf') else 0