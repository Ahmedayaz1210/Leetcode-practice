class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if len(nums) <= 1:
        #     return False
        # if k < 1:
        #     return False

        # i, j = 0, 1

        # while (j <= len(nums)-1):
        #     if abs(i-j) <= k:
        #         if nums[i] != nums[j]:
        #             j += 1
        #         else:
        #             return True
        #     else:
        #             i += 1
            

        # return False

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
