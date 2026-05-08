class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()

        for i in range(len(nums)):
            if nums[i] in counts:
                return True

            counts.add(nums[i])
        return False
            
                


