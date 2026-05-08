class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        high = len(nums) - 1
        scan = 0

        while scan <= high:
            if nums[scan] == 0:
                nums[scan], nums[low] = nums[low], nums[scan]
                scan += 1
                low += 1
            
            elif nums[scan] == 1:
                scan += 1

            elif nums[scan] == 2:
                nums[scan], nums[high] = nums[high], nums[scan]
                high -= 1
     
                

            



        