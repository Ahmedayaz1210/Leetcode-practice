'''
UNDERSTAND:
- Input: Given an m x n "board" where each cell can have a char value of either "X" or "O"
- We can flip all the "O"'s which aren't the edge or border cells
- But if any "O" on the edge is adjacent to any innner "O"s we can't flip those inner ones either
- By Adjacent we can move in 4 ways, up down left right
- Output: We don't have to return anything so only in place modification of the board
- How big is the grid?
- How many rows and columns?
- Only 'X' and 'O' can be the val?
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

MATCH:
- Problem doesn't seem too hard
- So we are trying to find all border O's and then find all adjacent O's from there
- So finding a path of O's from a border O tells us we have to explore paths so BFS or DFS
- Let's go with DFS

PLAN:
- Initialize rows, cols integers, a set which keeps track of which Os not to flip
- DFS method takes in current cell's position
    - Base cases: Check for out of bounds, being 'X' or already being in our set
    - If base case not hit then simpy add it to the set
    - Run dfs in all 4 directions
- Loop over border rows and cols
    - if any O is encountered, send it into dfs function to mark all its adjacent Os
- Loop over the whole board
    - Check if it's an O cell
        - If so, check if it's not in our not to flip set, if so flip it

EVALUATE:
- Question felt quite easy, seems like I am getting the hang of graph problems
- TC: O(m * n) to loop over grid to check and flip Os as necessary
- SC: O(m * n) if we have all Os in worst case
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, dontFlip = len(board), len(board[0]), set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] == 'X' or (r,c) in dontFlip:
                return
           
            dontFlip.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    if (r,c) not in dontFlip:
                        board[r][c] = 'X'

