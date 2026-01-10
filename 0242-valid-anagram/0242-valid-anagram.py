class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1

            if t[i] in t_hash:
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1

        if s_hash == t_hash:
            return True

        return False

"""
For cleaner code you can simplify return to return s_hash == t_hash
Instead of nested if statements for occurences, do s_hash[s[i]] = s_hash.get(s[i], 0) + 1


* Understand:
		* Essentially checking if the string t has same characters as string s and they are just rearranged. if yes return true else return false
		* we are given the constraints, so we have at least one character in each string, it can't be empty
		* maybe another edge case could be if they are the same words? but no way to instantly check that and return true, it would be same time because we would be checking for each character
		* something which could help off the bat checking if both strings are the same length if not instantly return false
* Match:
		* i think the optimal way or the firs thing in my mind comes to use a hashmap, store each character and it's occurrence for both strings and see if they match or not
* Plan:
		* check if both strings are same length to confirm we are on right track
		* initialize the hashmaps
		* since they are the same length confirmed by our first if statement, we can run one loop and store for both
		* see if both == each other? if so return true else false, yes in python u can use == to compare
* Review: Everything looks good
* Evaluate: 
		* TC: Looping over both at once so O(n) + O(n) simplified to just O(n)
		* SC: O(n) x 2 so O(n) but since lowercase chars we can say O(26) or O(1) simplified
"""

