'''
Understand:
- Given a 2d matrix with only integers. Each row is in ascending order, which means every element is greater than the one before and it applies throughout which means a row's starting element is greater than previous row's last
- Have to return True if target int is in matrix else false
- TC should be O(log(m*n))
- How big can ints be? look at constraints
- How big can matrix be? look at constraints
- Strictly ints? yes
- m is outer list, n is inner nested list
- all rows are same size

Match
- Since we know matrix is in ascending order throughout, we can basically get rid of half the matrix at once by keep checking the mid value and seeing if our target would be towards it's left or right so basically using binary search

Plan:
- So first we need to identify the middle row and see if target is greater than it's last element, if so we need to move to right arrays
- else if its smaller than middle's first element than it is in left arrays
- if neither then obv it's in this one, wherever in the point the middle array has been found
- once we have identified the middle row, we break out of first loop of finding the row and now we run our regular binary search algorithm on this subarray, so it's two layers, finding that array where element exists and then in that array either finding the element or returning False if it doesn't exist, this approach is better than looking at last element of every subarray

Evaluate:
- I was able to get the logic but since I don't have much experience with 2d array, I struggled a bit with mode
- TC: O(log(m * n)) since in first loop we cut down m rows by log and in second we cut down the n cols by log
- SC: O(1) since we only use single var pointers
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break #identified the middle now we run our basic BS
            
        # if element isn't in here, to avoid out of bounds we handle this
        if not (top <= bot):
            return False
        mid = (top + bot) // 2 #finding the same row from previous while loop where top and bot ended
        l = 0
        r = COLS - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
