'''
UNDERSTAND:
- Input: Given array of integers
- Have to take the top 2 largest numbers each time we loop through it and if the numbers are same, they both get taken out because it returns 0. Else if they are not the same we subtract y stone from x stone and put the result back into the array
- Output: After doing this constantly, if at the end we are remained with 1 stone, we simply return the number else we return 0 if array is empty
- TC? SC?
- How big can each stone weight be? 1 <= i <= 1000
- How big can our array be? 1 <= len <= 30
- So atleast we will start with 1 stone, then we simply return it, could be edge case
- Stone weight will also be at least 1, if we have 0, don't append it back

MATCH:
- Since we know we will always be dealing with the top two largest numbers, we can utilise heaps / PQ to keep track of those numbers at each iteration. 

PLAN:
- So we use a max heap to keep track of the top 2 numbers
- If the numbers are the same, don't return back anything and rearrange the Heap
- Else return the difference y - x and rearrange the heap

- Start with initializing our heap
- Loop over the stones array and append each number into our heap by negating it
- Now run a loop until length of heap is 1 or 0:
    - Keep popping top 2 numbers and remove the negation:
        - If they are the same, move on don't append 0
        - Else subtract the y (first popped) and x (second popped), return the difference back to heap
- Once the while loop is done, return back 0 if heap is empty else the only remaining number

EVALUATE:
- Solved the problem myself on my birthday wohooo
- TC: O(n log n) for heapifying the whole stones array which is n and push/pop take log n
- SC: O(n) in worst case we have all stones in the heap

Check Notes for why Heapify is O(n): https://www.notion.so/Leetcode-Practice-Notes-9104bfaf5dcc4fceb31ebb558b4ffad9?pvs=4#1596cef1fec6800296bdfb3893dc14ec

'''
from heapq import heapify, heappush, heappop 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            y = -y
            x = -x
            if x == y:
                continue
            else:
                heappush(stones, -(y - x))

        if not stones:
            return 0
        else:
            return -stones[0]
