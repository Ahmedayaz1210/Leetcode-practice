class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                #with this our value will never go negative
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

        '''
        * Looks like a very similar problem to container with the most water, the only difference looks like is math is a bit seperate and tricky
* Defnitely same pattern of running two pointers and checking mininum of the both to see how it works
* **Solution**
* This time our pointers won't be starting from opposite sides instead will be one after the other or something
* Remeber first and last won't store anything since they are boundaries and anything outside it will just fall
* Also will have to keep track of the surrounding elements too of the current elements because those cna create boundaries as well
* I can of get it but checking the previous and front ones are being a bit tricky so going to watch a video
*  The trick is to take max height of left and max of right and take minimum those maxes and subtract from our current element
*  if answer is negative that means you can't trap water there and that's basically 0
*  There is a solution with O(n) memory: by making maxLeft and maxRight arrays and a minimum of them array 
*  But with two pointers we can make it O(1) memory:
	*  Start with putting pointers at index 0 and last index
	*  Have two variables maxL and maxR, which we will update as we move through to the center
	*  we are going to take one with smaller value (maxL and maxR) and shift it, just like we did in previous questions
	*  The reason why thos trick works is because no matter how big our right is for example if our left is small like 0 or 1 it can only store that much of water
*  **Time complexity will still be O(n)**
        '''