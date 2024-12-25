'''
UNDERSTAND:
- Inputs: Given a stream of int numbers and have to find the median
- If array is odd, median is mid num else median is mean of mid 2 nums
- addNum adds the given number to our stream of int nums
- findMedian finds the median from that stream array
- It's a hard problem because we have to do in worst case for 50,000 calls and O(n) and O(n log n) wouldn't work for it
- So aiming for log n
- -10^5 <= num <= 10^5
- Guaranteed to have at least 1 number in stream before findMedian is called
- At most 5 * 10^4 calls

MATCH:
- Can do this using sorting or a heap but both can be O(n log n)
- If we use binary search we can find median in O(log n) but moving the elements is still O(n)
- Can use 2 heaps, one min and one max, lower half of the array can be max heap so its highest will be at the top which is first half's end from the original array and for upper half we can use min heap so the starting of the upper half which is the middle in original remains on top
- This way we can do this in O(log n) + O(log n) = O(log n) average because we have access to middle from both min and max heap and if its even array then we can average the top of both

PLAN:
- Initialize 2 heaps
- One max for lower half, one min for upper half, this maintains middle at the top and keeps it log n average

- addNum: Initial case:

If it's the first number, put it in maxHeap

For all other numbers:
First decide placement:

If minHeap is empty OR number < minHeap top: belongs in maxHeap
Otherwise: belongs in minHeap

Then handle balancing:

If adding to maxHeap would make it too big (>1 difference):
Move maxHeap's top to minHeap, then add new number to maxHeap
If adding to minHeap would make it too big:
Move minHeap's top to maxHeap, then add new number to minHeap

- findMedian: if lengths of both heaps are same, pop out the top from both and return mean
- Else return the top of larger of the two
'''
from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # First check where number belongs by comparing with minHeap's smallest
        if not self.min_heap or num < self.min_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
            
        # Balance heaps if needed
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)


    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()