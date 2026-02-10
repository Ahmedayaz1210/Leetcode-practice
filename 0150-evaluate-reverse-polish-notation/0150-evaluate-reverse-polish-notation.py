'''
Understand:
- Given an array of strings called tokens, where each token is either an math operand (*,/,+,-) or an integer (could be neg)
- We have to find reverse polish notation: the way I can interpret from the examples is that before we see any operation we need at least two integers to perform the operation on. And once we go from there each time we see an operation we hold off, but as soon as we see an int and we see that we saw an operation earlier, we tie them together and we use the operand and operation to perform the calculation on whatever result we got from previous operands and operation so kind of operating in a parentheses situation to get the correct calculation.
- The division between two integers always truncates toward zero. Something like int(a/b)
- How big can tokens be?1 to 10 to the 4
- How big can each int be? -200 to 200
- Can we only have 4 operations? yes
- Will we have at least two operands before facing an operation? Yes

Match:
- so we have to kind of combine two operands with an operation, so we hold off each time we see an operand, let's use a stack and put that operand in it and each time we encounter an operation we pop out the most recent operand from stack and perfrom calculation with previous result. or we store the result and push it back in stack and just pop twice

Plan:
- Ini stack and result variable
- run a loop over tokens.
- while the stack is not empty and current element is an operand we push it in stack
- we have to also be careful of converting string token integers into integers
- once we hit an operand, we pop twice, perform the appropriate calculation and push result back. now if it's a division make sure to use int(a/b) so it cuts the post decimal result
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if stack and token in operations:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(b / a))
                elif token == '+':
                    stack.append(a + b)
                else:
                    stack.append(b - a)
            else:
                stack.append(int(token))

        return stack[-1]
            
