'''
UNDERSTAND:
- Input:
 - Given a string
- Have to find the longest substring without repeating characters
- It is a substring not a subsequence so it has to be conitguous
- As soon as a char repeats, we stop looking at that substring and move on
- Output:
 - return the longest non repeating substring length, so returning an INTEGER
Questions:
 - Length of given string: 0 to 5 * 10 ^4
 - What are the characters in the string, symbols, integers, letters? letters, digits, symbols and spaces
- Edge case: if length is 0: we return 0, if 1 we return 1
- If we have a space: we trim it out

MATCH:
- Substring with a contiguous sequence tells that we will have to create a window 
- Window will be shrinking and growing, looking whether a duplicate is encountered or not
- To find duplicate: use hashMap, to keep track of the occurences of each character within the substring

PLAN:
- Keep a dictionary to track all occuring characters with their positions
- Keep a longest substring counter
 - Reason we put position in value is if we encounter a duplicate we move left pointer to one over the first occurence of our repeated character
- Keep a left pointer at 0, put it in dictionary
- Start a loop from 1 - end of string
- right starts at 1
- keep a current window size counter
- If right doesn't exist in dictionary, add it with it's position, increment right, increment current window size counter
- else if it does, take element from dictionary and it's position, pop it out of dicitionary, do max between longest substring counter and current one and move left pointer to one over the position of that occuring element, but it's first occurence.
return longest substring counter
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        longestSub = 0
        l = 0
        hashMap = {}
        
        for r, char in enumerate(s):
            if char in hashMap and hashMap[char] >= l:
                l = hashMap[char] + 1
            else:
                longestSub = max(longestSub, r - l + 1)
            
            hashMap[char] = r
        
        return longestSub