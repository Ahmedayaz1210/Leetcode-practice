'''
UNDERSTAND:
- Input: Given an array of int numbers "nums", where all numbers are unique so no duplicates
- Have to find all subsets from this array
- Subset is all possible selection of elements from the array, it can be empty array, the nums array itself is a subset, any individual number, or any pairs of them, all possible solutions
- Make sure none of the subsets are duplicate, for ex [2,3] and [3,2] are the same and are considered dups
- Output: Return a nested list which contains all the subsets as sublists from the nums array
- TC? SC?
- nums[i]: -10 to 10 inclusive
- how big can nums be? 1 to 10 inclusive
- All elements will be unique

MATCH:
- For all numbers we need to try all possible subsets, which means we have to try adding that number and then taking it out and making a subset and repeating this with all the numbers until we include all of them and not include all of them
- So taking a number, using it and then stepping back and not using it
- Can use the process of backtracking where we can run a dfs on including a number first and then taking it out and finding subsets

PLAN:
- Use two arrays:
  - result: stores all final valid subsets
  - current: tracks the subset we're currently building

- Key Insight: For each number, we must make a yes/no decision
  - When i=0, decide about nums[0]
  - When i=1, decide about nums[1]
  - When i=len(nums), we've decided about every number

- Base Case (i == len(nums)):
  - We've made decisions for all numbers
  - current array now holds a complete valid subset
  - Add current to result and return

- For each decision point i:
  1. Try INCLUDING nums[i]:
     - Add nums[i] to current
     - Explore all possibilities with this number (dfs)
     - Remove nums[i] when done
  
  2. Try EXCLUDING nums[i]:
     - Don't add nums[i]
     - Explore all possibilities without this number (dfs)

- Start decisions from index 0
- Return all found subsets


EVALUATE:
- This is first backtracking problem, this problem was part of the understanding topic so I didn't do it myself, I learned backtracking with this problem and learned with AI
- Recursion for backtracking is hard to track on paper but it helped a lot once I got it
- Seems like a hard topic
- TC: O(n * 2^n) n is for copying the current array at each decision and in worse case it can be all of nums since that counts as a subset, for each element we make 2 decisions, whether to add it or not so for n elements its 2^n
- SC: O(n) excluding the output, because at each call our stack is O(n) n being len of nums because after that we append to res array and return back from the call, also curr can store n elements in worse case
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i + 1)

            curr.pop()
            dfs(i + 1)


        dfs(0)
        return res