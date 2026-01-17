class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r, ans = 0, len(numbers) - 1, [0] *2
        print(ans)
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                ans[0] = l+1
                ans[1] = r+1
                return ans

'''
* Understand: Given 1d sorted list in increasing order, have to find two indices from the array where array[id1] and array[id2] add up to be the given target integer. Here index starts from 1 instead of 0, so we have to add one to each index before returning. We have to only use constant space to do this, so using a variable we have to find the solution, we will also be given at least 2 numbers in the array, read rest of constraints from description and there is only one solution to this problem


* Match: Seems like a problem where we have to keep track of two numbers at a time to check their sum so two pointers. 


* Plan: 
* We can keep two pointers, one at start other at end, if sum is big move right in if small move left out. This works since it is a sorted array. 
* So while left is smaller than right
* we check if sum is big move right elif move left elif same so return ans by +1 both indexing

* Evaluate:
* TC: O(n) running through answers once
* SC: O(2) simply O(1) because exactly one solution and only two numbers
* Solved all by myself!
'''