'''
Understand:
- So given a string s we have to find sequence(s) 10 letters long which occurr more than once in the string
- That 10 letter long sequence or substring can only have the letters [A,C,G,T]
- We return all the sequences we can find as a List
- Check constraints

Match:
- Since it has to be one of those 4 letters we can store them in a List [A,C,G,T]
- We have to check if a sequence is occurring more than once, I guess here we can use a hashset instead of a map because we are only checking for more than one occurrence so if its already in hashset and currently we found another occurrence we know its valid and we dont need to store every single occurrence
- Finding a contig sequence tells we can use a sliding window to keep track of the 10 letter substr
NOTE: constraint says s[i] is either 'A', 'C', 'G', or 'T'. which means we never will encounter a letter other than these 4

Plan:
- hashset for seeing if we have already seen this in current window
- left pointer = 0
- sequence = "" for tracking the 10 letter sequences
- ans = [] list to store all possible sequences
- loop over s with r pointer:
    - append current character to sequence
    - If sequence is of len 10, check if its in hashset, if so append to ans
    - else append to hashset
    - remove char at l
    - move l by 1
- return ans


'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashset = set()
        l = 0
        seq = ""
        ans = set()

        for r in range(len(s)):
            seq += s[r]
            if len(seq) == 10:
                if seq in hashset:
                    ans.add(seq)
                    print(ans)
                else:
                    hashset.add(seq)
                seq = seq[1:]
                l += 1
        return list(ans)