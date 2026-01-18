class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, ans = 0, len(height) - 1, 0
        l_max, r_max = height[l], height[r]

        while l < r:
            if l_max < r_max:
                l+=1
                l_max = max(l_max, height[l])
                ans += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
        return ans

'''
* Understand: Given an array of pos integers where each integer at an index represents height of a bar, the width of each bar is 1 representing one index, we have to find how many blocks of water we can store without it overfilling
* So basically if one block is height two, the next one is height one and the next one is height 2 we can only store one block of water in between because on both sides second block stops the overflow and u can stack a block on top of middle's one
* This makes it obvious that water can't be stored at index 0 and last since water will fall out of their left and right side respectively
* Look at constraints of how big n can be, how big height can be

* Match:
* So if we closely look we have to always keep track of the biggest blocks on left and right side but we need to know the smaller of the two to keep track of overflow, this tells me we need two pointers at all time keeping track from both sides

* Plan:
* For each position or index, the water level is determined by max at left and max at right and minimum of the two to avoid overflow

* Evaluate: 
* So I couldn't solve the problem but I got half of the concept down
* Basically O(n) space time solution is a bit more easier to come up in interview because there you run through the array once from left to right and store max on left and right of each position and then in the end u take min of the two maxes and subtract from current position's value and if its negative it basically means 0 water else u add it in final answer
* In O(1) space solution it's a bit tricky but you can store the maxes in a variable by only moving the smaller of the two pointers
'''