class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif stack:
                o = stack.pop()
                if (c == ')' and o != '(') or (c == ']' and o != '[') or (c == '}' and o != '{'):
                    return False
            elif  c == ')' or c == ']' or c == '}':
                return False
        return not stack
                    
'''
* Understand: 
* Given a string with ONLY shown parentheses and we have to validate the string under the 3 given conditions, so if a ( is open then it needs to be closed, closed in the correct order this is basically the difference between example 4 and 5, basically last one opened needs to be closed first and you go from there backwards, also they have to be closed by the same type of bracket.
* Does s only have these chars strictly? yes
* How big can s be? check constraints

Match:
* So we know that whatever was opened last gets closed first to validate and it also has to be the same type of bracket, essentially this would be last opened has to be first closed, LIFO, which is a characteristic of a stack. 
* Each time you encounter an open bracket you put it in the stack, and once you hit a closing bracket, you check the last one you just put in the stack and see if it's the corresponding open bracket, if so it's validate keep moving else false instantly

* Plan:
* Initialize our stack
* Run a loop over string
			* check if its any of the open brackets, append it in stack
			* if its a closed one, check if there is smth in stack and take out the last top from stack and compare, if they are same pair, keep moving else go ahead and return False and also if the stack is empty return False, we also have to check if we are encountering a close bracket and there is nothing in stack so return False
* return not stac because it's only true if stack if empty, else this would be that an open bracket didn't have a closed one which makes it false 

* Evaluate:
* Solved by myself, caught on edge cases pretty well and did in about 30 minutes
* TC: O(n) looping once, SC: O(n) worst case if all open brackets
'''