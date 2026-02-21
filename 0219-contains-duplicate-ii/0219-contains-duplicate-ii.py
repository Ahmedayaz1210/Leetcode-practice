'''
Understand:
- Basically what we have to do is take the int nums array and see if at any point the elements at indicies i and j have the same int and both are <= k indices apart.
- if so return true else false
- remember i and j have to be distinct indices, you can't return true if they are on same
- This means condition is never valid if array only has one element

Match:
- Since we know we are kind of given a fixed number and we can't go outside that range, we can use sliding window method but obviously we don't care to keep track of elements inside the window, we just care about i and j and this window can be dynamic since it is <= k but max we can go is k

Plan:
- l = 0
- for r in range
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l+=1

            if nums[r] in window:
                return True
            window.add(nums[r])

        return False



        