class Solution:
    def isValid(self, s: str) -> bool:
        # first let's check if there is nothing in our string we simply return True
        if not s:
            return True
        

        stack = []
        # looping through our string
        for p in s:
            if p == '(' or p =='[' or p == '{':
                stack.append(p)
            elif p == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif p == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif p == '}':
                if not stack or stack.pop() != '{':
                    return False
        
        return not stack
        
'''
* I have done this problem before so shouldn't be hard and I don't think it counts as cheating because I did it like 3 months ago
* I kind of do know that it will use a stack for sure to keep track of the pattern of paranthese or brackets
* We are given a string and we need to loop through it and see if all of the opening brackets have a corresponding closed bracket of the same type.
* We also need to keep track that it's in the same order like ({}) and not ({)}
* This is where last in first out of stacks property will help us
* **Solution**
* We loop through our string and if we encounter an open parentheses we add it to the stack 
* And if we encounter a closed one, we pop one from the stack which is our last added and in order to validate our answer that one has to be the corresponding same type of opening bracket or parentheses
* This could be done in **O(n) time complexity**
* I was able to get it, the only mistake I made is at the end I didn't check whether the stack was empty or not, if it's not empty we return false because then we have a mismatch so we use return not stack
'''