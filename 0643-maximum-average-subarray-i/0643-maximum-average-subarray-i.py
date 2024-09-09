class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        if k == 1:
            nums.sort()
            return float(nums[len(nums)-1])
        maxAvg = float('-inf')
        l = 0
        tempAvg = nums[l] 
        for r in range(1,len(nums)):
            tempAvg = tempAvg + nums[r]
            print(tempAvg)
            if r - l + 1 < k:
                continue
            elif r - l + 1 == k:
                maxAvg = max(maxAvg, tempAvg / k)
                tempAvg = tempAvg - nums[l]
                l += 1
            

        return maxAvg
        