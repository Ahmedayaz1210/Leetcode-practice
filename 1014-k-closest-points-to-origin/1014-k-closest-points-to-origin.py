'''
UNDERSTAND:
- Inputs: Given an array of integer pairs which are points on a graph, each subarray in the array is of length 2 because it has x and y coordinates. Also given an int k which is the size of result array we will be returning.
- Have to find k amount of points inside our points array which are closest to the origin (0,0)
- To find the closest origin we use the Euclidean distance
- Output: Have to return k amount of the closest points in a list
- For Eucliden distance our (x1,y1) is the (0,0) origin, which means the formula can be simplified to √(x² + y²)
- We don't have to return back the points in the same order as we got them
- Also no 2 points will have the same distance from the origin so our answer is guaranteed to be unique
- TC? SC? 
- Size of points array? 1 <= points.length <= 10^4
- Size of k: 1 <= k <= points.length
- Each point can be? -10^4 <= x_i, y_i <= 10^4


MATCH:
- We just need to return k amount of points with smallest distance
- That means a data structure which keeps smallest points in order and should be of length k
- Can use max heap for this

PLAN:
- Initialize a max heap
- Run a loop over the points list
- First make sure the max heap is of size k, if it isn't keep adding pairs because technically they are the closest for now
- Remember to push the points with it's distance as [-Distance, point] in the max heap
- Once max heap becomes size k and we still have points left, now calculate ED for each point you are on and compare with the biggest in the max heap which will be at the top, if this is smaller, pop and push else keep moving
- In the end remove the distance from the array and return back just the points
'''
import math
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for i in range(len(points)):
            distance = math.sqrt(points[i][0]**2 + points[i][1]**2)
            point_distance = [-distance, points[i]]
            
            if len(max_heap) != k:
                heappush(max_heap, point_distance)

            else:
                if -point_distance[0] < -max_heap[0][0]:
                    heappop(max_heap)
                    heappush(max_heap, point_distance)

        

        return [x[1] for x in max_heap]
                