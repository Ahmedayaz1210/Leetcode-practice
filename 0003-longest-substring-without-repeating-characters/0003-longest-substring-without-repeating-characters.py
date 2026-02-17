'''
Understand:
- Given a string as input, we need to find the longest substring so that within that substring each char which is present, occurs only once.
- Duplicate chars tells me that we can use a hashset over here
- Examples make the problem pretty straightforward
- How long can s be? 0 to 5 ^ 10^4
- s only consists of alphabets? nope symbols and spaces can be in there too

Match:
- Finding the longest substring can be done using a sliding window where we create the window with two pointers and keep expanding until chars are unique
- For keeping track of unique chars we can use a hashset so it ensures nothing is repeated

Plan:
- l = 0, hashset = {} and max = 0
- run a loop over s with r
    - now as long as s[r] keeps existing in hashset, we keep moving window from left side inwards, so remove s[l] from hashset and move l over
- now once s[r] doesn't exist, append this new element and check if max needs to get updated
- return max

- So a key thing which kept confusing me was why do we run a while loop and not if, the reason is if we have abcbde, we get abc and when r gets on b now we want to start next string at c right so we keep deleting from hashset until left pointer comes to c, now left is on c, c is only element in hashset and r keeps moving and we get cbde

Evaluate:
- Was a bit tricky to be honest, got the logic couldn't get code, so 50% credit only
- TC: O(n) looping once
- SC: O(n) in worst if we store the whole s in hashset
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, hashset, maxlen = 0, set(), 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen
        