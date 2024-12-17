'''
UNDERSTAND:
- Inputs: Have an integer array "nums" and an integer number "k"
- Have to find kth largest element from the nums array
- Remember if a number has a duplicate, it counts as a k too, we are not looking for kth distinct largest number so we can count dups as well
- Problem also asks us if we can solve without sorting
- Output: Return kth largest element
- TC? SC?
- Size of nums: 1 <= k <= nums.length <= 105
- nums[i]: -104 <= nums[i] <= 104
- Range of k: 1 <= k <= nums.length <= 105

MATCH:
- Obviously we can sort this and return kth index
- But sorting is not allowed
- Since we can count duplicates
- Can just use a max heap and pop out k amount of times

PLAN:
- Convert nums to negative nums
- Heapify it
- Pop out elements k-1 times because kth time it would be the number we want
- Now return back the top

EVALUATE:
- Did the problem myself
- First I was trying to return just the kth element after hapifying but thats not a sorted order
- So we have to pop out k-1 times so kth elements comes on top
- TC: O(n + k log n) n for heapifying and then popping k amount of times 
- SC: O(n)


OPTIMAL APPROACH:
- This can be done in O(n) TC and O(1) SC by using Quick Select Algorithm
- O(n) is average it can be O(n^2)
- O(1) SC because of in order modification/swapping
- For detailed explanation check notion notes
- Leetcode isn't approving Quick select because of O(n^2) worst time so submitting with heap approach
'''
from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Max Heap Approach
        
        negated_nums = [-num for num in nums]
        
        heapify(negated_nums)

        for _ in range(k-1):
            heappop(negated_nums)

        return -heappop(negated_nums)
        
        
        # Quick Select Approach:

        # Idx we looking for
        # k = len(nums) - k

        # def quickSelect(l, r):
            
        #     pivot, p = nums[r], l

        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if p > k:
        #         return quickSelect(l, p - 1)

        #     elif k > p: 
        #         return quickSelect(p + 1, r)

        #     else:
        #         return nums[p]

        # return quickSelect(0, len(nums) - 1)

            


