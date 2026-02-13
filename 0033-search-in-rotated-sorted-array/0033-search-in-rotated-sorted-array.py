'''
Understand:
- Given a sorted array nums which has all distinct values
- nums could be left rotated by a certain number meaning you push elements towards left by whatever the count is, lets call it k, k is unknown and once we move left, if a number is going beyond 0, for example -1, it gets pushed towards end of nums
- nums is 0 indexed, remember
- We have to find a given number and return its idx, target from this ascending array but it could be rotated and we don't know how many times it has been rotated towards left
- We also have to solve this in O(log n) so we can't just search linearly because O(n) is too simple, we need to optimize it.
- Look at constraints for value boundaries

Match:
- Binary search is one algorithm we can use to solve this in O(log n)
- I think the catch could be identifying the unknown k over here.
- Even though it is rotated, in a certain way it is still ascending.
- Key here is that, it will always be the case that one side of the array is always sorted, in given examples both are but better example is 
        [6,7,0,1,2,4,5]
        Split at mid (index 3, value 1): left = [6,7,0], right = [2,4,5]
        Left sorted? No (has the rotation point)
        Right sorted? Yes
- We can identify which half is sorted by comparing first and last value in that half, or left and middle and middle and right
- Now once we have identified which one is sorted and which one isn't, we can first check sorted and see if target is bigger than left and smaller than right than it has to be in sorted else we go to unsorted and after exhausting that we either find it or return -1

Plan:
- Run the binary search

Evaluate:
- This problem was a bit hard, wouldn't give myself credit for doing it, I even struggled a bit with the code, i forgot to check if one half isn't sorted then check other one
- SC: O(1)
- TC: O(log n) from BS
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[l] <= nums[mid]:
                    if target >= nums[l] and target <= nums[mid]:
                        r = mid -1
                    else:
                        l = mid + 1
                else:
                    if target >= nums[mid] and target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
                    
        return -1
