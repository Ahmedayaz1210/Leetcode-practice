'''
UNDERSTAND:
- Input: Given a list of integers "nums"
- Have to find all permutations of it and return them
- Permutations is basically all the different sequences of the numbers in which they can be rearranged
- Output: Return a list which has all the permutations as sublists
- TC? SC?
- Have to make sure none of the sublists are exactly the same
- Guaranteed that all ints in nums are unique
- nums can be 1- 6 len
- nums[i] can be -10 to 10 inclusive

MATCH:
- Since we have to try each number at each position, we can use backtracking
- So we can use a number at a position and then go back and use it in a different
- Choice: Which unused number should go in this position
- Constraint: All permutations need to have all the numbers so when a len(perm) == len(nums)
- Goal: Find all permutations

PLAN:
- res list
- curr list
- run dfs
    - base case is if len of curr === len of nums: we append curr to res and return back
    - now run a loop over nums:
        - check if curr num is not in curr:
            - append it
            - run dfs again
            - now pop it out and move forward with the next number and append this in another position

EVALUATE:
- TC is O(n!) for amount of permutations and O(n) for copying curr each time: O(n! * n)
- SC is same because we store n! permutations and n for recursion depth
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs()
                    curr.pop()
        dfs()
        return res