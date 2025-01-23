'''
UNDERSTAND:
- A string "digits" as input which just contains a sequence of digits
- Have to find all combinations of letters from those digits
- Each digit is mapped with some letters, they can be 3 or 4 letters as you can see in the picture
- Output: Have to return all combinations which can be made from "digits"
- Numbers can only be 2-9 inclusive
- Which means 0,1 or anything else is exluded since it doesn't have any letters
- From pic I am assuming each digit can only have either 3 or 4 letters
- 0 <= digits.length <= 4
- TC? SC?
- If given only one digit then just return it's letters

MATCH:
- Problem is kind of similar to subsets and combination sum because here we are making combinations
- For each letter we are trying all combinations with other letters of same digit or rest of the digits from our input string
- This is a process of backtracking
- So exploring all paths for a letter is DFS
- Use recursion for DFS
- Choices: For each letter in a digit, we try all other letters in all other digits
- Constraint: For each digit in our input, we must use exactly one of its letters in each combination
- Goal: Final all combination of letters from the digits string

PLAN:
- First we need to map letters and digits, 2-9 inclusive
- Make res list and curr string
- Dfs algorithm with i as parameter (tells us which digit we are on)
    - base case: since we only use one letter from each digit at a time so when i == len(digits) we append to res and return, no need to append copy of curr since it is a string
    - For each digit and for each of it's letters we loop over the next digit's all letters and combine them one by one, if like the next digit does not exist then we just explored all combinations
    - For each letter in our current digit:
        - We append it to curr and move to next digit
- run dfs from 0th index
- return res

EVALUATE:
- Finally solved a Backtracking question all by myself
- TC: O(n * 4^n) so n is from creating strings of len(n) and 4^n is in worse case for 7 and 9 we can loop over 4 digits
- SC: O(n) because call stack goes up to n and then return back hitting base case
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []    

        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            for letter in digit_to_letters[digits[i]]:
                dfs(i + 1, curr+letter)
        dfs(0, "") #strings are immutable in python so we need to use it as a param rather than global var
        return res