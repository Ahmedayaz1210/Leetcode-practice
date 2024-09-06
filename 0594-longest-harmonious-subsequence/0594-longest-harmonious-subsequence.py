'''
UNDERSTAND:
- Given an array of integers nums
- Have to return the longest sequence of an array where the difference between max val and min val is exactly 1
- The wording seems awful because basically for each number we see if that num + 1 exists, we add both to our subarray with their other occurences and return it's length
- There could be different pairs too like in example 2, [1,2], [2,3] and [3,4]. both have length of 2 so 2 is the answer
- We need to find a subsequence of nums where:
a) The difference between the maximum and minimum elements in this subsequence is exactly 1.
b) This subsequence is as long as possible
- Tricky part could be to make different sub arrays for each sequences
- Brute force could be taking each integer and find +1 of it and add it to the sequence
- Also have to keep track of duplicates
- In a sequence there will always be two distinct numbers but they can have as many occurences
- Questions: 
 - min and max length of nums? 1 - 2 * 10 ^ 4
 - how big an each int be? -10^9 to 10^9
 - what if we are given an empty array? 0
-Edge case: all numbers are same, we return 0

MATCH: 
- Finding subsequences is usually sliding window
- Remember when we have to keep track of the middle numbers we use sliding window, so like in example 1 we have to keep track of all of the 2's.
- For the above statement I made a mistake, yes you use a sliding window but here you don't need to keep an array because we are returning an integer so we need to keep track of the window which is right - left long

PLAN:
- Approach 1: Let's start by sorting the array so we can find "difference of 1" integers adjacently
- Approach 2: Initialize a hashmap to keep track of each number and it's occurences
- For each number check if it's +1 or/and (seperate arrays for both) -1 exists in the hashmap, if so, add their occurences and you have a sequence
- Using the sliding window method
- Sort the array first
- Create a window with left (0) and right(1) pointer
- run a loop till right reaches the end
- if the difference is 1, take the max between max tracker and our window
- now check if the difference is < 1, this means same numbers so increase right
- if difference greater than 1 then move over the left pointer because the sequence has been broken
'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        maxLen = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                maxLen = max(maxLen, right - left + 1)
        return maxLen