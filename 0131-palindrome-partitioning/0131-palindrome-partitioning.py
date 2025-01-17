'''
UNDERSTAND:
- Input: Given a string s
- Have to find all palindromes inside the string, so a letter by itself will always be a palindrome and then from there on we can see how many more do we have
- Output: Return all palindrome sequences, each sequence should be a seperate sublist and make up to represent s
- TC? SC?
- 1 <= s.length <= 16
- s contains only lowercase English letters.
- If no palindromes exist then we will have just one sublist with each letter being seperate
- So in worst case each sublist will have len(s) chars
- At each point we think how long of a palindrome can i build from here


MATCH:
- Have to try different sequences and see which ones make up a palindrome
- Exploring different paths for each char says we have to use Backtracking
- Can use DFS with recursion to achieve this
- Choice: how many more characters should I include in my current substring so it's within constraints? 

- Constraints: 
    - Each piece within a partition must be a palindrome
    - We must use every character in s exactly once (no skipping characters, no reusing characters)
    - The order of characters must be preserved (we can't rearrange letters): ["b","a","a"] would NOT be valid for example 1 even though each piece is a palindrome, because it doesn't preserve the order of characters in s

- Goal: Find all sequences which add up to make s

PLAN:
- res = []
- curr = []
- dfs(i)
    - base case: if i == len(s): res.append(curr.copy())

'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(i):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    curr.append(s[i : j + 1])
                    dfs(j+1)
                    curr.pop()
            
        dfs(0)
        return res


    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
            