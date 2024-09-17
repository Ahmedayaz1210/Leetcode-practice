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

My code:
        s1_hashmap = {}
        s2_hashmap = {}
        for s in range(len(s1)):
            s1_hashmap[s1[s]] = 1 + s1_hashmap.get(s1[s],0)
        print(s1_hashmap)
        
        l = 0
        for r in range(len(s2)):
            
            if s2[r] not in s1_hashmap:
                if s2[l] in s2_hashmap:
                    s2_hashmap[s2[l]] = s2_hashmap.get(s2[l]) - 1
                l += 1
            else:
                s2_hashmap[s2[r]] = 1 + s2_hashmap.get(s2[r],0)
                print(s2_hashmap)
                if s1_hashmap == s2_hashmap:
                    return True

        if s1_hashmap == s2_hashmap:
                return True
        return False


EVALUATE: 
- My code was almost correct, once again had logic error from start so implementing one small missing thing got confusing
- The trick was to add right pointer letter from the start and then check if any letter's value in s2 is greater than s1's if so take it out and move right
- Another trick was rather than comparing the two hashmaps, since we were validating window, we had to match window size with s1's length

Time: O(n) n is length os s2
Space complexity: In worst case, will have all letters so O(26) == O(1)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hashmap = {}
        s2_hashmap = {}
        
        for s in s1:
            s1_hashmap[s] = 1 + s1_hashmap.get(s, 0)
        
        l = 0
        for r in range(len(s2)):
            s2_hashmap[s2[r]] = 1 + s2_hashmap.get(s2[r], 0)
            
            while s2_hashmap.get(s2[r], 0) > s1_hashmap.get(s2[r], 0):
                s2_hashmap[s2[l]] -= 1
                if s2_hashmap[s2[l]] == 0:
                    del s2_hashmap[s2[l]]  
                l += 1
            
            if (r - l + 1) == len(s1):
                if s1_hashmap == s2_hashmap:
                    return True
        
        return False
