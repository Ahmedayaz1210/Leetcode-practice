class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer = [1]*(len(nums))
        # for i in range(0,len(nums)):
        #     for j in range(0,len(nums)):
        #         if i != j:
        #             answer[i] *= nums[j]
        # return answer
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            answer[j] *= postfix
            postfix *= nums[j]
        return answer
        
"""
* So we are given an array of numbers and we need to return a result array in which each element[ i ] is product of the whole nums array besides nums [ i ]
* Basically at each corresponding indexes in both arrays we won't add the product of that current index from nums array.
* Also have to find an answer in O(n), which makes it harder
* Let's start with a brute force and don't focus on time complexity
* **Brute force approach**
* Start i and j from 0
* If i and j don't have the same index, only then multiply
* You can't do if i == j and i != len(nums) - 1:
                    j += 1
Because: When i == 0, you enter the inner loop.
Inner loop (j): j iterates over [0, 1, 2, 3].
When j == 0, i == j so you increment j to 1.
answer[0] is multiplied by nums[1], so answer[0] becomes 1 * 2 = 2.
Next iteration of inner loop.
When j == 1, i != j so you multiply answer[0] by nums[1] again, which is not desired.
* answer [ i ] = answer [ i ] * nums [ j ]
* **Time complexity; O(n^2)**
* Now let's try to make it O(n)
* **Solution**
* You use the postfix and prefix method to do this in O(n)
"""
