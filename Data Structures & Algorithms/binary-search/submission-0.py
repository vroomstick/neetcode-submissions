class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            median = left + (right - left) // 2

            if target < nums[median]:
                right = median - 1
            elif target > nums[median]:
                left = median + 1
            else:
                return median

        return -1
        