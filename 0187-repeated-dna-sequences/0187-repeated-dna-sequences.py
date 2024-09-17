'''
UNDERSTAND:
- Given a string s, which is a DNA sequence
- Find all of the 10 letter long sequences which repeat more than once
- Dna sequence is a string made up of only 'A', 'C', 'G', 'T'
- We have to return all of the possible substrings which occurr more than once
- Substrings have to be contiguous sequences and can be multiple of them and have to be exactly 10 letter long
- Does it have to be exactly 10?
- String is only going to contain ACTG?
- How long can s be? >=1 and <= 10^5
- Any time and space constraints?
- All the letters are going to be only Uppercase? Yes
- Does the way we return output matter in the array? No
- What if s is < 10? Empty list

MATCH
- Window size is fixed, have to atleast find 10 letter long window
- Has to be contiguous sequence
- Tells us sliding window technique
- HASH MAP TO KEEP TRACK OF SEQUENCES OCCURRING ONCE

PLAN 
- Create a Window, add window to hash set
- Keep removing from left and expanding from right
- Check if the window exists in hash set, if so append it to the result list
- Originally we can make result list a hashset so it never repeats since we only have to return one occurrence
- Then in the end we can convert result set to a list and return it back

EVALUATE
- Overall got the solution, only thing I had to look up was that we can create a second set for result instead of a list so only one occurrence is added and later convert it to a list when returning answer
- Time complexity: O(n), looping through the entire string once
- Space complexity: O(n). in worst case our result can have n repeating sequences
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = set()
        result = set()

        window = ""
        for r in range(len(s)):
            window += s[r]
            if len(window) == 10:
                if window in sequences:
                    result.add(window)
                    print(result)
                sequences.add(window)
                window = window[1:]

        return list(result)
