#In leetcode its given that the array is sorted in ascending order and we have to find the index of the target value or the index where it would be if it were inserted in order.
# We can use binary search to achieve this in O(log n) time complexity.
# So its a Binary Search problem.

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left