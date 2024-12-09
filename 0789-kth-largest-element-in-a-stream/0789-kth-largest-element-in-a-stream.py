'''
UNDERSTAND:
- Inputs: To start off we will be given an integer k, which is the kth highest number we have to return each time function "add" is called from here on. Secondly given a starting list we will be using throughout. Will return null because initializing
    - After initializing "add" will be called which will add the given "value" and return back the kth highest from our list, we will use the same k each time
- Output: Either null for initializing or returning back kth highest integer if add is called
- K is int, nums is list of ints, val is also int
- TC? SC?
- How big can our k be? >= 1 <= nums.length + 1
- How big can our nums be? 0 to 10^4 inclusive
- Only integers right? Yes
- Can we have negative numbers in nums or k? Only in nums
- How many calls can be made at max?10^4 max calls can be made to add

MATCH:
- Since we have out pop out or return some integer highest number or value, we can use a priority queue and heap so we can maintain the highest at the top and keep popping k amount of times.

PLAN:
- So the approach in Match in wrong, we do use heaps but we don't need to use a max heap, we use a trick with min heap.
- We take k amount of the highest elements from our given original array and we store those k numbers in a heap of length k and always the smallest one will be at the top.
- Ex: we have 4,5,8,2 we want kth highest, k = 3, top 3 would be 4,5,8. In a min heap, 4 would be at the top and that's exactly the kth highest or the smallest out of all k big numbers
- So we use this approach

- When we get our Initial call
- Initialize a min heap of length k
- Only append top k elements into the heap
- Heapify it
- Now for add function, you append "val" to original list and compare it to the top of the min heap, if it's greater, pop out of the top of min heap and put the new number in, regardless of what happens the same top gets returned here even if it is popped out


'''
from heapq import heapify, heappush, heappop 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for num in self.nums:
            if len(self.heap) != self.k:
                heappush(self.heap, num)
            else:
                if num > self.heap[0]:
                    heappop(self.heap)
                    heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) != self.k:
            heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)