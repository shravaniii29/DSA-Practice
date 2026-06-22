"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Approach:
Use a dictionary to store previously seen numbers and their indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        visited_numbers = {}

        for i in range(len(nums)):
            needed_number = target - nums[i]

            if needed_number in visited_numbers:
                return [visited_numbers[needed_number], i]

            visited_numbers[nums[i]] = i