'''
UNDERSTAND:
- Inputs: Given an integer array nums and an integer number k
- Have to find a k length subarray within nums which gives us the highest accumulated sum
- Output: Return back this highest sum integer array, make sure the elements are in the same sequence as they were in original nums
- TC? SC?
- How long can our nums be? 1 to 1000 inclusive
- Guaranteed at least 1 number
- How big can each number be in nums? -10^5 to 10^5 inclusive
- Can have negative numbers
- How big can k be? 1 to nums.length inclusive

MATCH:
- Can use a sliding window approach, and store the maximin sum
- Can use a min heap of size k which will have highest numbers in it

PLAN:
- Use a min heap of size k
- Start by putting first k amount of numbers
- Then as you go through the rest of nums compare the new number with the smallest num in min heap, if it's greater pop the smaller number out and push the new one in
- When pushing make sure you push as a tuple with number's ith position
- Once you have looped through nums, pop elements out of heap and put into a result array, then sort by positions.
- Lastly remove the positions and return back just the values list
'''
from heapq import heapify, heappush, heappop
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
       heap = []

       for i in range(k):
        heap.append([nums[i], i])

       heapify(heap)
       res = []
       for i in range(k, len(nums)):
        if nums[i] > heap[0][0]:
            heappop(heap)
            heappush(heap, [nums[i], i])
    
       while heap:
        res.append(heappop(heap))

       
       res = sorted(res, key = lambda x: x[1])
       
       for r in range(len(res)):
        res[r] = res[r][0]
        
       return res