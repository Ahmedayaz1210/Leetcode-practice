class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        first let's check if both strings are the same length, if not then return false instantly
        if len(s) != len(t):
            return false
        Let's put all of the characters from s into the hashset
        Then we run a loop on t and if the character at the iterator is in the hashset we keep moving
        else return false
        
        if len(s) != len(t):
            return False
        
        hashset = set()
        for i in s:
            hashset.add(i)

        for j in t:
            if j not in hashset:
                return False
        return True
        '''

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

        

        
# * So basically in this question we are given two strings and we are checking if both have the exact **same characters** which would mean they have to be the **same Length**. 
# * Seems like another question where I could use a hashset to remember the characters in the first array and then match with the second.
# * Also seems like the same question as contains duplicate, so this is a pattern of Arrays and hashing.
# * Let's use hashset as extra memory to optimize the time complexity: **Time complexity and Space Complexity will be : O(n)**
# * Would a hashset work for this because a hashset does not contain any duplicate values and here there could be duplicates.
# * let's try solving with a hashset
# * Solution passed 43/48 test cases but still good attempt..
# * **Another solution**
# * saw this in discussions but what if i sort both arrays and then compare each value, if both are the same then it's true else false
# * **Another solution**
# * We can use hashmaps to keep count of each character's occurrences and compare them
# * so in python we can use dictionaries
# * Here time and space complexity are both O(n)
# * what if interviewer wants us to make space complexity O(1) so we don't use extra space. then we just use sorted method but even sorting algorithms take space complexity.
# * even a hasmap can atmost take 26 characters after that it is repetition
        