'''
UNDERSTAND:
- Inputs:
 - Given an integer "num"
 - Given an integer "k" 
- Treat num as a string and we have to find all contiguous sequences:
 - Contiguous sequence is of length k
 - num is divisible by that contiguous sequence of length k
- When dividing treat both num and substring an an integer
- Also num can have leading 0's, so 007 is valid
- 0 is not a divisor, so basically if you have any sequence with all 0's in it, you skip it
- Questions:
 - Length of num? 1 to 10^5
 - how big can k be? 1 to <= length of num as string

MATCH:
- A sliding window problem where the window size is always fixed
- We have to find contiguous substrings so we always have a window

PLAN:
- Create an output counter
- Treat num as a string and create a substring "window" from index 0 to index k
- run a loop on num as a string:
- check if num as an int is divisble by window as an int and remainder is 0, if so increment counter else do nothing - - Drop left most element and add right element

Evaluate:
- My code passed 180 out of 183 test cases, i couldn't handle cases where k = 1
- My code run time is O(n) since converting num to string is O(n) and the loop is n - k + 1 which is basically O(n) since k is smaller than n
'''
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        '''
        counter = 0
        numStr = str(num)
        
        window = numStr[:k-1]

        for i in range(k-1,len(numStr)):
            window += numStr[i]
            windowInt = int(window)
            if windowInt < 1:
                continue
            elif num % windowInt == 0:
                counter += 1
            window = window[1:]

        return counter
        '''

        counter = 0
        numStr = str(num)
        window = numStr[:k]

        for i in range(len(numStr) - k + 1):
            windowInt = int(window)
            if windowInt != 0 and num % windowInt == 0:
                counter += 1
            if i + k < len(numStr):
                window = window[1:] + numStr[i + k]

        return counter

