'''
Understand:
- Given list of ints nums and an int k
- k is the fixed size of window which moves across nums continously
- At each iteration, the window slides over to next position, so cutting element from left and adding one on right
- We have to find the max number in each sliding window we can make of size k and in the end from all windows we take the max numbers and return them as a list
- Check constraints
- We are guaranteed at least one number in nums and k to be 1 as well as the smallest value

Match:
- So question pretty much itself tells we need to use sliding window approach
- Next question is how do we keep track of max in each window without looping over the window again and again, so BF is to run max function or smth over each window which will be O(k*(n-k)) in worst time
- But how can we optimize this? Can we do this in a way that we loop over the whole array once and keep finding max in each window?
- We can use a monotonically decreasing queue where first element is always the max and all rest are decreasing, each time we try to add a new element we remove from behind because from behind we encounter the smallest element and we can compare the new one to it, if new one is bigger we automatically know the last element in dequeue is useless and it will never be greater than this new one which is coming after it in idx so it will be included in next window(s) so this way we can remove the one already in the queue from behind and we keep removing until the new element is greater
- now remember we store idx not the actual value because now if the max at front is out of bounds we can check if by comparing it's idx with left pointer, if left pointer is > start of dequeue we can remove the element from dq


'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = 0
        ans = []
        for r in range(len(nums)):
            if dq and dq[0] < l:
                dq.popleft()
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if r - l + 1 == k:
                ans.append(nums[dq[0]])
                l += 1
            
            
        return ans
        