class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1

            else: 
                counts[nums[i]] += 1
        
        for num in counts:
            if counts[num] > 1:
                return True

        return False
            
                


