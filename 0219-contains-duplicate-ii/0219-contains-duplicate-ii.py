'''
1. UNDERSTAND:
* Question basically asks: Find 2 numbers in the array that are equal and are at most k indices apart from each other
* Have two pointers i and j creating our window
* Have to find at least a pair of numbers which
	* Condition 1: Are Equal
	* Condition 2: Are <= k indices away from each other
	* Ex: In the first example, there are two "1"s so first condition satisfied, then they are 3 indices apart which satisfies <= 3(k) condition
* Indices are looked at by taking absolute value between them because it will always be negative since higher index comes after
* K is our max window size, this gives away that we can use Sliding Window technique
* How long can be the array? 1 - 10^5
* How big can be each value? -10^9 - 10^5
* How big can be k? 0 - 10^5
* K will always be smaller than length of array right? Yes
* Edge case: how would I handle just one value in array? Assuming false because we need at least two identical numbers

2. MATCH:
* Finding distinct values can be done using hashing and CD I was done using that
* Can use sliding window to create a window between a number and it's corresponding number later in the array

3. PLAN:
* Have Two pointers:
* i at index 0 and j at index 1
* Run a loop through the array until right pointer reaches the end
* Create a window between pointer i and j
* if nums[i] != nums[j]:
	* if abs(i-j) <= k: increment j
	* else if the abs val is greater increment i, so the left pointer gets incremented to keep the k window size
* else (means we found a pair): return True
* In the end return False
* I got it WRONG: supposed to use a hashmap to keep track of elements you've seen within the last k elements.
* The mistake I made was checking if elements at both pointers are equal but we are suppose to check within the window that's why I was failing the testcase: [0,1,2,3,2,5]
* The hashset checks it for you and you maintain the set with the length k

4. EVALUATE:
* In worst case we will be looping the whole array so time complexity : O(n)
* Normally space would be O(k) but if k equals len(nums) it could be O(n)
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if len(nums) <= 1:
        #     return False
        # if k < 1:
        #     return False

        # i, j = 0, 1

        # while (j <= len(nums)-1):
        #     if abs(i-j) <= k:
        #         if nums[i] != nums[j]:
        #             j += 1
        #         else:
        #             return True
        #     else:
        #             i += 1
            

        # return False

        window = set()

        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l+=1

            if nums[r] in window:
                return True
            window.add(nums[r])

        return False
