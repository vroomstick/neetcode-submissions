class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                streak = max(streak, counter)
                counter = 0
            else:
                counter += 1
                streak = max(streak, counter)

        return streak
        