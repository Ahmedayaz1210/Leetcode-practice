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