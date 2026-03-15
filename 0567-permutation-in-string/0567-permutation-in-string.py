'''
Understand:
- Given two strings s1 and s2 we have to see if any permutation of s1 exists in s2 as a substring
- Permutation means rearranging a string so it's still using the same characters 
- So over here we have to see if in s2 we can find any sequence of s1
- if it exists return true else false
- check constraints

Match:
- I guess we can simplify this problem by thinking all we need to do is check if chars in s1 occur in s2 sequentially and if they occur with same frequency
- So sliding window for sequential check and hash map for the frequency

Plan:
- hashmap s1 = {}
- hashmap s2 = {}
- First we can loop over s1 and store letters with occurrences in the hashmap
- l = 0
- now we loop over s2 with pointer r
    - we append or increment element in s2 hashmap
    - run a while loop checking if element in s2 hashmap at r has higher occurrence than same element in s1 hashmap
        - if so decrement left pointers occurrence from s2
        - make sure u delete that element if its occurrence is 0 else u wont be able to compare hashmaps correctly
        - no move l pointer
    - check if curr window and s1 len matches and both hashmaps == each other: return true
- return false

Evaluate:
- Got the question! Was just a bit confused why we need to add each element into s2 but it's necessary for the algorithm to run the while loop and keep removing that char until satisfied
- TC: O(n) n = len(s2)
- SC: O(26)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hashmap = {}
        s2_hashmap = {}

        for s in s1:
            s1_hashmap[s] = s1_hashmap.get(s,0) + 1

        l = 0
        for r in range(len(s2)):
            s2_hashmap[s2[r]] = s2_hashmap.get(s2[r],0) + 1

            while s2_hashmap.get(s2[r],0) > s1_hashmap.get(s2[r],0):
                s2_hashmap[s2[l]] -= 1
                if s2_hashmap[s2[l]] == 0:
                    del s2_hashmap[s2[l]]
                l += 1
            if (r - l + 1) == len(s1) and s1_hashmap == s2_hashmap:
                return True
        return False