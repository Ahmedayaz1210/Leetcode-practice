'''
Understand:
- Given an array of ints called temperatures, we have to return an answer array where answer[i] represents kind of same index from temperatures but this one tells when is the next warmer day from this day or in tech terms, what is the how many indices do we need to go on right to find the next greater element and how ever many steps we take from current index, we put them in that index's value. and if there is no next greater element to an indicy's value, then we return 0 in that place.
- How long can temps array be?
- how big can each int in temps be?

Match:
- So brute force can be comparing each element to all elements on it's right and storing that value which would be O(n^2)
- but how about if we can use a monotonic stack where we store indicy's next greater element, so stack is in increasing order and we pop each time we find a bigger value which can tell us how far the next one is buried in stack and then store it in answer[i] when popping

Plan:
- so one thing is straight, we will start by storing 0 in all indices of answer because if we can't find next greater we have to return 0 in that position, answer = 0 * [len(temps)]
- now we loop over temps, but using the index and not value because index will be used in answers to store next greater
- then we check while something is already in stack and if that is true, within same statement, is stacks top smaller than current value?, if it is pop it and for that popped index, store in answers current index - popped_index
- then lastly we push the current index into stack
- return answers

Evaluate:
- Was able to fully solve after first learning monotonic stacks
- TC and SC both O(n) because in tc the stack efficiently only loops once and keeps storing next greater which is slightly a bit back tracking logic, sc because we store same len of elements in answers
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_index = stack.pop()
                answers[popped_index] = i - popped_index
                
            stack.append(i)

        return answers
