'''
UNDERSTAND:
- Given two strings s1 and s2 as input
- Have to find at least 1 to all of permutations of s1 within s2
- Remember s1's permutation has to be a contiguous sequence, letters can't break, meaning letters in s1 can't have letters which are not in s1, when a s1's permutation is present in s2, like example 2
- Length of s1 and s2? 1 <= s1.length <= s2.length <= 10^4
- s1 and s2 are only english letters? Yes Followup: Lower case? Yes
- Time constraints for optimality?
- Space constraints? 
- Should we assume that the input strings s1 and s2 will always be valid, or should we handle any specific edge cases?
- Can any letters in s1 repeat within itself?

MATCH:
- Permutations is tricking us
- Question is to basically find all occurrences of letters in s1 within s2 but as a contiguous sequence
- Finding all occurrences? Can use a hash map
- Looking for a contogious sequence window? Fixed sliding window technique

PLAN:
- Create two hash maps both for s1 and s2
- Put s1's letter and their corresponding occurrences values in hash map as a key value pair
- Run a loop over s2 with a fixed size window of len(s1)
- Append the current letters in the window inside s2's hashmap
- See if occurrences for all letters match, if so return true
- Else shrink window from left and take out that letter's occurrence from s2's hashmap and expand window from the right, appending that letter in s2 hash map
- In the end return false because we never found a permutation
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hashmap = {}
        s2_hashmap = {}
        
        # Populate the s1_hashmap with character counts from s1
        for s in s1:
            s1_hashmap[s] = 1 + s1_hashmap.get(s, 0)
        
        l = 0
        for r in range(len(s2)):
            # Add the current character to the s2_hashmap
            s2_hashmap[s2[r]] = 1 + s2_hashmap.get(s2[r], 0)
            
            # If the current character count in s2_hashmap exceeds the count in s1_hashmap
            # or if it's not in s1_hashmap, we need to shrink the window from the left
            while s2_hashmap.get(s2[r], 0) > s1_hashmap.get(s2[r], 0):
                s2_hashmap[s2[l]] -= 1
                if s2_hashmap[s2[l]] == 0:
                    del s2_hashmap[s2[l]]  # Remove the character from hashmap if the count is 0
                l += 1
            
            # If the window size matches the size of s1, check for permutation match
            if (r - l + 1) == len(s1):
                if s1_hashmap == s2_hashmap:
                    return True
        
        return False
