class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k = 0, 1, 1

        while i < j <= len(nums) - 1:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1

        return i + 1

        