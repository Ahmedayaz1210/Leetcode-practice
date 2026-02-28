'''
Understand:
- So we know k is our fixed window or the length we need to check at each stage
- Basically we have to find all length k substrings that when divided on num the remainder is 0, so like num is pretty much divisible by that substring within itself
- 0 can't be a divisor of anything so if a substring is all 0s that does not count
- I guess leading 0s mean that something like 04 is counted as just 4 if k = 2
- We have to return how manu substrings we can make
- num is strictly an int

Match:
- Since we are looking for contig substrings we can use fixed sliding window technique
- Along with that we just need a variable to store the current substring as a number

Plan:
l = 0
currSub = ""
ans = 0

run a loop over num with r pointer:
append r into currSub
if currSub reaches k len:
    convert currSub into an int 
    if num / int(currSub) gives remainder 0, also check if curr sub as int is 0 in that case we dont increment either
    if so increment ans
    take out l from currstr and move on with l

return ans

Evaluate:
- Did it in about 20 minutes, all by myself, def getting better, even caught my mistakes and realized dont need l pointer
- TC: O(n)
- SC: O(k)
'''
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        currSub = ""
        ans = 0
        numStr = str(num)
        for r in range(len(numStr)):
            currSub += numStr[r]
            print(currSub)
            if len(currSub) == k:
                currNum = int(currSub)
                if currNum != 0 and num % currNum == 0:
                    ans += 1
                currSub = currSub[1:]
        return ans

