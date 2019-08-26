# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        last, i = 0, 1
        while i < len(nums):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]
            i += 1
        print("nums is " + str(nums))
        return last + 1
