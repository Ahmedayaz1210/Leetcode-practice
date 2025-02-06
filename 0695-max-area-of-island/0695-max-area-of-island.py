'''
UNDERSTAND:
- So the question is quite similar to number of islands, just one small change
- Input: m x n grid called "grid"
- 1's in grid = land or land area and 0's in grid = water
- If the 1's are adjacent horizontally and vertically they are basically adding up to be 1 island
- Even a single 1 by itself can be an island. if it does not have any adjacent one's horizontally and vertically
- Output: An integer number which represents the area of the largest island
- What is area here? Area is just the number of adjacent "1" cells the largest island is made up of
- Does grid only contain 0 and 1? Yes
- How many rows and columns can we have? Between 1 and 50 inclusive
- rows is m and columns is n
- Will all grids have an island? No
- Assume all four edges of the grid have water, it means there is conceptually water beyond the grid boundaries, not that the edge cells themselves must be water.
- TC? SC?

MATCH:
- What are we trying to do here? Find all adjacent 1's horizontally and vertically
- This can be thought of as which 1 is pointing or related to which other 1 or a sequence of them
- I am thinking BFS might be helpful because at each cell we can explore all of it's neighbors and find the adjacent 1's
- But DFS fits pretty good too because after finding a 1, we look for the next 1 rather than looking for all the neighbors of the same one, then once dfs hits a dead end, it is going to back track and visit other neighbors of one of the previous one it hit

PLAN:
- Result integer "max_area"
- visited list
- DFS (grid, row, column):
    - Base cases: if row and column go out of bounds or edges, if current cell is visited, if current cell is 0, we simply return on all these statements
    - If base case is not hit then we are at a 1, so we append it to visited, increment current area, check if current area is greater than max so far, update it and move in all 4 directions
- A nested loop to loop over the whole grid
    - Once a 1 is encountered and it is not in visited, we know it's an island even by itself so we send it into DFS function with 4 parameters current_area (starts at 0), grid, row and column (current cell where we encountered 1)
- Return max_area integer

'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(grid, row, col, curr_area):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row,col))
            curr_area = 1
            curr_area += dfs(grid, row+1, col, curr_area)
            curr_area += dfs(grid, row-1, col, curr_area)
            curr_area += dfs(grid, row, col+1, curr_area)
            curr_area += dfs(grid, row, col-1, curr_area)

            return curr_area


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    curr_area = dfs(grid, row, col, 0)
                    if curr_area > max_area:
                        max_area = curr_area


        return max_area