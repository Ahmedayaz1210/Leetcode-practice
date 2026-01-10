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

        

        

        