'''
UNDERSTAND:
- Input: Given a list of integers nums, nums may contain duplicates
- Have to return all possible subsets from nums
- Subsets is taking all different selections we can make from the list, which includes empty list as well
- Output: Return a list which contains sublists of all different selections
- TC? SC?
- 1 <= nums.len <= 10
- -10 <= nums[i] <= 10
- This question is the same as the difference between Combination I and II:
    - In Combination I, we had distinct elements and can use same one again and again
    - In Combination II, elements could repeat but we can't use one element again and again
    - Similarly in Subsets I we had distinct elements, but in Subsets II we have duplicates

MATCH:
- Since we need to take a step of choosing a number, trying all possible answers with it and then stepping back, not taking that same number and exploring all answer without taking it
- We can use the process of Backtracking with the help of DFS through recursion
- Choice: Either take a number or don't take it at all, not even its duplicates
- Constraint: No duplicate subsets
- Goal: Find all subsets

PLAN:
- Sort the nums list
- res list
- curr list
- Dfs method which takes current index as parameter:
    - Base case: when i == len(nums): 
        - Append a copy of curr into res 
        - return
    - Append ith num into curr
    - Run back Dfs on it to explore all paths by taking the num
    - Pop it out
    - Now we need to skip over same numbers to avoid getting duplicates
    - Use a while loop to go until len(nums) - 1 (because we check i + 1) and if nums[i] == nums[i+1]:
        - In this case simply increment i
    - Run back Dfs to explore all paths without taking this num
- Dfs starts from 0th index
- return res

EVALUATE:
- Finally solved a backtracking question myself!
- TC: O(n * 2^n)
- SC: O(n) for call stack
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        curr = []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res