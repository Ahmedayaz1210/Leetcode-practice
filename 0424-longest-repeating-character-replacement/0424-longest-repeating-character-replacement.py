'''
Understand: 
- Given two inputs string s and k int, you can perform k operations on s, operation here means that replacing any char from s to an uppercase alphabet and you can do this k times 
- Asked to find the longest chain of same uppercase chars, so looking at example 1 we replace both As with 2 Bs or both Bs with two As so we can get either chain of all As or all Bs but in this case both will be len 4 so doesn't matter - In the end we return the longest sequence of same char 
- Does s only have uppercase alphas? yes - How long is s? 1 to 10^5 - how big is k? 0 to len of s

Match:
- So we definitely need a hashmap to keep track of occurences of each alphabet.
- I think logic here is we will have a dynamic sliding window where right pointer loops the list and left moves accordingly. 
- I think the logic is that we keep checking the window size and compare it with keeping track of highest frequency character, when we subtract we get the number of elements which need to get changed and if that number exceeds k that's when window becomes invalid for example 2:
when window is "AABAB" window size is 5, A is occuring the most with 3 A's, 5-3 = 2 elements need to get changed but we can only change one so that's invalid now
- And if it any point it doesn't satisfy we keep running the while loop and update left accordingly.

Plan:
- left pointer at 0
- Hashmap = {}
- longest_window = 0
- for r in range(len(s)):
    - add the right element to hashmap
    - window_size = r - l + 1
    - max_freq = i dont know how to get max value from hashmap right now
    - if window_size - max_freq > k:
        - subtract l occurence from hashmap and if 0 then element gets deleted
        - l += 1
    - longest_window = max(longest_window, window_size)
return longest_window

Evaluate:
- Got the logic but had a lot of mistakes, need to do more easys before jumping into mediums
- SC: O(26) or O(1) in worse case
- TC: O(n) looping once
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        longest_window = 0
        max_freq = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1 #if doesnt exist do 0 else increment
            window_size = r - l + 1
            max_freq = max(max_freq, hashmap[s[r]])

            if window_size - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1

            longest_window = max(longest_window, r - l + 1)
        return longest_window