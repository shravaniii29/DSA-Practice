class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid          # Store current occurrence
                right = mid - 1    # Continue searching on the left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans