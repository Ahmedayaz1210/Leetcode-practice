'''
Understand:
- Given two sorted arrays, we just have to return the median number from them. Median means the middle number, now obviously if it's an odd length then we return the middle else we do the calculation.
- Since we have to do it in O(log (m+n)), m+n tells me that we have to merge them first and do in log time
- ans can be returned as a float
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

Match:
- m + n tells to merge both sorted arrays
- log tells we can use Binary search
- Wait no, I got it a bit wrong, even though the arrays are sorted it doesn't mean that last element of nums1 is always smaller than first element of nums2, they aren't sorted sorted, they are just sorted within themselves, this is what makes it a hard problem
- This means merging is not possible since it will always be O(m+n) and we will have to touch every element, so we have to find the median without merging
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = sorted(nums1 + nums2)
        n = len(x)

        if n % 2 == 1:
            return x[n // 2]
        else:
            return (x[n // 2 - 1] + x[n // 2]) / 2