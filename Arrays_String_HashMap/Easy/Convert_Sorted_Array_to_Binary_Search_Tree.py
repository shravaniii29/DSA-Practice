# Approach:
# Since the array is sorted, choose the middle element as root.
# Elements on the left of mid form the left subtree.
# Elements on the right of mid form the right subtree.
#
# Recursively repeat this process for every subarray.
# Choosing the middle element ensures the BST remains height-balanced.
#
# Time Complexity: O(n)
# Space Complexity: O(log n)  # recursion stack
# Keyword to remember

# Whenever you see:

# Sorted Array + Height Balanced BST

# immediately think:

# Middle Element = Root
# Recursion on Left Half
# Recursion on Right Half

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)