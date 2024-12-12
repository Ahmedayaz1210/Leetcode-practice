'''
UNDERSTAND:
- Input: Given a list of integers "score" where score[i] is the score of the ith athlete in a competition
- Have to find the top 3 highest scores and given those athletes, Gold, Silver and Bronze accodingly. For the rest from 4 to the nth place, they just get their place returned
- Output: Have to return the top 3 as medalists and rest as their placement number
- TC? SC? 
- Guaranteed that each score is UNIQUE
- How big can each score be? 0 to 10^6 inclusive
- How big can score array be? 1 to 10^4 so we are guaranteed at least one athlete or score

MACTH:
- Heap/PQ because we want numbers in descending order so can use max heap property

PLAN:
- Initialize a max heap
- Pop numbers out of score until empty 
- Check if they are first three, append medals
- Else their placement number
- Tricky part: Need to return the positions in same way we got input numbers
- so if highest number was at the end of original score list, we have to put gold there
- Can't store key value pairs in heaps
- So we can make a tuple of (-score, position)

'''
from heapq import heapify, heappush, heappop
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        for i in range(len(score)):
            score[i] = [-score[i], i]

        heapify(score)
        numOfPop = 0
        res = [None] * len(score)
        while score:
            x = heappop(score)
            index = x[1]
            print(x)
            numOfPop += 1
            if numOfPop == 1:
                res[index] = "Gold Medal"
            elif numOfPop == 2:
                res[index] = "Silver Medal"
            elif numOfPop == 3:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(numOfPop)
        return res

            
        