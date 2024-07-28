class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        g=[] #matrix stores the continous horizontal ones.
        for r in range(len(grid)):
            count = 0
            a = []
            for c in range(len(grid[0])-1, -1, -1):
                if grid[r][c]:
                    count+=grid[r][c]
                    a.insert(0, count)
                else:
                    count = 0
                    a.insert(0, 0)
            g.append(a.copy())

        for c in range(len(grid[0])): #grid stores the continous vertical ones.
            for r in range(len(grid)-2, -1, -1):
                if grid[r][c]:
                    grid[r][c] += grid[r+1][c]
        ans = 0
        row = 0
        while row < len(g): #computing left-right edges
            col = 0
            while col < len(g[0]):
                if g[row][col]:
                    ans+=2
                    col+=g[row][col]
                else:
                    col+=1
            row+=1

        col = 0
        while col < len(grid[0]): #computing top-bottom edges
            row = 0
            while row < len(grid):
                if grid[row][col]:
                    ans += 2
                    row += grid[row][col]
                else:
                    row+=1
            col+=1
        return ans