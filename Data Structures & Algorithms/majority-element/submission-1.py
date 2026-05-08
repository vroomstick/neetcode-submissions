class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        elements = {}

        for i in range(len(nums)):
            if nums[i] not in elements:
                elements[nums[i]] = 0
            elements[nums[i]] += 1

        for element, count in elements.items():
             if count > len(nums) // 2:
                return element


        