'''
UNDERSTAND:
- Input: An m x n "grid"
- Grid can only be made up of three integers. 0 - empty cell, 1 - fresh orange and 2 - rotten orange
- If a fresh orange is 4 direction adjacent to a rotten orange, it becomes rotten in the next minute, in our case the next loop or iteration
- Here rotten's 4 adjacency only means the 4 next to it, don't assume the whole column or row of that rotten orange
- Once we have gone through the whole grid we need to see how many minutes it took for all the fresh oranges to turn rotten
- If a fresh orange never went rotten after the whole traversal we return -1
- Output: Integer number representing how long in minutes it took all fresh oranges to turn rotten or -1 even if one remains fresh
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- We are not limited to one rotten orange so we can have multiple

MATCH:
- So the key moment like the walls and gates problem is that we don't have one rotten orange, we can have multiple
- Any time we have a question like this where we need to find the distance or time from all the things which change our grid's values we can use multi source BFS
- So first we find all the rotten oranges and from there we move outwardly to find all the fresh oranges and do in place modification to fresh oranges
- Only tricky thing is how do we know if any fresh oranges remain, do we loop the grid again? Maybe we loop the gird again in the end, it won't add anything new to TC so if any cell remains 1 you return -1

PLAN:
- First let's initialize our variables
- Rows int, cols int, visit set and a queue deque
- Loop over the whole grid and append any rotten oranges into the queue
- Initialize time variable, so from each rotten orange cell as we progress outwardly we keep incrementing it
- While there is something in queue:
- Loop over len of queue
- Change each cell's value to 2 representing rotten oranges
- Move in 4 directions and add all adjacent cells in queue and visit set use a helper function
- Increment time
- In the helper function check all bases cases which are out of bounds, if a cell is not 1 or not already in visit
- Append to visit and queue
- In the end loop over the grid again check if any cell is 1 if so return -1 else return time


EVALUATE:
- Problem was easy because island and treasure problem was same to this where we used multi source BFS
- TC: O(m*n) for looping over grid 
- SC: O(m*n) for storing all cells
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols, visit, q, fresh = len(grid), len(grid[0]), set(), deque(), 0

        def addCell(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or
                (r, c) in visit or grid[r][c] == 0
            ):
                return
            visit.add((r, c))
            q.append([r, c])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        time = -1
        while q:
            time += 1
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time