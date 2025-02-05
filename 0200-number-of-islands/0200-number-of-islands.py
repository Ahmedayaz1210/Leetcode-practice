'''
UNDERSTAND:
- Input: m x n grid called "grid"
- 1's in grid = land or land area and 0's in grid = water
- If the 1's are adjacent horizontally and vertically they are basically adding up to be 1 island
- Even a single 1 itself can be an island if it does not have any adjacent one's horizontally and vertically
- Output: An integer number which represents how many islands are there
- Does grid only contain 0 and 1? Yes
- How many rows and columns can we have? Between 1 and 300 inclusive
- row is m and column is n
- Will all grids have an island? No
- Assume all four edges of the grid have water, it means there is conceptually water beyond the grid boundaries, not that the edge cells themselves must be water.
- TC? SC?

MATCH:
- What are we trying to do here? Find all adjacent 1's horizontally and vertically
- This can be thought of as which 1 is pointing or related to which other 1 or a sequence of them
- I am thinking BFS might be helpful because at each cell we can explore all of it's neighbors and find the adjacent 1's
- But DFS fits pretty good too because after finding a 1, we look for the next 1 rather than looking for all the neighbors of the same one, then once dfs hits a dead end, it is going to back track and visit other neighbors of one of the previous one it hit

PLAN:
- Result integer
- visited list
- DFS (grid, row, column):
    - Base cases: if row and column go out of bounds or edges, if current cell is visited, if current cell is 0, we simply return on all these statements
    - If base case is not hit then we are at a 1, so we append it to visited and move in all 4 directions
- A nested loop to loop over the whole grid
    - Once a 1 is encountered we know it's an island even by itself so immediately increment result and then we send it into DFS function with 3 parameters grid, row and column (current cell where we encountered 1)
- Return result integer
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0' or (row, col) in visited:
                return

            visited.add((row,col))
            dfs(grid, row+1, col)
            dfs(grid, row-1, col)
            dfs(grid, row, col+1)
            dfs(grid, row, col-1)


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1' and (row,col) not in visited:
                    result += 1
                    dfs(grid, row, col)

        return result
