'''
UNDERSTAND:
- So the first thing to understand is how does a Queen move in chess? Up, down, left, right and diagnol
- Input: Given an integer n
- Have to create an n x n chess board and try to place n queens on it such that no queen can attack another queen
- Have to find all possible ways we can place n queens on n x n board
- Output: Return a list which contains sub list aka all possible solutions
- TC? SC?
- How big can n be? 1 <= n <= 9
- Each sublist will be of len(n)
- And each string or row in sublist will be len(n) as well
- Edge case: Not all boards will have a solution because 2x2 and 3x3 can't fit 2 and 3 respectively

MATCH:
- Since we are doing trial error for each placement we try, we take a step, then come back and take another step, a process of backtracking
- To explore a possible path for a queen in it's depth we can use DFS
- For DFS we can use recursion
- Choice: Which column should I put the queen in for each row?
- Constraint: No queens can share row, column, or diagonal
- Goal: Find all possible solutions where we can place n queens

PLAN:
- Result list
- column set, this will keep track that we don't put any queens in same column
- pos diag set, same thing with pos diag, we do this by doing (r+c) check notebook for drawing
- neg diag set, (r-c)
- The reason why we don't track rows here is because in our backtracking we are looping over rows so by design we never need to check for rows seperately, we do that in our recursion which only moves forward
- Current board, we will start off by putting only "." in it and then change it on the go inside our dfs
- Run Dfs (r as parameter which is same thing as current row or current queen because we are placing queens row by row)
    - Base case: When we have placed n amount of queens on the board we have a valid solution
    - Now since function loops over rows, for each row we need to loop over all columns
        - We need to see this col already exists in our col or diag sets
            - if so we need skip over this col
        - Else we add this col to our sets
        - We also put "Q" in this cell
        - Now move ahead in function and try placing next queen
        - Now undo everything, remove the col for all sets
        - Put back "." instead of "Q"
    - Run DFS from 0th row
    - Return res list
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board] # takes each row which is a sublist and converts it into a string for our output
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res