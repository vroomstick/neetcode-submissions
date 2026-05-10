class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = Counter(nums)

        for num, count in elements.items():
            if count > len(nums) // 2:
                return num
        