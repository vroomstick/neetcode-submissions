class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        elements = {}

        for i in range(len(nums)):
            if nums[i] not in elements:
                elements[nums[i]] = 1
            else:
                elements[nums[i]] += 1

        for item in elements.items():
            element, count = item

            if count > len(nums) // 2:
                return element


        