'''
Understand:
- Given a string s and and int k, we have to find longest substring in s so that all chars in s are the same, in this case it can be only uppercase english letters
- But we get k amount of replacements, so in our string we can change any k amount of characters
- So kind of an analogy that whatever is the most occurring letter, change k letters to that one to keep the sequence going
- So we can't have any empty string there has to be at least one letter but k can be 0
- Check constraints for futher explanation

Match:
- So a sequential substring tells me that I can use sliding window approach where we can have two pointers creating a window of the longest substring
- Since we need to keep track of all the elements in the window to see what needs to be replaced we can use a hashmap because we kind of need to know highest occurring one and how we can use k tries to change other letters

Plan:
- Left pointer starts at 0
- hashmap = {}
- longest sub = 0
- run loop over string with pointer r
    - maybe we can start by simply appending the element at r into hash map
    - now we check if the curr window size - highest occurring letter from hashmap is > k, if so we know that we are out of k tries 
        - now we subtrack l element by 1 from hashmap
        - l += 1
    - we update the highest window size
- return longest sub

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        longestSub = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            currWinSize = r - l + 1
            highestElement = hashmap[max(hashmap, key=hashmap.get)]
            if currWinSize - highestElement > k:
                hashmap[s[l]] = hashmap.get(s[l], 0) - 1
                l += 1
            longestSub = max(longestSub, r - l + 1)
        return longestSub
