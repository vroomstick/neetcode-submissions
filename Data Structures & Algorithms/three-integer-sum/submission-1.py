class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            l = i + 1
            r  = len(nums) - 1
            while l < r:
                current_sum = nums[l] + nums[r] + nums[i]
                if current_sum == 0:
                    if ([nums[i], nums[l], nums[r]]) not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                elif current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
        return result