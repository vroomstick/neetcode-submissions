class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        elements = {}

        for num in nums:
            if num not in elements:
                elements[num] = 0
            elements[num] += 1

        for element, count in elements.items():
             if count > len(nums) // 2:
                return element


        