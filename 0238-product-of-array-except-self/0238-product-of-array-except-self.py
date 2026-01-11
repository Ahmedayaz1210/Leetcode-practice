class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        ans = [1] * len(nums)
        
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(0,len(nums)):
            ans[i] = left[i] * right[i]

        return ans

"""
* Understand: Given an array of ints called nums
		* Have to return an array of ints called answer
		* Each answer[i] should be product (multiplication) of all of ints in nums besides nums[i]
		* So except the current one, multiple everything by each other in the array and put in answers current position
		* we will have at least two ints in our input array and numbers can't be bigger than 30 or less than -30
		* Just wondering how does "The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer" help me as an input? Can ignore in python
		* So edge case could be that if we have two numbers, just return the same array as answer because they are just product of themselves, or actually it would be same array just reversed
		
* Match: What tools can I use to solve this?
		* Repeating numbers tell can't use a hashset obv
		* Brute force would be to loop over nums each time, make product of everything besides current one u are on and just put that in answer[i]
		* what would be TC for that? O(n^2) because for each i we loop the array again
		* How can this be done in O(n)? Hint says to use prefix and suffix products. so somehow calculating before hand and after hand for each position? I think I got it, as you are looping before you get to i, you keep calculating everything on it's left, so if i = 2 and int is 3 in first example, u compute 1 x 2 and store it, then same thing for after i
		* But confused again? how would this be faster? how do we precompute in one go
		* So we would loop twice, first time to fill left array, then to fill right array, so this way we have left of all elements and right of all elements product and then we can just fill answer array accordingly, space is O(n) because we just create 4 arrays of same length

* Plan:
		* Initialize our 3 arrays
		* Run a loop over nums
		* fill in the left array by storing first value as one
		* left[0] = 1
				for i from 1 to n-1:
						left[i] = left[i-1] * nums[i-1]
		* Run a loop over nums again
		* fill in right array by storing last element as 1
			right[n-1] = 1
			for i from n-2 to 0:
					right[i] = right[i+1] * nums[i+1]
		* Multiply values at i for both left and right, store in ans and return 

* Evaluate: 
* TC: O(n) looping through arrays twice so simplified to O(n)
* SC: O(n) storing 3 arrays, all O(n)
* I would say got 60% of the problem myself, brute force was really easy O(n^2), firguring out how to move left and right was a bit tricky
"""