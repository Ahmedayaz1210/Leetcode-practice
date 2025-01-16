'''
UNDERSTANDING:
- Inputs: Given a 2D array representing a board, each sublist in this array represents a row of alphabets, each index in a sublist contains only one alphabet. Also given a string "word" 
- Have to find word inside of our 2d array
- The word can be made by using adjacent cells, they can be horizontally or vertically next to each other
- Output: A boolean value which determines if word exists in board or not
- TC? SC?
- m == board.length because all rows make up the board length
- n = board[i].length because the amount of elements in ith row will tell us num of columns
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.
- Edge Case: Need to keep track of visited cells so we don't loop over them again

MATCH:
- We need to basically do a bunch of trying and testing
- Have to see what happens if we take this alphabet and then what happens if we don't
- Using a process of backtracking
- Choice: 4 choices 
    (i+1, j) : down
    (i-1, j) : up
    (i, j+1) : right
    (i, j-1) : left
- Constraint: Can only move adjacent and also need to check if we have already visited a cell or not
- Goal: Find word inside the board
- Can use a set to keep track of which cells we have already visited
- Can use DFS and recursion to explore each path

PLAN:
- Initialize a set which can keep track of our visited cells
- rows = len(board), cols = len(board[0])
- run dfs(r, c, i): i is the curr cell we are on
    - if i == len(word):
        return True (first base case, if we are at the end it means we looper over everything)
    - now we need to check in which cases do we return false, also our base case(s)
    - if we go out of bounds of board or board[r][c] != word[i] or (r,c) in visited: return False
    - if nothing happens, it means so far so good
    - append (r,c) in visited
    - run dfs four times on all adjacent cells and store it inside a res variable, so if any of these calls return True or False it will be stored in here
    - now remove (r,c) from our visited set
    - return res
- loop over the board
- send in each row and column to dfs and start with index 0
- (we loop over the whole thing because inside dfs we actually don't loop over the board we only look at adjacent cells of a path which is so far validating our path)
- whatever is returned from dfs calls, store inside a variable
- return True immediately if its true, we do this because else it is going to loop over the whole thing and only return last path's boolean value
- return false


EVALUATE:
- Wasn't able to solve because first time working with 2d arrays or boards
- TC: O(m * 4^n) we go through the whole board and then we also make 4 calls each time and we make these calls len(word) times
- SC: O(n) because at max we store amount of len(word) calls in stack and cells in our set
- m is num of cells on board, n is len of word
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        rows, cols = len(board), len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r,c) in visited:
                return False
            visited.add((r,c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            visited.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                res = dfs(r,c,0)
                if res:
                    return True
        return False

        