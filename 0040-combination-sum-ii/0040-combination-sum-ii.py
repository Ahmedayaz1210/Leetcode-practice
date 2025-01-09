'''
UNDERSTANDING:
- Input: Given list of distinct ints and a target integer
- Have to find all unique combinations from candidates where the sum of that sublist = target
- Can only use a number once
- Our sublists have to be unique from each other, meaning two sublists can't have same frequency of each number: [2,3,4] and [3,2,4] are the same thing
- Output: Have to return a list which contains all sublists from combinations which add up to target
- TC? SC?
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30
- Feels like a combination of both subsets and Combination I because this time we actually can't repeat same number
- The different thing over here is we can have a number repeating inside of our candidates which can give us similar combinations so if we are not taking a number then we don't take any of its frequencies

MATCH:
- Need an algorithm where we can try different combinations
- So we try one number in different combinations, see what happens, then don't include and see what happens
- A process where we move forward then backtrack and test another solution
- Can achieve the process of tracking one path with DFS so we take a number and explore it in depths
- Can achieve DFS using recursion

PLAN:
- Sort the list so we can skip over same repeating nums
- res list : to store all combinations
- Run dfs from start of candidates
    - if target == sum: add curr to res and return back
    - if candidates has been exhausted or curr total has exceeded target: we return back
    - Make a choice of appending new number
    - And move forward
    - Or make a choice of not appending it, meaning pop it
    - Now we want to skip the same numbers which can repeat in candidates so we run a while loop until we encounter a new number and list doesn't get exhausted, sorting made it easier
    - And move forward
- Run dfs from start
- Return res

EVALUATE:
- TC: O(n log n + n * 2^n)
- SC: O(n)
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, total)

        dfs(0,[],0)
        return res