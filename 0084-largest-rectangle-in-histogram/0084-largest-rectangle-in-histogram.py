class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

'''
* Understand:
* Given an array of ints called heights where each heights[i] is the height of a bar and i is always 1 indicating width of the bar and also 1 indicy. 
* We have to find the consecutive amount of indicies of which's area (lxw) adds up to be the highest from all of the array. 
* And in that area we always take the height of the minimum of the bars
* So for example in Example 1, the reason we got 10 is we have height = 5 and 6 at indices 2 and 3 respectively, we take min of the two which is 5 (this makes a rectangle shape as you can see) and then since it is two indices width = 2, height = 5, width = 2, 5x2 = 10 area. That's the largest rectangle we can see
* According to example 2 bottom right, a bar by itself can be the largest rectangle as well
* How big is heights array and how big can each height be? Check constraints

* Match
* Thinking if two pointers would work here? Don't think so because then we would have to use extra memory to keep track of everything in a chain
* In brute force you would check every possible out rectangle that can be made, it's area, which would be nxn or O(n^2) not very optimal
* I think the height is very critical to notice here since width is just a chain of 1 + 1 + 1 and so on like that
* Basically if bar i is your rectangle, you extend it till you hit a bar shorter than it on both sides
* So the core problem is: For EACH bar, efficiently find:
* Nearest smaller bar on the left and Nearest smaller bar on the right
* This sounds like a monotonic stack problem where we need to keep track of next smaller element

* Evaluate:
* Couldn't solve the problem, don't have in depth knowledge of monotonic stacks
* TC and SC is O(n)

'''