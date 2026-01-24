class MinStack:

    def __init__(self):
        self.stack = []
        self.mem = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mem:
            self.mem.append(min(self.mem[-1], val))
        else:
            self.mem.append(val)


    def pop(self) -> None:
        self.mem.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mem[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
* Understand
* More of a design problem where we have to implement different functions.
* Given 4 functions, push takes an element and appends it in the stack.
* Pop remove top element of stack
* top just shows the top element but doesn't remove
* getMin returns the minimum element in stack
* Tricky part is everything has to be done in O(1) time which is easy for push pop and top but confusing for getting the minimum which makes me think we can't always have min at top because that's sorting and defeats constant time. maybe we need to keep track of min at all times?
* How big can val be? check constraints
* How many times can we call these functions? and do we only call on non empty stacks? check constraints

* Match:
* Easy to tell it's a stack problem.
* For push and pull we can use python's default stack functions
* For getting the top we can just look at stack's [-1] because this give's the last element which in our case would be the top one.
* I am thinking maybe we can have a global min var and each time push function is called, we can update it and getMin just returns that, but this has a slight problem, if we remove the min, how do we determine the next min in constant time?
* So we will be using extra space, as in the time at stack where at each element we add, at that point this was the min, and once we remove from top we remove it's memory from extra space by removing last element

* Plan:
* Init function: Initialize the stack and extra space
* push function, use python's function to append into the stack and if it's first element add it to extra space, else keep going and compare with last element in extra space, of course in code this would get handled itself so dont have to write if else statement
* pop, use python's function to pop out the top and remove last element from extra space to erase its memory
* top retrieve -1 element from stack
* getMin return last element in extra space

Evaluate:
* TC: O(1)
* SC: O(n) worst case you append everything and don't pop
* I was able to write the code myself but took me a hint and bit to understand we can keep track of min at memory at each point, so would give myself 80% of the credit. 
'''