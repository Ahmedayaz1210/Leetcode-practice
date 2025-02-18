'''
UNDERSTAND:
- Input: An m x n grid "heights" where each cell has an integer and represents the height above water
- The island is surrounded by pacific ocean on the top and left cells and surrounded by Atlantic on the bottom and right cells
- When it rains, the water can fall from the cells with larger int values to the cells with smaller or equal integer values
- Have to find which cells when it rains on them can pass the water to other cells so water can travel both in pacific and atlantic ocean
- We can only move in 4 directions, up down left and right
- Output: Return a list of all cells which can pass water to both oceans
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

MATCH:
- What are trying to do here? Find cells which can flow water into both oceans by having smaller neighboring cells
- Can run a dfs from every cell and check if it reaches both oceans but that means repeating cells which can lead up to extra TC, O(m*n)^2
- We know top and left touches pacific and bottom and right cells touch atlantic 
- How about we move inwards from the sides
- So we first create a set on which cells can flow into atlantic starting from right and bottom and checking higher or = to values
- Same for pacific
- Now the cells in both sets will be our answer
- This reduces TC because we can loop the grid twice seperately and when moving inwards we can mark each cell which can flow to the current ocean we are checking as already visited so we don't have to do it again
- Kind of like a different multi source DFS

PLAN:
- Initialize Rows and Columns size, pacific, atlantic and result sets
- DFS function takes current cell position, current ocean set and previous cell's height so it can be compared (obv for first cell it is going to compare to itself)
    - Check base cases which include out of bounds and if cell is already present in the respective ocean set because if it is no point in checking again and this reduces TC
    - If it doesn't hit base case, we found a valid solution for current ocean so append it to that set
- Loop over top and botom row and send them to dfs function with their respective oceans and heights
- Similarly loop over left and right columns and send to dfs function with their respective oceans and heights
- Lastly loop over grid and check if each cell exists in both atl and pac set, if so append to result list
- Return res list

EVALUATE:
- I got the logic kind of by moving inwards but i was confused on how to solve it, honestly wasn't a really hard question, from previous experience I should have been able to do it
- TC: O(m*n) we loop over grid three times separately and we don't visit cells which have already been checked
- SC: O(m*n) all sets can store the grid in worse case
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS, atl, pac, res = len(heights), len(heights[0]), set(), set(), []

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prevHeight):
                return

            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

