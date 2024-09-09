#Notes got deleted while refreshing :(
#Passed all test cases but only beats 5%, good progress but a lot of hard coding
'''
My code:
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
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
    
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k

        '''
        In this approach we create the first window from 0 to k - 1 (because of python)
        Then run the loop from k to the end creating each window, removing left most element
        (i-k does that) and adding the nums[i] equivalent to right pointer
        Another thing: better to / k at the end because before that we just need the highest 
        sum, doesn't make sense to / k each time
        '''