'''
Understand:
- Given two strings s and t of lens m and n.
- Have to find smallest substring from s such that all letters of t exist in it and we can have other letters too as long as all t's letters are included and we can also have dups from t
- Return either the min substr or ""
- Check constraints
- In example one this could be one ans but it's not the min but u can see abc exist in it ADOBEC

Match:
- Since finding a contig sequence we can use a sliding window to keep track of the substring
- And since we know we can have duplicates, we need to use hash map instead of a hashset.
- What starts the window is a letter from t 
- What ends a window is if all letters from t have been encountered with the same frequency, else we could exhaust the whole string
- SO I guess the while loop or something in logic has to check that if we have alr encountered smth from t then we keep moving else l shrinks the window until we find a t letter to start the window with
- Actually we don't need to handle that because let's suppose we have EBANC yes it is valid but our logic will know that since all t letters have been included, automatically shrink with l pointer and next check would fall on BANC so that would get checked as well

Plan:
- hashmap_t = {}
- hashmap_s = {}
- min_str = somehow make a big str like inf or smth
- curr_str = ""
- l = 0
- loop over t and fill hashmap_t
- loop over s with r pointer:
    - append letter at r with frequence update in hashmap_s
    - append letter to curr_str
    - while all elements from hashmap_t are in hashmap_s with frequency match:
        - update the min accordinly
        - subtract element at l with 1 frequency
        - subtract element from curr_str
        - move l by one
- return min_str if its not None else return ""
    
Evaluate:
Understanding: This was my first time solving a hard problem in a while. Conceptually, the sliding window + hashmap idea was clear, and I understood how to check for a valid window.

Implementation: The code was tricky, especially tracking frequencies and shrinking the window efficiently. I estimate I solved about 70% of the problem correctly. The main inefficiency was using curr_str operations, which would have made the solution O(n²) instead of optimal O(m+n). Using indices (res = [l, r]) instead is the key improvement.

Progress: Despite minor inefficiencies, this was good practice, and I’m now more confident in handling sliding window + hashmap problems for substrings.
- TC: O(m+n)
- SC: O(m+n)
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap_s, hashmap_t = {}, {}

        # build hashmap_t
        for c in t:
            hashmap_t[c] = hashmap_t.get(c, 0) + 1

        l = 0
        have = 0
        need = len(hashmap_t)

        res = [-1, -1]
        min_len = float('inf')

        for r in range(len(s)):
            # expand window
            c = s[r]
            hashmap_s[c] = hashmap_s.get(c, 0) + 1

            # check if this char satisfies requirement
            if c in hashmap_t and hashmap_s[c] == hashmap_t[c]:
                have += 1

            # shrink window
            while have == need:
                # update result
                if (r - l + 1) < min_len:
                    res = [l, r]
                    min_len = r - l + 1

                # remove left char
                left_char = s[l]
                hashmap_s[left_char] -= 1
                if left_char in hashmap_t and hashmap_s[left_char] < hashmap_t[left_char]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if min_len != float('inf') else ""