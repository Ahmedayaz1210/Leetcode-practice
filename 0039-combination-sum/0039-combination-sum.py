'''
UNDERSTAND:
- Input: Given list of distinct ints and a target integer
- Have to find all unique combinations from candidates where the sum of that sublist = target
- Can use a number multiple times inside our sublist but our sublists have to be unique from each other
- Meaning two sublists can't have same frequency of each number: [2,3,3] and [3,2,3] are the same thing
- Output: Have to return a list which contains all sublists from combinations which add up to target
- TC? SC?
- Guranteed we won't have more than 150 combinations
- Each num in cands is unique
- 2 <= candidates[i] <= 40
- 1 <= candidates.length <= 30
- 1 <= target <= 40
- We need to stop trying a number when sublist goes >= target 

MATCH:
- Need an algorithm where we can try different combinations
- So we try one number in different combinations, see what happens, then don't include and see what happens
- A process where we move forward then backtrack and test another solution

PLAN:
- Result list to store combinations of different answer sublists
- Current list which will store the current combination we are building
- Current Sum variable which keeps track of the current list's sum
- Under some condition we append current into our result list
- Run dfs with current index and sum as inputs:
    - Base cases: if current sum > target:
        - break out
    - if current sum == target:
        - append curr sublist to res list, make a copy of curr
    - after doing both we take our the current idx num right?
- dfs(0 index, 0 sum)
- return res

choices: either take a num again or take next
constraints: sum has to be exact target
goal: find all combinations


EVALUATE:
- TC: O(2^(t/m)) t is target and m in min val in candidates
    - The intuition here is that at each call we can make 2 decisions and then in worse case the max calls we can make at each depth is how long it takes smallest value to get to target which is t/m

- SC: O(t/m) same reason because that's how long depth will be
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0,[],0)
        return res