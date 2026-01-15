class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1

            while l <= r and not s[r].isalnum():
                r -= 1

            if l <= r and s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True



'''
* Understand: 
* Have to validate if a string is palindrome, palindrome is basically a string which after you remove spaces and non letters/numbers characters it should read same forward and backward. If this is the case return true else return false
* From examples you can see an edge case is if string is empty it is automatically true so that could be first if statement
* s will be at least one character which could be just a space too and goes up till 2 * 10^5
* and s is also only ascii characters

* Match:
* Seems pretty straightforward, run two pointers one from start going forward and one from end going backwards and compare characters on both pointers, if they are the same keep continuing and if at any point there is a mismatch instantly return False. 
* I guess we run the pointers until right one's index is less than left one's which means there is an overlap or if they are the same
* This would be O(n) TC and O(1) SC because we loop the whole string and only use two pointers
* We have to also make each char lowercase, skip over empty and non alpha chars

* Plan:
* Initialize our left and right pointers
* Run a while loop until they are on same index or left <= right
* compare chars at both positions after converting to lowercase and checking if alphanumeric using the built in function which handles spaces as well
* if they dont match return False
* Else in the end return True

* Evaluate:
* Got 90% of the problem, it was just I had to check if l<=r at every stage which kind of confused me but got the logic myself!
* TC: O(n) since looping once
* SC: O(1) since only using two pointers
* If we didn't have alnum function we can check do smth like this def is_alnum(char):
    # Check if it's a lowercase letter (a-z)
    if ord('a') <= ord(char) <= ord('z'):
        return True
    # Check if it's an uppercase letter (A-Z)
    if ord('A') <= ord(char) <= ord('Z'):
        return True
    # Check if it's a digit (0-9)
    if ord('0') <= ord(char) <= ord('9'):
        return True
    return False

and if we need to create our own .lower function
def chars_equal_ignore_case(char1, char2):
    # Convert both to same case before comparing
    # If uppercase, add 32 to get lowercase
    c1 = ord(char1)
    c2 = ord(char2)
    
    # Normalize to lowercase
    if ord('A') <= c1 <= ord('Z'):
        c1 += 32
    if ord('A') <= c2 <= ord('Z'):
        c2 += 32
    
    return c1 == c2
'''