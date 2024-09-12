'''
UNDERSTAND:
- Input:
 - String 's' and integer 'k'
- From string have to take out at most k characters
- Replace them with characters which occur before it
- To form a contiguous sequence of the same characters
- For each substring all the characters in it have to be exact same as the starting out
- Questions: 
 - How long can s be? 1 to 10^ 5
 - How big k can be? 0 to length of s 
 - Is s only letters? Yes uppercase letters only
- Edge cases:
 - If length of s is 1, we return 1
 - If k is 0, we don't replace anything, we return longest substring of same chars from the s

MATCH: 
- Replacing chars with one(s) occurring before it or them
- Keep track of the longest substring or window of those same repeating characters
- We use Sliding Window approach

PLAN: 
- left pointer = 0
- longestSub = 0
- kcounter = 0
- currSub = ""
- run loop over the string with the right pointer
 - Check if the char on right pointer == char on left pointer:
  - add right pointer char to the currSub
 -  if not the same and kcounter < k:
  - add left pointer element to curSub
  - ++ kcounter
 - if they are not the same and kcounter >= k:
	 - longestSub = max(longestSub, len(currSub))
	 - currSub = ""
	 - kcounter = 0
	 - left pointer ++ 
	 - right pointer goes back to left pointer as well
- return longestSub

EVALUATE:
- Not the best code
- Check each possible window and still have to move right pointer to left pointer
- My code: O(n^2)
- Passed 26/45 test cases:
- Ex: fails "ABBB"
        l, r = 0, 0
        longestSub = 0
        kcounter = 0
        currSub = ""

        while r < len(s): 
            if s[l] == s[r]:
                currSub += s[r] 
                r += 1
            elif kcounter < k:
                currSub += s[r]  
                kcounter += 1
                r += 1
            else:
                longestSub = max(longestSub, len(currSub))
                currSub = ""
                kcounter = 0
                l += 1
                r = l 
        
        longestSub = max(longestSub, len(currSub))
        
        return longestSub

NEETCODE:
- I KNEW that we would be using hashMap somehow because we have to keep track of elements in the middle of window and their occurences technically
- Have to take length of window and count of the most occuring char in hashMap, hashMap - count[most occurring] = num of characters in our window that we need to replace (confirming if this is < k, if yes we have a valid window)
- Finding most occurring char from hashMap will be O(26) because only 26 alphabets in worst case
- Now with this logic we implement sliding window
- It's about how many we need to replace, we don't have to replace it, I think that's the trap here
- This way we only loop once and then our window takes care of the rest, because it can shrink from left to validate how many changes we need
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res  = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res








