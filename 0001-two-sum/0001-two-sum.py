class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 
        Brute force approach
        answer = []
        for i in range (0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i),answer.append(j)
        return answer
        '''
        hashMap = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[nums[i]] = i
        return
            