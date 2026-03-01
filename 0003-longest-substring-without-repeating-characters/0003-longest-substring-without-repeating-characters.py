'''
Understand:
- Given a string and we have to find the longest contg sequence as a substring where in that subarray no alphabets are repeated twice, how long can substring be with unique alphas
- I mean in the worst case it can be O(26)
- We have to return the len of that longest substring
- There could be multiple substrings which are same longest len
- Actually its not only english letters, it could be symbols and spaces as well so not exactly O(26)

Match:
- Since we are finding a contig sequence we know we can use a sliding window 
- And that window has to be dynamic so expanding and shrinking since we are finding the longest and not a fixed size
- Also since we know we are finding unique characters we can def utilize a hashset to check if that char has already occurred in the window

Plan:
- have left pointer starting at 0
- have hashset to keep track of unique chars
- have a maxLen var starting at 0
- run a loop over given string with r pointer
- now the key point here is that i dont think we first add the element, we would have to check if it already exists
- so we check if curr element at r exists in the hashset, if so remove it but we don't check with if we check with while because what if that element is somewhere in the middle? since we want it to stay contig, we keeping removing elements until we have removen the duplicate so within this while we keep removing element on left pointer and keep moving left forward to shrink the window from left
- then in the end once we are out of while loop we know that element def does not exist anymore so we now append element at pointer r and continue
- now we update maxLen accordingly
- return maxLen out of the loop

Evaluate:
- Solved a medium after solving easys, this felt much easier now
- TC: O(n)
- SC: O(k) i said k because letters, symbols and spaces are finite
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashset = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.discard(s[l]) #using discard because handles error well
                l += 1
            hashset.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen