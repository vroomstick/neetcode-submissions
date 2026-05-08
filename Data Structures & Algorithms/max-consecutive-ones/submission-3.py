class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        streak = 0

        for i in range(len(nums)):
            if nums[i] != 1:
                counter = 0
            else:
                counter += 1
                streak = max(streak, counter)

        return streak

        