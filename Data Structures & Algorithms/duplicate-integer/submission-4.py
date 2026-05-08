class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()

        for i in range(len(nums)):
            if nums[i] not in counts:
                counts.add(nums[i])
            else: 
                return True

        return False
            
                


