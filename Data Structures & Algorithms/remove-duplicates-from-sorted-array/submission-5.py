class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, k = 0, 1, 1

        while l < r <= len(nums) - 1:
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
                r += 1
                k += 1

            else:
                r += 1

        return k